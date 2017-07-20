from csv import DictWriter


def clean_val(st):
    """
    Returns cleaned string which removes newline char, trailing spaces,
    and colons
    """
    st = st.strip('\n').strip('\r\n')
    st = st.split('#')[0].strip(': ')
    return st.upper()


def convert_txt_to_csv(input_path, out_path):
    """
    Params: input file path, output file path
    Returns: None

    Takes input text file path and writes the values to output file
    """
    with open(input_path) as f:
        lines = f.readlines()

        # clean all the lines
        lines = [clean_val(line) for line in lines]

        # if start index is not present , exit immediately
        try:
            start_index = lines.index('MEASURE')
        except ValueError:
            print 'Bad Input'
            exit()

        all_point_indexes = [idx for idx in xrange(len(lines))
                             if lines[idx] == 'POINT'
                             ]

        csv_values = []  # the final required list of dicts
        for p_idx in all_point_indexes:
            if p_idx > start_index:
                vals = lines[p_idx+1:p_idx+5]
                print vals
                csv_dict = {}
                for val in vals:
                    k, v = map(str.strip, val.split(':'))
                    csv_dict[k] = v
                csv_values.append(csv_dict)

    with open(out_path, 'w') as csvfile:
        fieldnames = ['X', 'Y', 'Z', 'RES']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_values:
            writer.writerow(row)


if __name__ == '__main__':
    convert_txt_to_csv('csv_input_1.txt', 'out1.csv')
    convert_txt_to_csv('csv_input_2.txt', 'out2.csv')
