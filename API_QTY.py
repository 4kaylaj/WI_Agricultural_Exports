#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:01:03 2022

@author: kayla
"""

#Import modules
import requests
import pandas as pd

#%%
#Define funtion to creat api call with year & hs arguement
def api_call(year, hs_code, filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
  #Set varialbes
  #Cannot get QTY varaiable to work. Check error
  var_str = "E_COMMODITY,E_COMMODITY_LDESC,QTY_1_YR,QTY_1_YR_FLAG,QTY_2_YR,QTY_2_YR_FLAG"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code,
             "YEAR":year}
  #Create response varialbe
  response=requests.get(api,payload)
  #Print results
  print(f"Status code: {response.status_code}")
  print(f"Response: {response.text}")
  #Convert QTY to 
  #Create a dataframe
  row_list = response.json()
  #Set column name list
  colnames = row_list[0]
  #Define data
  datarows = row_list[1:]
  #Convert into a Pandas dataframe
  dataframe = pd.DataFrame(columns=colnames, data=datarows)
  #Write dataframe to file
  dataframe.to_csv(filename)
#%%
#Figure out how to check quiantiy withotu converting into CSV
api_call("2013","121120", "121130_2013_QTY.csv")
api_call("2014","121120", "121130_2014_QTY.csv")
api_call("2015","121120", "121130_2015_QTY.csv")
api_call("2016","121120", "121130_2016_QTY.csv")
api_call("2017","121120", "121130_2017_QTY.csv")
api_call("2018","121120", "121130_2018_QTY.csv")
api_call("2019","121120", "121130_2019_QTY.csv")
api_call("2020","121120", "121130_2020_QTY.csv")
api_call("2021","121120", "121130_2021_QTY.csv")
#%%


