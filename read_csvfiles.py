import pandas as pd
import glob

def fun_readcsvfile():
    filename = 'C:/Users/Linuxbean/Music/leadgen_project/static/uploads/Complete MRA 16012023.csv'
    f2 = 'C:/Users/Linuxbean/Music/leadgen_project/static/uploads/Latest samples short list doctored.csv'

    for files in glob.glob(filename):
      with open(files) as filename:
          df = pd.read_csv (files)
          print(df)

    for files in glob.glob(f2):
      with open(files) as f2:
          df_trial = pd.read_csv (files)
          print(df_trial)

    return df,df_trial