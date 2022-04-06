#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:06:09 2022

@author: kayla
"""
#Import modules
import os
import pandas as pd

#Create empty dataframe
master_df = pd.DataFrame()

#Create loop to loop through files using os to create path
for file in os.listdir(os.getcwd()):
    #Create if/then statement to pick out files
    if file.endswith('.csv'):
        #append results into master dataframe
        master_df = master_df.append(pd.read_csv(file))

#Write out master_df to CSV file
master_df.to_csv("121130_joined.csv", index=False)

#Was not sure how to do this. Got code from video:
#https://www.youtube.com/watch?v=dcQs8k9WGbY
    