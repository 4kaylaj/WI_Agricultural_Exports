#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:06:05 2022

@author: kayla
"""
#Import modules
import requests
import json
import pandas as pd

#%%
#Define funtion to creat api call with year & hs arguement
def api_call(year, hs_code, filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs'
  #Set varialbes
  var_str = "STATE,ALL_VAL_YR,E_COMMODITY,E_COMMODITY_LDESC"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code,
             "YEAR":year, "MONTH":"12"}
  #Create response varialbe
  response=requests.get(api,payload)
  #Print results
  print(f"Status code: {response.status_code}")
  print(f"Response: {response.text}")
  #Create a dataframe
  row_list = response.json()
  #Set column name list
  colnames = row_list[0]
  #Define data
  datarows = row_list[1:]
  #Convert into a Pandas dataframe
  dataframe = pd.DataFrame(columns=colnames, data=datarows)
  dataframe.to_csv(filename)
#%%
#Run api_call function for ginseng 
api_call("2013","121120", "121130_2013.csv")
api_call("2014","121120", "121130_2014.csv")
api_call("2015","121120", "121130_2015.csv")
api_call("2016","121120", "121130_2016.csv")
api_call("2017","121120", "121130_2017.csv")
api_call("2018","121120", "121130_2018.csv")
api_call("2019","121120", "121130_2019.csv")
api_call("2020","121120", "121130_2020.csv")
api_call("2021", "121120", "121130_2021.csv")
#%%














