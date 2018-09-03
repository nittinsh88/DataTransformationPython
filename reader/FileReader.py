'''
Created on Aug 29, 2018
D:\pythonassignmet\forecast_data-master\raw.csv

@author: nitsharm7
'''
#import csv
import pandas as pd


filePath=input("Please provide the file Path for pandas")  
#df = pd.read_csv(filePath,nrows=2)


dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv(filePath,parse_dates=['datetime'],date_parser=dateparse)
print(df[0:2])
filtered_data = df.dropna(axis='rows', how='any')
#print(filtered_data)
#print(str(df['datetime'].dt.date))
filtered_data=filtered_data.groupby([df['datetime'].dt.date]).agg({'Vancouver': 'sum','Portland':'sum','San Francisco':'sum','Seattle':'sum','Year':'min','ds':'first'})
filtered_data.to_csv('out.csv')
print('done')
