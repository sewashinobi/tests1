"""
This is to convert given file to csv file
"""
import sys

MEASURE = 'MEASURE:'
POINT = 'POINT:'
X = 'X:'
Y = 'Y:'
Z = 'Z:'
RES = 'RES:'


def add_to_results(results, row):
    rec = ''
    if(X in row and Y in row and
       Z in row and RES in row):
        rec = rec + row[X] + ','
        rec = rec + row[Y] + ','
        rec = rec + row[Z] + ','
        rec = rec + row[RES]
        results.append(rec)


def convert(in_file):
    with open(in_file, 'r') as fp:
        lines = fp.readlines()
    found_measure = False
    results = []
    results.append('X,Y,Z,RES')
    row = None
    done_with_row = True
    found_point = False
    for line in lines:
        str_ = line.strip('\n').strip(' ').upper()
        if MEASURE in str_:
            found_measure = True
            found_point = False
            continue
        if found_measure:
            if POINT in str_:
                found_point = True
                done_with_row = True
                continue
            if found_point and done_with_row:
                row = {}
                done_with_row = False
            print str_
            if(str_.startswith(X) or
                    str_.startswith(Y) or
                    str_.startswith(Z) or
                    str_.startswith(RES)):
                values = str_.split(' ')
                key = values[0].strip()
                val = values[1].strip('#')
                row[key] = val
                if(len(row.keys())) == 4:
                    add_to_results(results, row)
                    done_with_row = True
                    found_point = False
    with open('output.txt', 'w') as fp2:
        for row in results:
            fp2.write(row)
            fp2.write('\n')

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print "Not enough arguments"
        sys.exit(0)
    convert(sys.argv[1])
