
import pandas as pd

def txt_file_to_csv(file_name):
    """ This function converts text file in specified format
    to csv file"""
    
    point_values=[]
    with open(file_name,'r') as fp:
        measure_detected =False
        point_encountered= False
        values=dict() 
        
        for line in fp:                       
            if measure_detected:
                if(line.strip().lower()) == 'point:': # discard point
                    point_encountered =True
                if(line.strip()[0]) == '#': # discard comments
                    pass
                else:
                    line_items = line.split(':')
                    point_var = line_items[0].strip()
                    point_val = line_items[1].strip()
                
                    point_val = point_val.split('#')
                    point_val = point_val[0]
                    if point_var.upper() in ['X','Y','Z','RES']:
                        values[point_var.upper()] = point_val
                
            if(line.strip().lower()) == 'measure:':
                measure_detected=True
                
            if values and len(values.keys())==4:
                point_values.append(values)
                point_encountered =False
                values=dict()
    return point_values
    
if __name__ == '__main__':
    # Enter input file name here
    file_name = 'csv_input_2.txt'
    val = txt_file_to_csv(file_name)
    
    # generate dataframe to convert to csv.
    df = pd.DataFrame(val)
    out_file_name = file_name.replace('.txt','').split('_')
    out_file_name[1]='output'
    out_file_name = "_".join(out_file_name)+'.csv'
    df.to_csv(out_file_name,columns=['X','Y','Z','RES'])
            
    
        
        
            
            
        
        
        
