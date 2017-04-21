from collections import OrderedDict


def append_prefix(prefix, values_list):
    if prefix:
        return ['{0} / {1}'.format(prefix, value) if value else prefix for value in values_list]
    return values_list


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
            self.header = append_prefix(list_name, [new_merging_data.header]) if new_merging_data.header else None
            self.rows.append([new_merging_data.rows])

    def merge_header(self, new_header, new_columns, missing_columns):
        # TODO Handle the fact that there might be new AND missing at the same time
        if new_columns and missing_columns:
            raise Exception('Merging rows that contains both new and missing columns is not handled for now.')
        if new_columns or not self.header:
            self.header = new_header

    def get_new_columns(self, new_header):
        if self.header:
            return [column_name for column_name in new_header if column_name not in self.header]
        return []

    def get_missing_columns(self, new_header):
        if self.header:
            return [column_name for column_name in self.header if column_name not in new_header]
        return []

    def add_empty_columns(self, row, missing_columns):
        for column_name in missing_columns:
            row.insert(self.header.index(column_name), '')

    def merge_list(self, new_header, new_list):
        """
        Merge this list to the rows.

        :param new_list: Either a list of values or a list of list of values
        """
        if isinstance(self.rows, list):
            raise Exception('Merging a list to a list is not handled for now.')
        self.append_list_to_value(new_header, new_list)

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

all_definitions = {}


class Field:
    def __init__(self, json_definition, json_definitions):
        self.description = json_definition.get('description')
        self.type = json_definition.get('type')
        self.array_field = Field(json_definition.get('items'), json_definitions) if self.type == 'array' else None
        self.format = json_definition.get('format')
        self.ref = json_definition.get('$ref')
        if self.ref and self.ref not in all_definitions:
            all_definitions[self.ref] = Definition(self.ref, json_definitions)
            all_definitions[self.ref].init_fields(json_definitions)
        self.definition = all_definitions.get(self.ref)

    def convert(self, name, value):
        if self.definition:
            return self.definition.convert(value)
        return self.convert_to_type(name, value)

    def convert_to_type(self, name, value):
        if self.type == 'array':
            return self.convert_array(name, value)
        return self.convert_simple_type(value)

    def convert_array(self, name, value):
        # An empty list should not add any extra information
        if value is None or value == []:
            return RowsMerger()
        if not isinstance(value, list):
            raise Exception('{0} is supposed to be a list: {1}'.format(self.description, value))

        merger = RowsMerger()
        for array_item in value:
            merger.merge_new_list_item(name, self.array_field.convert(name, array_item))
        if merger.header is None and name is not None:
            merger.header = [name]
        return merger

    def convert_simple_type(self, data):
        merger = RowsMerger()
        # TODO Handle type conversion for dates, ...
        merger.rows = data
        return merger


def extract_fields(json_properties, json_definitions):
    fields = OrderedDict()
    for reference_name in json_properties.keys():
        json_field = json_properties[reference_name]
        if reference_name not in fields:
            fields[reference_name] = Field(json_field, json_definitions)
    return fields


class Definition:
    def __init__(self, definition_reference, json_definitions):
        """
        Creates a new definition (usually an object).
        
        :param definition_reference: Always prefixed by #/definitions/
        :param json_definitions: All definitions (JSON dictionary)
        """
        definition_reference = definition_reference[len('#/definitions/'):]
        if definition_reference not in json_definitions:
            raise Exception('"{0}" is not within {1}'.format(definition_reference, json_definitions))
        self.json_definition = json_definitions[definition_reference]
        self.type = self.json_definition.get('type')
        self.title = self.json_definition.get('title')
        self.fields = {}

    def init_fields(self, json_definitions):
        self.fields = extract_fields(self.json_definition.get('properties'), json_definitions)

    def convert(self, data):
        if not isinstance(data, dict):
            raise Exception('{0} is supposed to be a dict: {1}'.format(self.title, data))

        merger = RowsMerger()

        for field_name in self.fields.keys():
            field_value = data.get(field_name)
            field = self.fields[field_name]
            merger.merge(field_name if not field.array_field else None, field.convert(field_name, field_value))

        undefined_fields = [field_name for field_name in data.keys() if field_name not in self.fields]
        if undefined_fields:
            raise Exception('The following fields are not part of the definition: {0}'.format(undefined_fields))

        return merger


class Response:
    def __init__(self, json_response, json_definitions={}):
        schema = json_response.get('schema')
        self.field = Field(schema, json_definitions) if schema else None

    def rows(self, data):
        if not self.field:
            # Return first 255 characters of the response by default
            return [str(data)[:255]]
        merger = self.field.convert(None, data)
        if merger.header:
            rows = [merger.header] if isinstance(merger.header, list) else [[merger.header]]
            if isinstance(merger.rows, list):
                if isinstance(merger.rows[0], list):
                    rows.extend(merger.rows)
                else:
                    rows.append(merger.rows)
            else:
                rows.append([merger.rows])
            return rows
        elif merger.rows is None:
            return ['']
        else:
            if isinstance(merger.rows, list):
                return merger.rows
            else:
                return [merger.rows]
