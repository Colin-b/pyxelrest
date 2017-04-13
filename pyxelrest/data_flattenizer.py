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
        self.__definitions = definitions
        self.__should_flatten = requires_flatten(definitions)

    def to_list(self, data):
        self._fill_rows(data)
        return self.__rows

    def _fill_rows(self, data):
        if self.__should_flatten:
            pass  # TODO Handle flatenning
        else:
            self._fill_rows_without_flatten(data)

    def _fill_rows_without_flatten(self, data):
        if isinstance(data, dict):
            self._convert_dict_to_2_rows(data)
        elif isinstance(data, list):
            if data and isinstance(data[0], dict):
                self._convert_list_of_dicts_to_rows(data)
            else:
                self._convert_list_to_rows(data)
        else:
            self.__rows.append(data)

    def _convert_dict_to_2_rows(self, unsorted_dictionary):
        header_row = list(self.__definitions.keys())
        self.__rows.append(header_row)
        self.__rows.append(convert_dict_to_row(header_row, unsorted_dictionary))

    def _convert_list_of_dicts_to_rows(self, dictionaries_list):
        header_row = list(self.__definitions.keys())
        self.__rows.append(header_row)
        for unsorted_dictionary in dictionaries_list:
            self.__rows.append(convert_dict_to_row(header_row, unsorted_dictionary))

    def _convert_list_to_rows(self, values_list):
        self.__rows.extend(values_list)


def convert_dict_to_row(ordered_header, dictionary):
    # Sort dictionary according to keys (create a list of tuples)
    sorted_dict = sorted(dictionary.items(), key=lambda entry: ordered_header.index(entry[0]))
    # Create a list of values according to the previously created list of tuples
    return [to_cell(entry[1]) for entry in sorted_dict]


def to_cell(value):
    if value is None or value == {} or value == []:
        return ''
    return value


def requires_flatten(definition):
    for reference_to_another_definition in definition.values():
        if reference_to_another_definition:
            return True
