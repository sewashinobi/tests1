__author__ = 'cc'
import sys
import csv

class CSVConvertor:
    '''
    class to process text file and generate CSV file equivalent
    '''


    def __init__(self,filename):
        '''

        :return:
        '''
        self.input_file_name = filename
        self.fileObj = open(self.input_file_name,'r')
        self.output_file_name = self.input_file_name.replace('input','output').replace('txt','csv')

    def process_point(self,point_list):
        '''

        :param point_list:
        :return: a dictionary representing a point
        '''
        print point_list
        point_dict = {val.split(": ")[0].rstrip():''.join(i for i in val.split(": ")[1] if i.isdigit() or i in ['.','-']) for val in point_list}
        return point_dict


    def get_all_points(self):
        '''

        :return:
        '''
        lines = self.fileObj.readlines()
        #remove lines with comments
        lines = filter(lambda x: not x.startswith("#") ,lines)

        #remove new lines and whitespace characters in beginning and end
        lines = map(lambda x: x.strip().rstrip().lower(),lines)

        index_of_measure = lines.index("measure:")
        lines = lines[index_of_measure+1::]

        points_list = []
        for i in xrange(0,len(lines),5):
            points_list.append(self.process_point(lines[i+1:i+5]))
        return points_list


    def generate_csv_file(self):
        '''

        :return:
        '''
        points = self.get_all_points()
        self.create_csv_file(points)

    def create_csv_file(self,points):
        '''

        :param points:
        :return:
        '''
        csvfile = open(self.output_file_name, 'wb')
        fieldnames = ['X', 'Y','Z','RES']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for point in points:
            print point
            writer.writerow({'X':point['x'] , 'Y': point['y'],'Z':point['z'],'RES':point['res']})
        csvfile.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Input text file name"
        sys.exit(-1)
    CSVConvertorObj = CSVConvertor(sys.argv[1])
    CSVConvertorObj.generate_csv_file()
