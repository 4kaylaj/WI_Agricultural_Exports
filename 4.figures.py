#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:48:06 2022

@author: kayla
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Import CSV files into variables
master_soybeanFM=pd.read_csv("Master_SoybeanFM.csv")
master_soybean=pd.read_csv("Master_Soybean.csv")
master_whey=pd.read_csv("Master_Whey.csv")
master_gin=pd.read_csv("Master_Gin.csv")
master_corn=pd.read_csv("Master_Corn.csv")

#Add price column and WI QTY Column
def clean (df):
    df["price"] = df["National_Value"]/df["QTY_1_YR"]
    df["WI_QTY"] = df["WI_Value"]/df["price"]
    df['date'] = df["MONTH"].astype(str) + "/" + df["YEAR"].astype(str)
    date = pd.to_datetime(df['date'])
    df['date'] = date
    df['MONTH'] = date.dt.month
    df['YEAR'] = date.dt.year

clean(master_soybeanFM)
clean(master_soybean)
clean(master_whey)
clean(master_gin)
#clean(master_corn)
#%%
def plot(df,time, quantity, title,figure):
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(df["date"], df["QTY_1_YR"])
    ax2.plot(df["date"], df["WI_QTY"])
    ax1.axvline(pd.Timestamp(time),color="red", linewidth=5, alpha=.3)
    ax2.axvline(pd.Timestamp(time),color="red", linewidth=5, alpha=.3)
    ax1.set_xlabel('Year')
    ax2.set_xlabel('Year')
    ax1.set_ylabel(quantity)
    ax2.set_ylabel(quantity)
    ax1.set_title('National Exports')
    ax2.set_title('WI Exports')
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(figure)
#%%
    
plot(master_soybeanFM,"2019-01-01", "Quantity (Kg)", "Soybean Flour Exports", 'SoybeanFM.png')
plot(master_soybean,"2018-01-01", "Soybean Exports", 'Soybean.png')
plot(master_whey,"2018-01-01", "Whey Exports", "Whey.png")
plot(master_gin,"2018-01-01", "Ginseng Exports","Ginseng.png")
#plot(master_corn, "Corn Exports", "Corn.png")
#%%


