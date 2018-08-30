'''
Created on Aug 29, 2018
D:\pythonassignmet\forecast_data-master\raw.csv

@author: nitsharm7
'''
#import csv
import pandas as pd


filePath=input("Please provide the file Path for pandas")  
df = pd.read_csv(filePath,nrows=2)

print(df)
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv(filePath,parse_dates=['datetime'],date_parser=dateparse)
filtered_data = df.dropna(axis='rows', how='any')
print(filtered_data)
print(str(df['datetime'].dt.date))
print(filtered_data.groupby([df['datetime'].dt.date]).agg({'Vancouver': 'sum','Portland':'sum','San Francisco':'sum','Seattle':'sum','Year':'min','ds':'first'}))




'''
filePath = input("Please provide the file Path")
with open(filePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    printNumber =2
    for row in csv_reader:
        if line_count == 0:
            print(", ".join(row))
            line_count += 1
        else:
            if(printNumber >0):
                print(row)
                printNumber-=1
            line_count += 1
    print("Processed "+ str(line_count)+" lines.")
    '''