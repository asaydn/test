import pandas as pd
data = pd.ExcelFile('https://github.com/adelnehme/python-for-excel-users-webinar/blob/master/sales_data_dirty.xlsx?raw=true')
print(data.sheet_names)
