# Take input file names
from typing import Dict, Union

input_file_name = input('Input input file name')
output_file_name = input('Input output file name')

# open output file and print the header row
result_file_handle = open(output_file_name, 'w+')
result_file_handle.write('X,Y,Z,RES\n')

# falg to know when valid content starts
content_starts = False

# open input file for reading
input_file_handle = open(input_file_name, 'r')

# read the content and split on new line
content = input_file_handle.read().split('\n')
number_of_lines = len(content)

line_count = 0
new_line = {}  # type: Dict[str, Union[float, int]]

while line_count < number_of_lines-4:
    line = content[line_count].split('#')[0]
    if line.strip() == 'MEASURE:':
        content_starts = True
        line_count += 1
        continue
    if content_starts:
        if line.strip() == 'POINT:':
            new_line = {}

            # read next four lines and extract the desired values
            for i in range(1, 5):
                line_content = content[line_count + i].split(':')
                key = line_content[0].strip().lower()
                val = line_content[1].split('#')[0].strip().lower()
                new_line[key] = val

            # write the values into the output file in csv format
            result_file_handle.write('%s,%s,%s,%s\n' % (new_line['x'],
                                                        new_line['y'],
                                                        new_line['z'],
                                                        new_line['res']))
            line_count += 4
        else:
            line_count += 1
    else:
        line_count += 1

# close file objects
result_file_handle.close()
input_file_handle.close()
