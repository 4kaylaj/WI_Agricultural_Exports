#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:00:23 2022

@author: kayla
"""

#%%
#Import requests and pandas modules 
import requests
import pandas as pd

#%%
#Define a funtion to create an api call using an hs code as arguement 
#to get value varialbe
def val_call(hs_code, filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs'
  #Set varialbes
  var_str = "STATE,ALL_VAL_MO,E_COMMODITY,E_COMMODITY_LDESC,YEAR,MONTH"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code}
  #Create response varialbe
  response=requests.get(api,payload)
  #Print results
  print(f"Status code: {response.status_code}")
  #Create a dataframe
  row_list = response.json()
  #Set column name list
  colnames = row_list[0]
  #Define data
  datarows = row_list[1:]
  #Convert into a Pandas dataframe
  dataframe = pd.DataFrame(columns=colnames, data=datarows)
  #Write dataframe to file
  dataframe.to_csv(filename,index=False)
#%%
#Run val_call function
#Flour/Meal Soybeans
val_call("120810", "FlourMealSoybean.csv")

#Soybeans, Whether or Not Broken (1201)
val_call("120110", "Soybeans.csv")

#Whey
val_call("040410", "Whey.csv")

#Ginseng
val_call("121120", "Ginseng.csv")

#Corn
val_call("110313", "Corn.csv")

#Milk (less than 1% fat)
val_call("040110", "Milk.csv")

#%%
#Define a funtion to create an api call using an hs code as arguement 
#to get quantity varialbe
def quant_call(hs_code, filename):
  #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
  #Set varialbes
  var_str = "E_COMMODITY_LDESC,QTY_1_MO,UNIT_QY1,YEAR,MONTH"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code}
  #Create response varialbe
  response=requests.get(api,payload)
  #Print results
  print(f"Status code: {response.status_code}")
  #Create a dataframe
  row_list = response.json()
  #Set column name list
  colnames = row_list[0]
  #Define data
  datarows = row_list[1:]
  #Convert into a Pandas dataframe
  df = pd.DataFrame(columns=colnames, data=datarows)
  #Write dataframe to file
  df.to_csv(filename, index=False)

#%%
#Run quant_call function
#Note: for some commodities, there are multiple quantity values 
#that need to be aggregated to match the value variables. This is true
#for whey, ginseng, and corn.
#Flour/Meal Soybeans
quant_call("1208100000", "QTY_FlourMealSoybean.csv")

#Soybeans, Whether or Not Broken
quant_call("1201100000", "QTY_Soybeans.csv")

#Whey
quant_call("0404100500", "ModWhey_QTY.csv") #Kg
quant_call("0404100850", "ModOtherWhey_QTY.csv") #Kg
quant_call("0404102000", "FluidOtherWhey_QTY.csv") #liter
quant_call("0404104000", "DriedOtherWhey_QTY.csv") #Kg

#Ginseng
quant_call("1211201020", "CultivatedGinseng_QTY.csv")
quant_call("1211201090", "WildGinseng_QTY.csv")

#Corn
quant_call("1103130020", "CornmealCorn_QTY.csv")
quant_call("1103130060", "OtherCorn_QTY.csv")

#1% Milk
quant_call("0401100000", "QTY_Milk.csv")









