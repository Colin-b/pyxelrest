class Flattenizer:
    def __init__(self):
        self.values_per_level = {}
        self.indexes_per_level = {}
        self.header_per_level = {}
        self.all_rows = []
        self.flatten_header = []
        self.all_flatten_rows = []

    def reset(self):
        self.values_per_level = {}
        self.indexes_per_level = {}
        self.header_per_level = {}
        self.all_rows = []
        self.flatten_header = []
        self.all_flatten_rows = []

    def init_values_per_level(self, row, level):
        if not self.values_per_level.get(row):
            self.values_per_level[row] = {}
        if not self.values_per_level[row].get(level):
            self.values_per_level[row][level] = []

    def extract_values_and_level(self, data):
        self.reset()
        self.set_values_per_level(0, 0, '', data, 0)

    def set_values_per_level(self, row, level, header, value, column_index):
        if value:
            if isinstance(value, dict):
                self.set_values_per_level_for_dict(row, level, value, column_index)
            elif isinstance(value, list):
                self.set_values_per_level_for_list(row, level, header, value, column_index)
            else:
                self.set_value_on_level(row, level, header, value)
        else:
            self.set_value_on_level(row, level, header, value='')

    def set_value_on_level(self, row, level, header, value):
        self.init_values_per_level(row, level)
        self.values_per_level[row][level].append({'header': header, 'value': value})

    def set_values_per_level_for_dict(self, row, level, dict_value, column_index):
        """
        For a dict, each value is set on the current row and level.
        """
        for dict_key in dict_value.keys():
            self.set_values_per_level(row, level, header=dict_key, value=dict_value[dict_key], column_index=column_index + 1)

    def set_values_per_level_for_list(self, row, level, header, list_values, column_index):
        """
        Each item of a list corresponds to a row.
        The first item belongs to the current row.
        A list corresponds to a nested level.
        """
        # This new level should be displayed next to the list column.
        if level + 1 not in self.indexes_per_level:
            self.indexes_per_level[level + 1] = column_index

        # In order to avoid losing key in case this list has a key, add a column without value
        self.init_values_per_level(row, level)
        self.values_per_level[row][level].append({'header': header, 'value': ''})

        # Iterate through the list
        # Create and Update all required rows for the first list value
        self.set_values_per_level(row, level + 1, header, list_values[0], column_index + 1)

        # Create and Update all required rows for the other list values
        # As other rows might have been created, always recompute the actual row number
        new_row = len(self.values_per_level) - 1
        for list_value in list_values[1:]:
            new_row += 1
            # Clone first row until current level
            for previous_level in range(0, level + 1):
                self.init_values_per_level(new_row, previous_level)
                self.values_per_level[new_row][previous_level] = self.values_per_level[row][previous_level]
            self.set_values_per_level(new_row, level + 1, header, list_value, column_index + 1)

    def to_list(self, data):
        self.extract_values_and_level(data)
        # Extract Header and Rows
        for row in self.values_per_level.values():
            row_values_per_level = {}
            self.all_rows.append(row_values_per_level)
            for level in row.keys():
                level_values = row[level]
                row_values_per_level[level] = [level_value['value'] for level_value in level_values]
                if level not in self.header_per_level:
                    self.header_per_level[level] = [level_value['header'] for level_value in level_values]
        # Add blanks to Rows shorter than others
        for level in self.header_per_level.keys():
            for row in self.all_rows:
                if level not in row:
                    row[level] = ['' for header_value in self.header_per_level[level]]
        # Flatten Header
        for level in self.header_per_level.keys():
            if level in self.indexes_per_level:
                related_to_index = self.indexes_per_level[level] + 1
                self.flatten_header[related_to_index:related_to_index] = self.header_per_level[level]
            else:
                self.flatten_header.extend(self.header_per_level[level])
        # Flatten Rows
        for row in self.all_rows:
            flatten_row = []
            self.all_flatten_rows.append(flatten_row)
            for level in row.keys():
                if level in self.indexes_per_level:
                    related_to_index = self.indexes_per_level[level] + 1
                    flatten_row[related_to_index:related_to_index] = row[level]
                else:
                    flatten_row.extend(row[level])
        # Remove unnecessary columns that may appear for lists TODO Avoid adding this in the first place
        if not self.flatten_header[0]:
            self.flatten_header = self.flatten_header[1:]
            self.all_flatten_rows = [flatten_row[1:] for flatten_row in self.all_flatten_rows]
        if not self.flatten_header or self.flatten_header == ['']:
            return self.all_flatten_rows if self.all_flatten_rows and self.all_flatten_rows != [[]] else ['']
        flatten_data = [self.flatten_header]
        flatten_data.extend(self.all_flatten_rows)
        return flatten_data
