#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:48:06 2022

@author: kayla
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Import CSV files into variables
master_soybeanFM=pd.read_csv("Master_SoybeanFM.csv")
master_soybean=pd.read_csv("Master_Soybean.csv")
master_whey=pd.read_csv("Master_Whey.csv")
master_gin=pd.read_csv("Master_Gin.csv")
master_corn=pd.read_csv("Master_Corn.csv")

#Add price column and WI QTY Column

master_soybeanFM["price"] = master_soybeanFM["National_Value"]/master_soybeanFM["QTY_1_YR"]
master_soybeanFM["WI_QTY"] = master_soybeanFM["WI_Value"]/master_soybeanFM["price"]

master_soybeanFM['date'] = master_soybeanFM["MONTH"].astype(str) + "/" + master_soybeanFM["YEAR"].astype(str)
date = pd.to_datetime(master_soybeanFM['date'])

master_soybeanFM['date'] = date
master_soybeanFM['MONTH'] = date.dt.month
master_soybeanFM['YEAR'] = date.dt.year

master_soybean["price"] = master_soybean["National_Value"]/master_soybean["QTY_1_YR"]
master_soybean["WI_QTY"] = master_soybean["WI_Value"]/master_soybean["price"]

master_soybean['date'] = master_soybean["MONTH"].astype(str) + "/" + master_soybean["YEAR"].astype(str)
date = pd.to_datetime(master_soybean['date'])

master_soybean['date'] = date
master_soybean['MONTH'] = date.dt.month
master_soybean['YEAR'] = date.dt.year

master_whey["price"] = master_whey["National_Value"]/master_whey["Sum"]
master_whey["WI_QTY"] = master_whey["WI_Value"]/master_whey["price"]

master_whey['date'] = master_whey["MONTH"].astype(str) + "/" + master_whey["YEAR"].astype(str)
date = pd.to_datetime(master_whey['date'])

master_whey['date'] = date
master_whey['MONTH'] = date.dt.month
master_whey['YEAR'] = date.dt.year

master_gin["price"] = master_gin["National_Value"]/master_gin["Sum"]
master_gin["WI_QTY"] = master_gin["WI_Value"]/master_gin["price"]

master_gin['date'] = master_gin["MONTH"].astype(str) + "/" + master_gin["YEAR"].astype(str)
date = pd.to_datetime(master_gin['date'])

master_gin['date'] = date
master_gin['MONTH'] = date.dt.month
master_gin['YEAR'] = date.dt.year

master_corn["price"] = master_corn["National_Value"]/master_corn["Sum"]
master_corn["WI_QTY"] = master_corn["WI_Value"]/master_corn["price"]

master_corn['date'] = master_corn["MONTH"].astype(str) + "/" + master_corn["YEAR"].astype(str)
date = pd.to_datetime(master_corn['date'])

master_corn['date'] = date
master_corn['MONTH'] = date.dt.month
master_corn['YEAR'] = date.dt.year

#%%
fig, ax1 = plt.subplots()
sns.lineplot(data=master_soybeanFM, x="date", y="WI_QTY", palette="crest", ax=ax1)
#Set the title for ax1
ax1.set_title("WI Soybean (Flour/Meal) Exports")

#Set title of X label
ax1.set_xlabel("Year")

ax1.set_ylabel("Quantity")

ax1.axvline(pd.Timestamp("2019-01-01"),color="red")
#axq.refline(x=["Year"==2019])

#sns.lineplot(data=master_soybeanFM, x="date", y="QTY_1_YR", palette="crest", ax=ax1)

#Tighten layout
#fig.tight_layout()
#%%
#Will have to do in pandas to get it to skip missing data
fig, ax2 = plt.subplots()
sns.lineplot(data=master_soybean, x="date", y="WI_QTY", palette="crest", ax=ax2)
#Set the title for ax1
ax2.set_title("WI Soybean Exports")

#Set title of X label
ax2.set_xlabel("Year")
ax2.set_ylabel("Quantity")
#%%
fig, ax3 = plt.subplots()
sns.lineplot(data=master_whey, x="date", y="WI_QTY", palette="crest", ax=ax3)
#Set the title for ax1
ax3.set_title("WI Whey Exports")

#Set title of X label
ax3.set_xlabel("Year")

ax3.set_ylabel("Quantity")
#%%
fig, ax4 = plt.subplots()
sns.lineplot(data=master_gin, x="date", y="WI_QTY", palette="crest", ax=ax4)
#Set the title for ax1
ax4.set_title("WI Ginseng Exports")

#Set title of X label
ax4.set_xlabel("Year")

ax4.set_ylabel("Quantity")
#%%
fig, ax5 = plt.subplots()
sns.lineplot(data=master_corn, x="date", y="WI_QTY", palette="crest", ax=ax5)
#Set the title for ax1
ax5.set_title("WI Corn Exports")

#Set title of X label
ax5.set_xlabel("Year")

ax5.set_ylabel("Quantity")
#%%






