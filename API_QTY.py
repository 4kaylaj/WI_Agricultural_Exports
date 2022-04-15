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
def api_call(year, hs_code,filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
  #Set varialbes
  var_str = "E_COMMODITY,E_COMMODITY_LDESC,QTY_1_YR,QTY_1_YR_FLAG,QTY_2_YR,QTY_2_YR_FLAG"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code,"YEAR":year}
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
api_call("2013","1211201020","2013_ChilledGinseng.csv")

#api_call("2015","1005100010", "2015_ChilledGinseng.csv")
#api_call("2016","1005100010", "2016_ChilledGinseng.csv")
#api_call("2017","1005100010", "2017_ChilledGinseng.csv")
#api_call("2018","1005100010", "2018_ChilledGinseng.csv")
#api_call("2019","1005100010", "2019_ChilledGinseng.csv")
#api_call("2020","1005100010", "2020_ChilledGinseng.csv")
#api_call("2021","1005100010", "2021_ChilledGinseng.csv")
#%%
#api_call("2013","1211201090", "2013_WildGinseng.csv")
#api_call("2014","1211201090", "2014_WildGinseng.csv")
#api_call("2015","1211201090", "2015_WildGinseng.csv")
#api_call("2016","1211201090", "2016_WildGinseng.csv")
#api_call("2017","1211201090", "2017_WildGinseng.csv")
#api_call("2018","1211201090", "2018_WildGinseng.csv")
#api_call("2019","1211201090", "2019_WildGinseng.csv")
#api_call("2020","1211201090", "2020_WIldGinseng.csv")
#api_call("2021","1211201090", "2021_WildGinseng.csv")
#%%
#api_call("2013","1211201020", "2013_CultivatedGinseng.csv")
#api_call("2014","1211201020", "2014_CultivatedGinseng.csv")
#api_call("2015","1211201020", "2015_CultivatedGinseng.csv")
#api_call("2016","1211201020", "2016_CultivatedGinseng.csv")
#api_call("2017","1211201020", "2017_CultivatedGinseng.csv")
#api_call("2018","1211201020", "2018_CultivatedGinseng.csv")
#api_call("2019","1211201020", "2019_CultivatedGinseng.csv")
#api_call("2020","1211201020", "2020_CultivatedGinseng.csv")
#api_call("2021","1211201020", "2021_CultivatedGinseng.csv")
#%%


















