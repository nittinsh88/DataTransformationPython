'''
Created on Aug 31, 2018
http://127.0.0.1:5000/weatherdata?startdate=2012/10/1&enddate=2012/10/8&location=Vancouver

@author: nitsharm7
'''

import pandas as pd
from flask import Flask, redirect, url_for, request, make_response,abort
from datetime import datetime
from flask_jsonpify import jsonify

app = Flask(__name__)

filePath = "out.csv"

def getData(startDate, endDate, location):
 #dateparse = lambda x: pd.datetime.strptime(x, '%Y/%m/%d')
 df = pd.read_csv(filePath) 
 df['date'] = pd.to_datetime(df['datetime'])
 mask = ((df['date'].dt.date >= startDate.date()) & (df['date'].dt.date <= endDate.date()))
 print(df.loc[mask])
 df=df.loc[mask]
 return(df[location])
 

@app.route('/weatherdata', methods=['GET'])
def getFilteredData():
   startDate = request.args.get('startdate')
   if(startDate is not None):
          startDate = getDateFromString(startDate) 
   else:
           abort(400)  
   endDate = request.args.get('enddate') 
   if(endDate is not None):
          endDate = getDateFromString(endDate) 
   else:  
           abort(400)
   location = request.args.get('location') 
   if(location is  None):
        abort(400) 
   df = getData(startDate, endDate, location)   
   if not df.empty:
      df_list = df.values.tolist()
      JSONP_data = jsonify(df_list)
   return JSONP_data
   abort(400) 
 
 
 
@app.errorhandler(400)
def not_found(e):
  return 'data not available'  
 #return make_response("Data Not Available", 400)
  
  
def getDateFromString(argDate):
    if(argDate is not None):
        return  datetime.strptime(argDate, '%Y/%m/%d')
    else:
        return 'not a valid date'
 
@app.route('/')
def index():
   return 'Welcome to the weather data service'
 
if __name__ == '__main__':
 app.run(debug=True)
 
