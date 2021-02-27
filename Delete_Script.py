
import pandas as pd
import os
import sys


'getcwd:      ', os.getcwd()
osfile, maindir =('__file__:    ', __file__)
filename = os.path.basename(sys.argv[0])
inpath = maindir.replace(filename,"Excels")
outpath = maindir.replace(filename,"BulkFile.xlsx")





def delete_excels(inpath,outpath):
    for root, dirs, files in os.walk(inpath):
        for f in files:
            path = os.path.join(root, f)
            print(path)
            excelframe = pd.read_excel(path)
            del_frame = excelframe.drop(columns=['ip_address'])
            dataframe = [del_frame]
            compactframe = pd.concat(dataframe)
            compactframe.to_excel(outpath)


delete_excels(inpath,outpath)



