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
def api_call(year, hs_code):
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
  df = pd.DataFrame(columns=colnames, data=datarows)
  #Do nothing if QTY=M???
  for rec in df:
      if df["QTY_1_YR_FLAG"] == 'M':
          print("Flag: Missing Values for QTY_1_YR")
      else:
          print(df['QTY_1_YR'])
      if df["QTY_2_YR_FLAG"] == "M":
          print("Flag: Missing Values for QTY_2_YR")
      else:
          print(df['QTY_2_YR'])

  
#%%
api_call("2013","121120")
#%%


















