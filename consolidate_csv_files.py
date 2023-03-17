from os import listdir
from os.path import isfile, join
import pandas as pd


class Consolidate_CSV():

    def __init__(self,file_path,output_path,output_file_name):

        self.file_path = file_path
        self.output_file_name = join(output_path,output_file_name)
        #List File Names from path
        file_names = [f for f in listdir(self.file_path) if isfile(join(self.file_path, f)) ]
        #Filter CSV Files from the path
        file_names = [f for in file_names if ".csv" in f.lower()]

    def read_csv(self):
        main_frame = list()
        for file in file_names:
            df = pd.read_csv(join(self.file_path,file))
            """Insert Transformation here"""
            main_frame.append(df)
        consolidated_df  = pd.concat(main_frame)
        consolidated_df.to_csv(self.output_file_name,index=False)

    
if __name__ =="__main__":
    
    file_path = FILE_PATH # DEFINE file path of the csv files
    output_path =  OUTPUT_PATH # DEFINE the file path on where to put the Consolidated file 
    output_file_name = OUTPUT_FILE_NAME #  Define the Output FileName
    x= Consolidate_CSV(file_path,output_path,output_file_name)
    x.main()

        