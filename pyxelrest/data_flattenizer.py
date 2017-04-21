import logging

class Flattenizer:
    def __init__(self):
        self.__values_per_level = {}
        self.__indexes_per_level = {}
        self.__header_per_level = {}
        self.__all_rows = []
        self.__flatten_header = []
        self.__all_flatten_rows = []

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
        self._set_values_per_level(0, 0, '', data, 0)

    def _set_values_per_level(self, row, level, header, value, column_index):
        # Because "0" or "False" are considered as "not value", this condition cannot be smaller
        if value is None or value == [] or value == {}:
            self._set_value_on_level(row, level, header, value='')
        else:
            if isinstance(value, dict):
                self._set_values_per_level_for_dict(row, level, value, column_index)
            elif isinstance(value, list):
                self._set_values_per_level_for_list(row, level, header, value, column_index)
            else:
                self._set_value_on_level(row, level, header, value)

    def _set_value_on_level(self, row, level, header, value):
        self._init_values_per_level(row, level)
        self.__values_per_level[row][level].append({'header': header, 'value': value})

    def _set_values_per_level_for_dict(self, row, level, dict_value, column_index):
        """
        For a dict, each value is set on the current row and level.
        """
        for dict_key in dict_value.keys():
            self._set_values_per_level(row, level, header=dict_key, value=dict_value[dict_key],
                                       column_index=column_index + 1)

    def _set_values_per_level_for_list(self, row, level, header, list_values, column_index):
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
        self.__values_per_level[row][level].append({'header': header, 'value': ''})

        # Iterate through the list
        # Create and Update all required rows for the first list value
        self._set_values_per_level(row, level + 1, header, list_values[0], column_index + 1)

        # Create and Update all required rows for the other list values
        # As other rows might have been created, always recompute the actual row number
        new_row = len(self.__values_per_level) - 1
        for list_value in list_values[1:]:
            new_row += 1
            # Clone first row until current level
            for previous_level in range(0, level + 1):
                self._init_values_per_level(new_row, previous_level)
                self.__values_per_level[new_row][previous_level] = self.__values_per_level[row][previous_level]
            self._set_values_per_level(new_row, level + 1, header, list_value, column_index + 1)

    def to_list(self, data):
        """
        Return data formatted as a valid Excel return.
        
        :param data: JSON formatted data
        :return: Array (of Array) of primitive typed fields
        """
        logging.debug('Converting data to list...')
        self._extract_values_and_level(data)
        # Extract Header and Rows
        for row in self.__values_per_level.values():
            row_values_per_level = {}
            self.__all_rows.append(row_values_per_level)
            for level in row.keys():
                level_values = row[level]
                row_values_per_level[level] = [level_value['value'] for level_value in level_values]
                if level not in self.__header_per_level:
                    self.__header_per_level[level] = [level_value['header'] for level_value in level_values]
        # Add blanks to Rows shorter than others
        for level in self.__header_per_level.keys():
            for row in self.__all_rows:
                if level not in row:
                    row[level] = ['' for header_value in self.__header_per_level[level]]
        # Flatten Header
        for level in self.__header_per_level.keys():
            if level in self.__indexes_per_level:
                related_to_index = self.__indexes_per_level[level] + 1
                self.__flatten_header[related_to_index:related_to_index] = self.__header_per_level[level]
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
        if not self.__flatten_header[0]:
            self.__flatten_header = self.__flatten_header[1:]
            self.__all_flatten_rows = [flatten_row[1:] for flatten_row in self.__all_flatten_rows]
        if not self.__flatten_header or self.__flatten_header == ['']:
            logging.debug('Data converted to a flat list without header.')
            return self.__all_flatten_rows if self.__all_flatten_rows and self.__all_flatten_rows != [[]] else ['']
        flatten_data = [self.__flatten_header]
        flatten_data.extend(self.__all_flatten_rows)
        logging.debug('Data converted to a flat list.')
        return flatten_data


class Flattenizer2:
    def __init__(self, definitions):
        self.__rows = []
        self.__definitions = definitions[0]
        self.__object_definition_key = definitions[1]
        # This variable is here to fasten flattening as it is not required most of the time
        self.__should_flatten = requires_flatten(definitions[0])

    def to_list(self, data):
        self._fill_rows(data)
        return self.__rows

    def _fill_rows(self, data):
        if isinstance(data, dict):
            if self.__should_flatten:
                self._convert_dict_to_flatten_rows(data)
            else:
                self._convert_dict_to_2_rows(data)
        elif isinstance(data, list):
            if data and isinstance(data[0], dict):
                if self.__should_flatten:
                    self._convert_list_of_dicts_to_flatten_rows(data)
                else:
                    self._convert_list_of_dicts_to_rows(data)
            else:
                self._convert_list_to_rows(data)
        else:
            self.__rows.append(data)

    def _convert_dict_to_2_rows(self, unsorted_dictionary):
        header_row = self.header_row_without_flatten()
        self.__rows.append(header_row)
        self.__rows.extend(convert_dict_to_rows(header_row, unsorted_dictionary))

    def _object_to_columns(self, list_or_dict, definition_reference, columns, prefix):
        if isinstance(list_or_dict, list):
            for dictionary in list_or_dict:
                self._dictionary_to_columns(dictionary, definition_reference, columns, prefix)
        else:
            self._dictionary_to_columns(list_or_dict, definition_reference, columns, prefix)

    def _dictionary_to_columns(self, dictionary, definition_reference, columns, prefix):
        object_definition = self.__definitions[definition_reference]

        filled_columns = []
        for property_name in dictionary.keys():
            column_name = self._column_name(prefix, property_name)
            value = dictionary[property_name]
            property_reference = object_definition[property_name]
            if property_reference:
                self._object_to_columns(value, property_reference, columns, column_name)
            else:
                column = columns.setdefault(column_name, ['' for i in range(self._nb_value_rows(columns) - 1)])
                self._fill_previous_columns(columns, column)
                column.append(value)
                filled_columns.append(column_name)

        # TODO Ensure that all unfilled columns are filled with ''
        # for column_name, column_values in columns.items():
        #     if column_name not in filled_columns:
        #         column_values.append('')

    def _column_name(self, prefix, property_name):
        return prefix + ' / ' + property_name if prefix else property_name

    def _fill_previous_columns(self, columns, column):
        column_previous_length = len(column)
        # Fill previous columns if needed
        for column_values in columns.values():
            # Only run through previous columns
            if column_values is column:
                break
            # As new column length will be incremented by one (new value to be added)
            if len(column_values) == column_previous_length:
                column_values.append('')

    def _order_columns(self, definition_reference, columns):
        # TODO Order Columns
        # index_by_column = {}
        # current_index = 0
        # for property_name in object_definition.keys():
        #     property_reference = object_definition[property_name]
        #     if property_reference:
        #         pass  # TODO Handle imbricated levels
        #     else:
        #         index_by_column[property_name] = current_index
        #         current_index += 1
        pass

    def _nb_value_rows(self, columns):
        # Counting the number of rows in first column is enough as they should be equals
        for column in columns.values():
            return len(column)
        return 0

    def _columns_to_rows(self, columns):
        # Initialize rows (add 1 header row)
        self.__rows = [[] for index in range(self._nb_value_rows(columns) + 1)]
        # Convert columns to rows
        for column_name in columns:
            # Header row
            row_index = 0
            self.__rows[row_index].append(column_name)
            # Values rows
            for column_value in columns[column_name]:
                row_index += 1
                self.__rows[row_index].append(column_value)

    def _convert_dict_to_flatten_rows(self, unsorted_dictionary):
        columns = {}

        self._object_to_columns(unsorted_dictionary, self.__object_definition_key, columns, '')

        self._order_columns(self.__object_definition_key, columns)
        self._columns_to_rows(columns)

    def _convert_list_of_dicts_to_rows(self, dictionaries_list):
        header_row = self.header_row_without_flatten()
        self.__rows.append(header_row)
        for unsorted_dictionary in dictionaries_list:
            self.__rows.extend(convert_dict_to_rows(header_row, unsorted_dictionary))

    def _convert_list_of_dicts_to_flatten_rows(self, dictionaries_list):
        columns = {}

        for unsorted_dictionary in dictionaries_list:
            self._object_to_columns(unsorted_dictionary, self.__object_definition_key, columns, '')

        self._order_columns(self.__object_definition_key, columns)
        self._columns_to_rows(columns)

    def header_row_without_flatten(self):
        if not self.__definitions:
            raise Exception('No definition found to guess header.')
        # There should be only one definition if there is no flatten
        for definition in self.__definitions.values():
            return list(definition.keys())

    def _convert_list_to_rows(self, values_list):
        self.__rows.extend(values_list)


def convert_dict_to_rows(ordered_header, dictionary):
    # Sort dictionary according to keys (create a list of tuples)
    sorted_dict = sorted(dictionary.items(), key=lambda entry: ordered_header.index(entry[0]))
    # Create a list of values according to the previously created list of tuples
    rows = [[]]
    for entry in sorted_dict:
        value = entry[1]
        if isinstance(value, list) and value:
            for i in range(len(rows), len(value)):
                rows.append(rows[0])
            index = 0
            for list_value in value:
                rows[index].append(to_cell(list_value))
                index += 1
        else:
            for row in rows:
                row.append(to_cell(value))
    return rows


def to_cell(value):
    if value is None or value == {} or value == []:
        return ''
    return value


def requires_flatten(definitions):
    if not definitions:
        return False
    # If there is more than one object definition then there is imbricated levels
    if len(definitions) > 1:
        return True
    # Also check for recursive definitions
    for definition in definitions.values():
        for inner_reference in definition.values():
            if inner_reference:
                return True
