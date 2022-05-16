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
    df = pd.read_excel(file_name,sheet_name = sheet)
    print(f'reading file {file_name} {sheet}')
    if sheet.upper() in month_yr_1:
        expiration_date = pd.to_datetime(sheet.upper(), format = "%b %y").replace(day=21)
    elif sheet.upper() in month_yr_2:
        expiration_date = pd.to_datetime(sheet.upper(), format = "%b%y").replace(day=21)
    elif sheet.upper() in month_yr_3:
        expiration_date = pd.to_datetime(sheet.upper(), format = "%b %Y").replace(day=21)
    week_start = expiration_date  + relativedelta(months=-1)
    week_start = week_start.replace(day=20)
    df['effective_date'] = week_start
    df['expiration_date'] = expiration_date
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
   
  
