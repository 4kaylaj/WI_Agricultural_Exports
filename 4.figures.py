#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:48:06 2022

@author: kayla
"""
#Import needed modules
import pandas as pd
import matplotlib.pyplot as plt


#Import CSV files into variables
master_soybeanFM=pd.read_csv("Master_SoybeanFM.csv")
master_soybean=pd.read_csv("Master_Soybean.csv")
master_whey=pd.read_csv("Master_Whey.csv")
master_gin=pd.read_csv("Master_Gin.csv")
master_corn=pd.read_csv("Master_Corn.csv")
master_milk=pd.read_csv("Master_Milk.csv")

#Add price column and WI QTY Column
def clean (df):
    df["price"] = df["National_Value"]/df["QTY_1_MO"]
    df["WI_QTY"] = df["WI_Value"]/df["price"]
    df['date'] = df["MONTH"].astype(str) + "/" + df["YEAR"].astype(str)
    date = pd.to_datetime(df['date'])
    df['date'] = date
    df['MONTH'] = date.dt.month
    df['YEAR'] = date.dt.year

#Run clean function
clean(master_soybeanFM)
clean(master_soybean)
clean(master_whey)
clean(master_gin)
clean(master_corn)
clean(master_milk)
#%%
#Compute annual averages
#Compute soybeanFM annual averages
mean_W = master_soybeanFM.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_soybeanFM.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_soybeanFM = master_soybeanFM.merge(mean_W, left_on='YEAR', right_index=True)
master_soybeanFM = master_soybeanFM.merge(mean_N, left_on='YEAR', right_index=True)

#Compute soybean annual averages
mean_W = master_soybean.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_soybean.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_soybean = master_soybean.merge(mean_W, left_on='YEAR', right_index=True)
master_soybean = master_soybean.merge(mean_N, left_on='YEAR', right_index=True)

#Compute whey annual average
mean_W = master_whey.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_whey.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_whey = master_whey.merge(mean_W, left_on='YEAR', right_index=True)
master_whey = master_whey.merge(mean_N, left_on='YEAR', right_index=True)

#Compute gin annual average
mean_W = master_gin.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_gin.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_gin = master_gin.merge(mean_W, left_on='YEAR', right_index=True)
master_gin = master_gin.merge(mean_N, left_on='YEAR', right_index=True)

#Compute corn annual average
mean_W = master_corn.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_corn.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_corn = master_corn.merge(mean_W, left_on='YEAR', right_index=True)
master_corn = master_corn.merge(mean_N, left_on='YEAR', right_index=True)

#Compute milk annual average
mean_W = master_milk.groupby("YEAR")["WI_QTY"].mean()
mean_W = mean_W.rename("WI_Mean")

mean_N = master_milk.groupby("YEAR")["QTY_1_MO"].mean()
mean_N = mean_N.rename('NAT_Mean')

master_milk = master_milk.merge(mean_W, left_on='YEAR', right_index=True)
master_milk = master_milk.merge(mean_N, left_on='YEAR', right_index=True)

#%%
#Create a function to plot monthly exports and annual export averages at both
#for both the nation and Wisconsin
def plot(df,time, quantity, title,figure):
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(df["date"], df["QTY_1_MO"])
    ax1.plot(df["date"], df["NAT_Mean"])
    ax2.plot(df["date"],df["WI_QTY"])
    ax2.plot(df["date"], df["WI_Mean"])
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

#Run plot function
plot(master_soybeanFM,"2018-06-01", "Quantity (Kg)","Soybean Flour Exports", 'SoybeanFM.png')
plot(master_soybean,"2018-06-01","Quantity (Kg)","Soybean Exports", 'Soybean.png')
plot(master_whey,"2018-06-01","Quantity (Kg)","Whey Exports", "Whey.png")
plot(master_gin,"2018-06-01","Quantity (Kg)","Ginseng Exports","Ginseng.png")
plot(master_corn,"2018-06-01","Quantity (Kg)","Corn Exports","Corn.png")
plot(master_milk,"2018-06-01","Quantity (L)","Milk Exports","Milk.png")
#%%
#Update CSV files
master_soybeanFM.to_csv("Master_SoybeanFM.csv", index=False)
master_soybean.to_csv("Master_Soybean.csv", index=False)
master_whey.to_csv("Master_Whey.csv", index=False)
master_gin.to_csv("Master_Gin.csv", index=False)
master_corn.to_csv("Master_Corn.csv", index=False)
master_milk.to_csv("Master_Milk.csv", index=False)

