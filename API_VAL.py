#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:06:05 2022

@author: kayla
"""
#Import modules
import requests
import pandas as pd

#%%
#Define funtion to creat api call with year & hs arguement
def api_call(year, hs_code, filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs'
  #Set varialbes
  #Cannot get QTY varaiable to work. Check error
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
  #Convert QTY to 
  #Create a dataframe
  row_list = response.json()
  #Set column name list
  colnames = row_list[0]
  #Define data
  datarows = row_list[1:]
  #Convert into a Pandas dataframe
  dataframe = pd.DataFrame(columns=colnames, data=datarows)
  #Set index
  dataframe.set_index("STATE")
  #Write dataframe to file
  dataframe.to_csv(filename)
#%%
#Run api_call function for Flour/Meal Soybeans
api_call("2013","120810", "2013_FlourMealSoybean.csv")
api_call("2014","120810", "2014_FlourMealSoybean.csv")
api_call("2015","120810", "2015_FlourMealSoybean.csv")
api_call("2016","120810", "2016_FlourMealSoybean.csv")
api_call("2017","120810", "2017_FlourMealSoybean.csv")
api_call("2018","120810", "2018_FlourMealSoybean.csv")
api_call("2019","120810", "2019_FlourMealSoybean.csv")
api_call("2020","120810", "2020_FlourMealSoybean.csv")
api_call("2021","120810", "2021_FlourMealSoybean.csv")
#%%
#Soybeans, Whether or Not Broken (1201)
api_call("2013","1201", "2013_1201Soybean.csv")
api_call("2014","1201", "2014_1201Soybean.csv")
api_call("2015","1201", "2015_1201Soybean.csv")
api_call("2016","1201", "2016_1201Soybean.csv")
api_call("2017","1201", "2017_1201Soybean.csv")
api_call("2018","1201", "2018_1201Soybean.csv")
api_call("2019","1201", "2019_1201Soybean.csv")
api_call("2020","1201", "2020_1201Soybean.csv")
api_call("2021","1201", "2021_1201Soybean.csv")

#%%%
api_call("2013","040410", "2013_Whey.csv")
api_call("2014","040410", "2014_Whey.csv")
api_call("2015","040410", "2015_Whey.csv")
api_call("2016","040410", "2016_Whey.csv")
api_call("2017","040410", "2017_Whey.csv")
api_call("2018","040410", "2018_Whey.csv")
api_call("2019","040410", "2019_Whey.csv")
api_call("2020","040410", "2020_Whey.csv")
api_call("2021","040410", "2021_Whey.csv")




























