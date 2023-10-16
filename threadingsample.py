import threading
from queue import Queue
import pandas as pd
from dateutil.relativedelta import relativedelta

month_yr = pd.date_range(start='2021-01-01',end = pd.datetime.today(),freq = 'MS')
month_yr = [str(date.strftime('%b %y')).upper() for date in month_yr]
fname = f'{FILENAME}.xlsx'
file_name = pd.ExcelFile(fname)
sheet_list = file_name.sheet_names
sheet_list = [sheet for sheet in sheet_list if (sheet.upper()) in month_yr]
print(sheet_list)

def read_excel_sheets(file_name,sheet):
    df = pd.read_excel(file_name,sheet)
    print(df.shape)
    print(f'now doing {sheet} {file_name}')
    print(df.columns)
    df = df.filter(regex='(?i)^(?!NaN).+', axis=1)
    df['source'] = file_name
    df = df.dropna(axis=1, how='all')
    return df
  
threads=list()
que = Queue()          
frame = list()
for index,sheet in enumerate(sheet_list):
    x = threading.Thread(target=lambda q, arg1,arg2: q.put(read_excel_sheets(arg1,arg2)), args=(que,file_name,sheet))
    threads.append(x)
    x.start()
for thread in threads:
    thread.join()
    result = que.get()
    frame.append(result)    
    print("thread starting")

df = pd.concat(frame)
target_path = TARGET_PATH
df.to_parquet(target_path) 
  
