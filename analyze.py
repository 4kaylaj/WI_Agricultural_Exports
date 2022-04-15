#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:35:26 2022

@author: kayla
"""
#Import modules
import pandas as pd

#Read csv file into a variable
master_df = pd.read_csv("Soybeans_joined.csv")

#Set index
master_df = master_df.set_index("Unnamed: 0", drop=True)

#Rename index
#Why isn't this working?
master_df = master_df.rename(columns={'Unnamed: 0':'INDEX'})
#Drop uneeded column
master_df = master_df.drop(columns=["E_COMMODITY", "MONTH"])

#Sort by year and state
sort = master_df.sort_values(['YEAR', 'STATE'])

#%%
#See what total_val is measured in??
#Create a figure to show total value from 2013-2020
#Pull out total values by year
year_totals = sort.query("STATE=='-'")
#year_totals = year_totals.drop(columns=["STATE"])
fig = year_totals.plot('YEAR', 'ALL_VAL_YR', title="Soybean Flout/Meal Value by Year", legend=False)

#Set title of X label
fig.set_xlabel("Year")

#Set title of Y label
fig.set_ylabel("Soyean Flour/Meal Value")
#Got help from:
    #https://stackoverflow.com/questions/20865487/pandas-plot-without-a-legend
    #https://stackoverflow.com/questions/21487329/add-x-and-y-labels-to-a-pandas-plot#:~:text=You%20can%20set%20the%20labels%20on%20that%20object.&text=Or%2C%20more%20succinctly%3A%20ax.,name%2C%20if%20it%20has%20one.
    #https://www.geeksforgeeks.org/time-series-plot-or-line-plot-with-pandas/#:~:text=To%20generate%20a%20line%20plot,is%20called%20on%20the%20DataFrame.&text=Set%20the%20values%20to%20be%20represented%20in%20the%20x%2Daxis.
#%%



