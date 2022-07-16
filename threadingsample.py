import threading
from queue import Queue
import pandas as pd
from dateutil.relativedelta import relativedelta

month_yr = pd.date_range(start='2021-01-01',end = pd.datetime.today(),freq = 'MS')
month_yr_1 = [str(date.strftime('%b %y')).upper() for date in month_yr]
month_yr_2 = [str(date.strftime('%b%y')).upper() for date in month_yr]
month_yr_3 = [str(date.strftime('%b %Y')).upper() for date in month_yr]

fname = r'filename.xlsx'
file_name = pd.ExcelFile(fname)
sheet_list = file_name.sheet_names
sheet_list = [sheet for sheet in sheet_list if (sheet.upper()) in month_yr_1 or  (sheet.upper()) in month_yr_2 or  (sheet.upper()) in month_yr_3]
print(sheet_list)

def read_excel_sheets(file_name,sheet):
    df = pd.read_excel(file_name,sheet)
    print(df.shape)
    print(f'now doing {sheet}{file_name}')
    print(df.columns)
    col_ = list(df.columns[:5])
    col_.remove(col_[0])
    col_=col_[0]
    if 'Unnamed' in col_:
        df.columns = df.iloc[0]
        df = df.drop(df.index[[0]])
    df = df.filter(regex='(?i)^(?!NaN).+', axis=1)
    df['source'] = file_name
    df = df.dropna(axis=1, how='all')
    new_col = list(df.columns)
    new_col = [c for c in new_col if 'SAMPLE' in str(c)]
    if 'SAMPLE' in new_col:
        df = df.rename(columns ={'SAMPLE':'sample'})
    print(df.columns)
    return df
  
threads=list()
que = Queue()          
frame = []
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
   
  
