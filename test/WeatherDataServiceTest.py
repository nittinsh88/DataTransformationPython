'''
Created on Sep 2, 2018

@author: nitsharm7
'''
import unittest
import service.WeatherDataService as wds
from datetime import datetime
import pandas as pd
from pandas.util.testing import assert_frame_equal,assert_series_equal





class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def testGetDateFromString(self):
        date = datetime.strptime('2012/10/1', '%Y/%m/%d')
        dateReturn = wds.getDateFromString('2012/10/1')
        self.assertEqual(date, dateReturn)
        
       
        
    def testgetData(self):
        df = pd.read_csv('out.csv') 
        actual=wds.getData(wds.getDateFromString('2012/10/1'), wds.getDateFromString('2012/10/2'), 'Vancouver') 
        print(df['Vancouver'])   
        print(actual)       
        assert_series_equal(df['Vancouver'], actual)
        
        
            
       


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()