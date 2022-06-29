

import pingouin as pi 
import pandas as pd



 csv_file = "C:/users/aio55/document/weight_height.csv"
 df_from_csv = pd.read_csv
df = pd.read_csv('C:/users/aio55/document/weight_height.csv') 
df_from_csv.info()
print('%i people and %x columns' % df.shape) 
df.head()
pi.corr(x=df['Height'], y=df['Weight'])
