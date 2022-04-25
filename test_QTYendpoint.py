#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:13:51 2022

@author: kayla
"""
#Need to use 10-digit HS code and add month to the query 
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
  var_str = "E_COMMODITY,E_COMMODITY_LDESC,QTY_1_YR,QTY_1_YR_FLAG,QTY_2_YR,QTY_2_YR_FLAG,MONTH"
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
  #Write dataframe to file
  df.to_csv(filename)

#%%
#Soybeans in 2013
api_call("2013", "1208100000", "2013_Test.csv")
#Soybeans in 2013
#api_call("2013", "1201", "2013_1201.csv")
#Corn in 2020
#api_call("2020","1005", "2020_1005.csv")
#Soybeans in 2020
#api_call("2020", "1201", "2020_1201.csv")
#%%

