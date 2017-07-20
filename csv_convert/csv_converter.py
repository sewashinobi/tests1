# This code converts the text file to .csv file in the required format
import re
from collections import OrderedDict
import csv
with open('csv_input_1.txt', 'r') as f:
    text_read = f.read()
processed_text = re.findall('MEASURE:([\w\W]*)', text_read, re.IGNORECASE)
data = re.findall('([\w]+)\s*:\s*([-+\d.]+)', processed_text[0], re.IGNORECASE)
data = map(lambda x: [x[0], eval(x[1])], data)

data_dict = OrderedDict()
for i in xrange(len(data)):
    if data[i][0].upper() not in data_dict.keys():
        data_dict[data[i][0].upper()] = [data[i][1]]
    else:
        data_dict[data[i][0].upper()].append(data[i][1])

data_rows = map(list, zip(*data_dict.values()))
heading_row = []
heading_row.append(data_dict.keys())
heading_row.extend(data_rows)

with open('csv_output_1_Shreyas.csv', 'wb') as csvfile:
    csv_data = csv.writer(csvfile, delimiter=',')
    for j in heading_row:
        csv_data.writerow(j)