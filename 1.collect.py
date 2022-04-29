#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:00:23 2022

@author: kayla
"""
#Overview:
#This script is used to pull export data from the U.S. Census Bureau,
#USA Trade Online by Harmonized System (HS) code and stores retrieved
#data in CSV files. Although this project examines several commodities,
#exporting data into a CSV file allows the functions to be useful
#for anyone seeking to retrieve general export data from USA Trade Online.
#%%
#This script uses two modules: requests and pandas. 
import requests
import pandas as pd

#%%
#USA Trade Online has several endpoint options. Endpoints can be choosen
#based on 
#Define funtion to creat api call hs arguement to get value varialbe
def val_call(hs_code, filename):
    #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/statehs'
  #Set varialbes
  #Cannot get QTY varaiable to work. Check error
  var_str = "STATE,ALL_VAL_YR,E_COMMODITY,E_COMMODITY_LDESC,YEAR,MONTH"
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
#Run api_call function for Flour/Meal Soybeans
val_call("120810", "FlourMealSoybean.csv")

#Soybeans, Whether or Not Broken (1201)
val_call("120110", "Soybeans.csv")

#Whey
val_call("040410", "Whey.csv")

#Ginseng
val_call("121120", "Ginseng.csv")

#Cranberries, Blueberries, Etc, Fresh
#val_call("081040", "Cranberries.csv")

val_call("110313", "Corn.csv")

#%%
#Define funtion to creat api call with hs arguement to get quantity varialbe
def quant_call(hs_code, filename):
  #Set api varialbe
  api = 'https://api.census.gov/data/timeseries/intltrade/exports/hs'
  #Set varialbes
  #Cannot get QTY varaiable to work. Check error
  var_str = "E_COMMODITY_LDESC,QTY_1_YR,UNIT_QY1,YEAR,MONTH"
  #Set key
  key_value = "881eddebb146c5b0babd4b75ceea21da104a4ad3"
  #Set payload 
  payload = {'get':var_str, 'key':key_value, "E_COMMODITY":hs_code}
  #Create response varialbe
  response=requests.get(api,payload)
  #Print results
  print(f"Status code: {response.status_code}")
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
  df.to_csv(filename, index=False)

#%%
#Run api_call function for Flour/Meal Soybeans
quant_call("1208100000", "QTY_FlourMealSoybean.csv")


#Soybeans, Whether or Not Broken (1201)
quant_call("1201100000", "QTY_Soybeans.csv")
#Need another call here

#Whey
quant_call("0404100500", "ModWhey_QTY.csv") #Kg
quant_call("0404100850", "ModOtherWhey_QTY.csv") #Kg
quant_call("0404102000", "FluidOtherWhey_QTY.csv") #liter
quant_call("0404104000", "DriedOtherWhey_QTY.csv") #Kg

#Ginseng
quant_call("1211201020", "CultivatedGinseng_QTY.csv")
quant_call("1211201090", "WildGinseng_QTY.csv")
#Missing call?

#Cranberries, Blueberries, Etc, Fresh
#Note did not include blueberries so does not fit wiht val call
#quant_call("0810400050", "QTY_Cranberries.csv")

quant_call("1103130020", "CornmealCorn_QTY.csv")
quant_call("1103130060", "OtherCorn_QTY.csv")









