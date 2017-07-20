import os,glob
import csv
dir_path = os.path.dirname(os.path.realpath(__file__))
print dir_path
os.chdir(dir_path)
for files in glob.glob("*.txt"):
    print files
    if files!='csv_question.txt':
        txt_file_object=open(files,'r')
        for file_op in txt_file_object:
            print file_op
            if file_op=="MEASURE:":
                print file_op
        
            
            
    
