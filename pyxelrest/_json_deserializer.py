import datetime
import logging
from typing import Any

import dateutil.parser
import dateutil.tz

logger = logging.getLogger(__name__)


def to_date_time(value: str) -> str | datetime.datetime | datetime.date:
    """
    Convert to date-time or date as described in https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14
    :param value: string representation of the date-time or date
    :return: date or datetime instance or original string if conversion failed
    """
    # dateutil does not handle lower cased timezone
    if value[-1:] == "z":
        value = value[:-1] + "Z"

    try:
        dt = dateutil.parser.parse(value)

        # Changed in python 3.6: The astimezone() method can now be called on naive instances
        # that are presumed to represent system local time.
        if not dt.tzinfo:
            return dt

        # Conversion cannot be performed for dates after year 3000, best effort and return in provided timezone
        if dt.year > 3000:
            return dt

        # Conversion cannot be performed for dates <= to 1970-01-01 best effort and return in provided timezone
        if dt.year < 1971:
            return dt

        return dt.astimezone(tz=dateutil.tz.tzlocal())
    except dateutil.parser.ParserError:
        logger.warning(
            f"{value} cannot be converted to a date-time. Returning value as is."
        )
        return value


def convert_simple_type(value: Any, json_definition: dict) -> Any:
    """
    :param value: Can be of any JSON type except list or dict.
    :param json_definition: OpenAPI definition of the value (format used to parse it).
    """
    if isinstance(value, str):
        field_format = json_definition.get("format") if json_definition else None
        # Sometimes it can happen that array definition is returned as a single element
        if not field_format and "items" in json_definition:
            return convert_simple_type(value, json_definition.get("items", {}))
        if field_format in ("date-time", "date"):
            value = to_date_time(value)
        else:
            # Return first 255 characters otherwise value will not be valid
            value = value[:255]
    return value


class Flattenizer:
    """
    Convert any JSON data into a Microsoft Excel 2D array.

    Store data for each row following a level index that will be flattened into a single level afterwards.
    """

    def __init__(
        self, all_responses: dict, status_code: int, json_definitions: dict | None
    ):
        # { level_index -> column_index }
        self.__indexes_per_level: dict[int, int] = {}
        # { level_index: [header1, header2] }
        self.__headers_per_level: dict[int, list] = {}
        # [ { level_index -> [value1, value2] } ]
        self.__values_per_level: list[dict[int, list[Any]]] = []
        self.__headers_row = []
        self.__values_rows = []
        json_response = response(status_code, all_responses)
        self.schema = (
            json_response.get("schema", json_response) if json_response else {}
        )
        self.json_definitions = (
            json_definitions if json_definitions is not None and self.schema else {}
        )

    def _reset(self):
        self.__indexes_per_level = {}
        self.__headers_per_level = {}
        self.__values_per_level = []
        self.__headers_row = []
        self.__values_rows = []

    def _extract_values_and_level(self, data: Any):
        self._reset()
        self._set_values_per_level(
            row=0,
            level=0,
            header="",
            value=data,
            column_index=0,
            json_definition=self.schema,
        )

    def _set_values_per_level(
        self,
        row: int,
        level: int,
        header: Any,
        value: Any,
        column_index: int,
        json_definition,
    ):
        # Because 0 or False are evaluated to False in python, this condition cannot be smaller
        if value is None or value == [] or value == {}:
            self._add_level_headers(level, header)
            self._level_values(row, level).append("")
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
                self._add_level_headers(level, header)
                self._level_values(row, level).append(
                    convert_simple_type(value, json_definition)
                )

    def _level_values(self, row: int, level: int) -> list[Any]:
        if row >= len(self.__values_per_level):
            self.__values_per_level.append({})
        return self.__values_per_level[row].setdefault(level, [])

    def _add_level_headers(self, level: int, header: Any):
        headers = self.__headers_per_level.setdefault(level, [])
        if header not in headers:
            headers.append(header)

    def _set_values_per_level_for_dict(
        self, row: int, level: int, values: dict, column_index: int, json_definition
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

        for header, value in values.items():
            self._set_values_per_level(
                row,
                level,
                header,
                value,
                column_index=column_index + 1,
                json_definition=properties.get(header, {}),
            )

    def _set_values_per_level_for_list(
        self,
        row: int,
        level: int,
        header: Any,
        values: list,
        column_index: int,
        json_definition,
    ):
        """
        Each item of a list corresponds to a row.
        The first item belongs to the current row.
        A list corresponds to a nested level.
        """

        if header:
            # In order to avoid losing header in case this list has one, add a column without value
            self._add_level_headers(level, header)
            self._level_values(row, level).append("")
            level += 1

            # This new level should be displayed next to the list column.
            if level not in self.__indexes_per_level:
                self.__indexes_per_level[level] = column_index
            column_index += 1

        json_definition = json_definition.get("items", {})

        # Iterate through the list
        # Create and Update all required rows for the first list value
        self._set_values_per_level(
            row,
            level,
            header,
            value=values[0],
            column_index=column_index,
            json_definition=json_definition,
        )

        # Create and Update all required rows for the other list values
        # As other rows might have been created, always recompute the actual row number
        new_row = len(self.__values_per_level) - 1
        for value in values[1:]:
            new_row += 1

            # Clone first row until current level
            new_row_levels = {
                previous_level: self.__values_per_level[row][previous_level]
                for previous_level in range(0, level)
            }
            if new_row == len(self.__values_per_level):
                self.__values_per_level.append(new_row_levels)
            else:
                self.__values_per_level[new_row].update(new_row_levels)

            self._set_values_per_level(
                row=new_row,
                level=level,
                header=header,
                value=value,
                column_index=column_index,
                json_definition=json_definition,
            )

    def to_list(self, data: Any):
        logger.debug("Converting response to list...")
        self._extract_values_and_level(data)

        # Add blanks to Rows shorter than others
        for level in self.__headers_per_level.keys():
            for row in self.__values_per_level:
                if level not in row:
                    row[level] = [""] * len(self.__headers_per_level[level])

        # Flatten Header
        for level, headers in self.__headers_per_level.items():
            if level in self.__indexes_per_level:
                related_to_index = self.__indexes_per_level[level] + 1
                self.__headers_row[related_to_index:related_to_index] = headers
            else:
                self.__headers_row.extend(headers)

        # Flatten Rows
        for row in self.__values_per_level:
            flatten_row = []
            self.__values_rows.append(flatten_row)
            for level, values in row.items():
                if level in self.__indexes_per_level:
                    related_to_index = self.__indexes_per_level[level] + 1
                    flatten_row[related_to_index:related_to_index] = values
                else:
                    flatten_row.extend(values)

        # Append headers as first row
        if self.__headers_row and self.__headers_row != [""]:
            self.__values_rows.insert(0, self.__headers_row)

        logger.debug(
            f"Response converted to list of {len(self.__values_rows)} elements."
        )
        return self.__values_rows


def response(status_code: int, responses: dict):
    if str(status_code) in responses:
        return responses[str(status_code)]
    return responses.get("default")
