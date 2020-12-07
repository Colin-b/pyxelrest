import datetime
import logging
from typing import Union

import dateutil.parser
import dateutil.tz

logger = logging.getLogger(__name__)


def to_date_time(value: str) -> Union[str, datetime.datetime, datetime.date]:
    """
    Convert to date-time or date as described in https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14
    :param value: string representation of the date-time or date
    :return: date or datetime instance or string if None
    """
    if not value:
        return ""
    # dateutil does not handle lower cased timezone
    if value[-1:] == "z":
        value = value[:-1] + "Z"
    datetime_with_service_timezone = dateutil.parser.parse(value)
    if datetime_with_service_timezone:
        # Changed in python 3.6: The astimezone() method can now be called on naive instances
        # that are presumed to represent system local time.
        if not datetime_with_service_timezone.tzinfo:
            return datetime_with_service_timezone
        # Conversion cannot be performed for dates after year 3000, best effort and return in provided timezone
        if datetime_with_service_timezone.year > 3000:
            return datetime_with_service_timezone
        # Conversion cannot be performed for dates <= to 1970-01-01 best effort and return in provided timezone
        if datetime_with_service_timezone.year < 1971:
            return datetime_with_service_timezone
        return datetime_with_service_timezone.astimezone(tz=dateutil.tz.tzlocal())
    return value


class Flattenizer:
    def __init__(self, all_responses: dict, status_code: int, json_definitions: dict):
        self.__values_per_level = {}
        self.__indexes_per_level = {}
        self.__header_per_level = {}
        self.__all_rows = []
        self.__flatten_header = []
        self.__all_flatten_rows = []
        json_response = response(status_code, all_responses)
        self.schema = (
            json_response.get("schema", json_response) if json_response else {}
        )
        self.json_definitions = (
            json_definitions if json_definitions is not None and self.schema else {}
        )

    def _reset(self):
        self.__values_per_level = {}
        self.__indexes_per_level = {}
        self.__header_per_level = {}
        self.__all_rows = []
        self.__flatten_header = []
        self.__all_flatten_rows = []

    def _init_values_per_level(self, row, level):
        if not self.__values_per_level.get(row):
            self.__values_per_level[row] = {}
        if not self.__values_per_level[row].get(level):
            self.__values_per_level[row][level] = []

    def _extract_values_and_level(self, data):
        self._reset()
        self._set_values_per_level(0, 0, "", data, 0, self.schema)

    def _set_values_per_level(
        self, row, level, header, value, column_index, json_definition
    ):
        # Because "0" or "False" are considered as "not value", this condition cannot be smaller
        if value is None or value == [] or value == {}:
            self._set_value_on_level(row, level, header, "", json_definition)
        else:
            if isinstance(value, dict):
                self._set_values_per_level_for_dict(
                    row, level, value, column_index, json_definition
                )
            elif isinstance(value, list):
                self._set_values_per_level_for_list(
                    row, level, header, value, column_index, json_definition
                )
            else:
                self._set_value_on_level(row, level, header, value, json_definition)

    def _set_value_on_level(self, row, level, header, value, json_definition):
        self._init_values_per_level(row, level)
        self.__values_per_level[row][level].append(
            {
                "header": header,
                "value": self.convert_simple_type(value, json_definition),
            }
        )

    def convert_simple_type(self, value, json_definition):
        if isinstance(value, str):
            field_format = json_definition.get("format") if json_definition else None
            if (
                not field_format and "items" in json_definition
            ):  # Sometimes it can happen that array definition is returned as a single element
                return self.convert_simple_type(value, json_definition.get("items", {}))
            if field_format == "date-time" or field_format == "date":
                value = to_date_time(value)
            else:
                # Return first 255 characters otherwise value will not be valid
                value = value[:255]
        return value

    def _set_values_per_level_for_dict(
        self, row, level, dict_value, column_index, json_definition
    ):
        """
        For a dict, each value is set on the current row and level.
        """
        ref = json_definition.get("$ref")
        if ref:
            ref = ref[len("#/definitions/") :]
            json_definition = self.json_definitions.get(ref)
            properties = json_definition.get("properties")
        else:
            properties = {}
        for dict_key in dict_value.keys():
            json_definition = properties.get(dict_key, {})
            self._set_values_per_level(
                row,
                level,
                dict_key,
                dict_value[dict_key],
                column_index + 1,
                json_definition,
            )

    def _set_values_per_level_for_list(
        self, row, level, header, list_values, column_index, json_definition
    ):
        """
        Each item of a list corresponds to a row.
        The first item belongs to the current row.
        A list corresponds to a nested level.
        """
        # This new level should be displayed next to the list column.
        if level + 1 not in self.__indexes_per_level:
            self.__indexes_per_level[level + 1] = column_index

        # In order to avoid losing key in case this list has a key, add a column without value
        self._init_values_per_level(row, level)
        self.__values_per_level[row][level].append({"header": header, "value": ""})

        json_definition = json_definition.get("items", {})

        # Iterate through the list
        # Create and Update all required rows for the first list value
        self._set_values_per_level(
            row, level + 1, header, list_values[0], column_index + 1, json_definition
        )

        # Create and Update all required rows for the other list values
        # As other rows might have been created, always recompute the actual row number
        new_row = len(self.__values_per_level) - 1
        for list_value in list_values[1:]:
            new_row += 1
            # Clone first row until current level
            for previous_level in range(0, level + 1):
                self._init_values_per_level(new_row, previous_level)
                self.__values_per_level[new_row][
                    previous_level
                ] = self.__values_per_level[row][previous_level]
            self._set_values_per_level(
                new_row,
                level + 1,
                header,
                list_value,
                column_index + 1,
                json_definition,
            )

    def to_list(self, data):
        logger.debug("Converting response to list...")
        self._extract_values_and_level(data)
        # Extract Header and Rows
        for row in self.__values_per_level.values():
            row_values_per_level = {}
            self.__all_rows.append(row_values_per_level)
            for level in row.keys():
                level_values = row[level]
                row_values_per_level[level] = [
                    level_value["value"] for level_value in level_values
                ]
                if level not in self.__header_per_level:
                    self.__header_per_level[level] = [
                        level_value["header"] for level_value in level_values
                    ]
        # Add blanks to Rows shorter than others
        for level in self.__header_per_level.keys():
            for row in self.__all_rows:
                if level not in row:
                    row[level] = [""] * len(self.__header_per_level[level])
        # Flatten Header
        for level in self.__header_per_level.keys():
            if level in self.__indexes_per_level:
                related_to_index = self.__indexes_per_level[level] + 1
                self.__flatten_header[
                    related_to_index:related_to_index
                ] = self.__header_per_level[level]
            else:
                self.__flatten_header.extend(self.__header_per_level[level])
        # Flatten Rows
        for row in self.__all_rows:
            flatten_row = []
            self.__all_flatten_rows.append(flatten_row)
            for level in row.keys():
                if level in self.__indexes_per_level:
                    related_to_index = self.__indexes_per_level[level] + 1
                    flatten_row[related_to_index:related_to_index] = row[level]
                else:
                    flatten_row.extend(row[level])
        # Remove unnecessary columns that may appear for lists TODO Avoid adding this in the first place
        if self.__flatten_header != [""] and not self.__flatten_header[0]:
            self.__flatten_header = self.__flatten_header[1:]
            self.__all_flatten_rows = [
                flatten_row[1:] for flatten_row in self.__all_flatten_rows
            ]
        if not self.__flatten_header or self.__flatten_header == [""]:
            if self.__all_flatten_rows and self.__all_flatten_rows != [[]]:
                logger.debug(
                    f"Response converted to list of {len(self.__all_flatten_rows)} elements."
                )
                return self.__all_flatten_rows
            logger.debug("Response converted to empty list.")
            return [""]
        self.__all_flatten_rows.insert(0, self.__flatten_header)
        logger.debug(
            f"Response converted to list of {len(self.__all_flatten_rows)} elements."
        )
        return self.__all_flatten_rows


def response(status_code: int, responses: dict):
    if str(status_code) in responses:
        return responses[str(status_code)]
    return responses.get("default")
