#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:46:33 2022

@author: kayla
"""
#Import needed modules 
import os
import pandas as pd
#%%
#Define a function to join CSV files by commodity 
def join_files(ending, filename):
    #Create empty dataframe
    master_df = pd.DataFrame()
    #Create loop to loop through files using os to create path
    for file in os.listdir(os.getcwd()):
        #Create if/then statement to pick out files
        if file.endswith(ending):
            #append results into master dataframe
            master_df = master_df.append(pd.read_csv(file))
    out_file = filename
    if os.path.exists(out_file):
        os.remove(out_file)
    #Write out master_df to CSV file
    master_df.to_csv(filename, index=False)

#%%
#Run join_files function to put all data needed for one commodity
#into one CSV file

join_files("Whey_QTY.csv", "JoinedWhey.csv")
join_files("Ginseng_QTY.csv", "JoinedGinseng.csv")
join_files("Corn_QTY.csv", "JoinedCorn.csv")

join_files("FlourMealSoybean.csv", "VQ_FlourMealSoybean.csv")

join_files("Soybeans.csv", "VQ_Soybeans.csv") 

join_files("Whey.csv", "VQ_Whey.csv")

join_files("Ginseng.csv", "VQ_Ginseng.csv")

join_files("Corn.csv", "VQ_Corn.csv")

join_files("Milk.csv", "VQ_Milk.csv")

#%%

#Was not sure how to do this. Got code from video:
#https://www.youtube.com/watch?v=dcQs8k9WGbY