import datetime
import logging
from typing import Union

import dateutil.tz
import dateutil.parser

logger = logging.getLogger(__name__)


def append_prefix(prefix: str, values_list: list) -> list:
    """
    Append the prefix to each item in the values_list.
    This method is used to update header for inner fields.
    """
    if prefix:
        return [f"{prefix} / {value}" if value else prefix for value in values_list]
    return values_list


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


class RowsMerger:
    def __init__(self):
        self.header = None
        self.rows = None

    def merge(self, new_header, new_merging_data):
        """
        Update rows with this new data.

        :param new_data: Either a value, a list of values or a list of list of values
        """
        if new_merging_data.rows is None:
            return

        new_header = new_header if new_header else new_merging_data.header

        if self.rows is None:
            self.header = new_header if new_header else new_merging_data.header
            self.rows = new_merging_data.rows
        elif isinstance(new_merging_data.rows, list):
            self.merge_list(new_header, new_merging_data.rows)
        else:
            self.merge_single_value(new_header, new_merging_data.rows)

    def merge_new_list_item(self, list_name, new_merging_data):
        """
        Current rows needs to be duplicated for each call and this new data should be appended.
        
        :param new_data: Either a value, a list of values or a list of list of values
        """
        if new_merging_data.rows is None:
            return

        if self.rows is None:
            self.rows = []

        if isinstance(new_merging_data.rows, list):
            new_header = append_prefix(list_name, new_merging_data.header)
            new_columns = self.get_new_columns(new_header)
            missing_columns = self.get_missing_columns(new_header)
            self.merge_header(new_header, new_columns, missing_columns)

            for row in self.rows:
                self.add_empty_columns(row, new_columns)

            if isinstance(new_merging_data.rows[0], list):
                for converted_list in new_merging_data.rows:
                    self.add_empty_columns(converted_list, missing_columns)
                    self.rows.append(converted_list)
            else:
                self.add_empty_columns(new_merging_data.rows, missing_columns)
                self.rows.append(new_merging_data.rows)
        else:
            self.header = (
                append_prefix(list_name, [new_merging_data.header])
                if new_merging_data.header
                else None
            )
            self.rows.append([new_merging_data.rows])

    def merge_header(self, new_header, new_columns, missing_columns):
        if new_columns and missing_columns:
            # TODO Add new columns at the right place instead of the end
            raise Exception("Addition of new columns to header is not handled properly")
        elif new_columns or not self.header:
            self.header = new_header

    def get_new_columns(self, new_header):
        if self.header:
            return [
                column_name
                for column_name in new_header
                if column_name not in self.header
            ]
        return []

    def get_missing_columns(self, new_header):
        if self.header:
            return [
                column_name
                for column_name in self.header
                if column_name not in new_header
            ]
        return []

    def add_empty_columns(self, row, missing_columns):
        for column_name in missing_columns:
            row.insert(self.header.index(column_name), "")

    def merge_list(self, new_header, new_list):
        """
        Merge this list to the rows.

        :param new_list: Either a list of values or a list of list of values
        """
        if isinstance(self.rows, list):
            self.merge_list_to_list(new_header, new_list)
        else:
            self.append_list_to_value(new_header, new_list)

    def merge_list_to_list(self, new_header, new_list):
        if not isinstance(self.rows[0], list):
            if isinstance(new_list[0], list):
                self.append_list_of_list_to_list(new_header, new_list)
            else:
                self.append_list_to_list(new_header, new_list)
        else:
            if isinstance(new_list[0], list):
                self.append_list_of_list_to_list_of_list(new_header, new_list)
            else:
                self.append_list_to_list_of_list(new_header, new_list)

    def append_list_of_list_to_list(self, new_header, new_list_of_list):
        self.header.extend(new_header)
        new_rows = []
        for new_list in new_list_of_list:
            new_row = list(self.rows)
            new_row.extend(new_list)
            new_rows.append(new_row)
        self.rows = new_rows

    def append_list_to_list(self, new_header, new_list):
        raise Exception(
            f"Merging two lists is not handled for now. {new_list} merged to {self.rows}"
        )

    def append_list_of_list_to_list_of_list(self, new_header, new_list_of_list):
        self.header.extend(new_header)
        new_rows = []
        for row in self.rows:
            for new_list in new_list_of_list:
                new_row = list(row)
                new_row.extend(new_list)
                new_rows.append(new_row)
        self.rows = new_rows

    def append_list_to_list_of_list(self, new_header, new_list):
        raise Exception(
            f"Merging two lists is not handled for now. {new_list} merged to {self.rows}"
        )

    def append_list_to_value(self, new_header, new_list):
        """
        Rows is currently containing a single value.
        Append a list of list or a list to this value.

        :param new_list: Either a list or a list of list
        """
        self.header = [self.header]
        self.header.extend(new_header)

        if isinstance(new_list[0], list):
            for new_inner_list in new_list:
                new_inner_list.insert(0, self.rows)
        else:
            new_list.insert(0, self.rows)
        self.rows = new_list

    def merge_single_value(self, value_name, value):
        """
        Append a value to rows.
        Rows is Either a value, a list of values or a list of list of values
        
        :param value_name: Header name of the value
        :param value: Not a list
        """
        # New data to be appended to every list
        if isinstance(self.rows, list):
            self.header.append(value_name)
            if isinstance(self.rows[0], list):
                for previous_list in self.rows:
                    previous_list.append(value)
            else:
                self.rows.append(value)
        else:
            self.header = [self.header, value_name]
            self.rows = [self.rows, value]

    def header_and_rows(self):
        if self.header:
            header_and_rows = (
                [self.header] if isinstance(self.header, list) else [[self.header]]
            )
            if isinstance(self.rows, list):
                if isinstance(self.rows[0], list):
                    header_and_rows.extend(self.rows)
                else:
                    header_and_rows.append(self.rows)
            else:
                header_and_rows.append([self.rows])
            return header_and_rows
        if self.rows is None:
            return [""]
        if isinstance(self.rows, list):
            return self.rows
        return [self.rows]


all_definitions = {}


class Field:
    def __init__(self, json_definition: dict, json_definitions: dict):
        self.description = json_definition.get("description")
        self.type = json_definition.get("type")
        self.array_field = (
            Field(json_definition.get("items"), json_definitions)
            if self.type == "array"
            else None
        )
        self.format = json_definition.get("format")
        self.ref = json_definition.get("$ref")
        if self.ref and self.ref not in all_definitions:
            all_definitions[self.ref] = Definition(self.ref, json_definitions)
            all_definitions[self.ref].init_fields(json_definitions)
        self.definition = all_definitions.get(self.ref)

    def convert(self, name, value):
        if self.definition:
            return self.definition.convert(value)
        return self.convert_to_type(name, value)

    def convert_to_type(self, name, value):
        if self.type == "array":
            return self.convert_array(name, value)
        return self.convert_simple_type(value)

    def convert_array(self, name, value):
        # An empty list should not add any extra information
        if value is None or value == []:
            return RowsMerger()
        if isinstance(value, dict):
            raise Exception(f"{self.description} is supposed to be a list: {value}")

        merger = RowsMerger()

        # Allow lists to be a single value
        if not isinstance(value, list):
            merger.merge_new_list_item(name, self.array_field.convert(name, value))
        else:
            for array_item in value:
                merger.merge_new_list_item(
                    name, self.array_field.convert(name, array_item)
                )

        if merger.header is None and name is not None:
            merger.header = [name]
        return merger

    def convert_simple_type(self, value):
        merger = RowsMerger()
        if isinstance(value, str):
            if self.format == "date-time" or self.format == "date":
                value = to_date_time(value)
            else:
                # Return first 255 characters otherwise value will not be valid
                value = value[:255]
        merger.rows = value
        return merger


class DefaultField:
    """
    Used to perform deserialization of responses without schema.
    """

    def convert(self, name, value):
        if isinstance(value, dict):
            return DefaultField.convert_dict(value)
        if isinstance(value, list):
            return DefaultField.convert_list(name, value)
        return DefaultField.convert_simple_type(value)

    @staticmethod
    def convert_dict(dictionary):
        merger = RowsMerger()

        for field_name in dictionary.keys():
            field_value = dictionary.get(field_name)
            merger.merge(
                field_name if not isinstance(field_value, list) else None,
                DefaultField().convert(field_name, field_value),
            )

        return merger

    @staticmethod
    def convert_list(name, values):
        # An empty list should not add any extra information
        if not values:
            return RowsMerger()

        merger = RowsMerger()
        for value in values:
            merger.merge_new_list_item(name, DefaultField().convert(name, value))
        if merger.header is None and name is not None:
            merger.header = [name]
        return merger

    @staticmethod
    def convert_simple_type(value):
        merger = RowsMerger()
        if isinstance(value, str):
            # Return first 255 characters otherwise value will not be valid
            value = value[:255]
        merger.rows = value
        return merger


def extract_fields(json_properties: dict, json_definitions: dict) -> dict:
    fields = {}
    for reference_name in json_properties.keys():
        json_field = json_properties[reference_name]
        if reference_name not in fields:
            fields[reference_name] = Field(json_field, json_definitions)
    return fields


class Definition:
    def __init__(self, definition_reference: str, json_definitions: dict):
        """
        Creates a new definition (usually an object).
        
        :param definition_reference: Always prefixed by #/definitions/
        :param json_definitions: All definitions (JSON dictionary)
        """
        definition_reference = definition_reference[len("#/definitions/") :]
        if definition_reference not in json_definitions:
            raise Exception(
                f'"{definition_reference}" is not within {json_definitions}'
            )
        self.json_definition = json_definitions[definition_reference]
        self.type = self.json_definition.get("type")
        self.title = self.json_definition.get("title")
        self.fields = {}

    def init_fields(self, json_definitions: dict):
        self.fields = extract_fields(
            self.json_definition.get("properties"), json_definitions
        )

    def convert(self, data: dict) -> RowsMerger:
        if not isinstance(data, dict):
            raise Exception(f"{self.title} is supposed to be a dict: {data}")

        merger = RowsMerger()

        for field_name in self.fields.keys():
            field_value = data.get(field_name)
            field = self.fields[field_name]
            merger.merge(
                field_name if not field.array_field else None,
                field.convert(field_name, field_value),
            )

        undefined_fields = [
            field_name
            for field_name in data.keys()
            if field_name not in self.fields and field_name[:6].lower() != "x-pxl-"
        ]
        if undefined_fields:
            raise Exception(
                f"The following fields are not part of the definition: {undefined_fields}"
            )

        return merger


class Response:
    def __init__(self, all_responses: dict, status_code: int, json_definitions: dict):
        json_response = response(status_code, all_responses)
        schema = json_response.get("schema") if json_response else None
        self.field = (
            Field(schema, json_definitions if json_definitions is not None else {})
            if schema
            else DefaultField()
        )

    def rows(self, data):
        logger.debug("Converting response to list...")
        rows = self.field.convert(None, data).header_and_rows()
        logger.debug(f"Response converted to list of {len(rows)} elements.")
        return rows


def response(status_code: int, responses: dict):
    if str(status_code) in responses:
        return responses[str(status_code)]
    return responses.get("default")
