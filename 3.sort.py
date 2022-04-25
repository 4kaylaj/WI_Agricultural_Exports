#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 15:28:35 2022

@author: kayla
"""
#NEED TO MAKE ALL MASTER LOOK THE SAME
#Import modules
import pandas as pd  

#Read csv file into a variable
soybeanFM_df=pd.read_csv("VQ_FlourMealSoybean.csv")
soybean_df=pd.read_csv("VQ_Soybeans.csv")
whey_df=pd.read_csv("VQ_Whey.csv", dtype={"E_COMMODITY":str})
gin_df=pd.read_csv("VQ_Ginseng.csv")
corn_df=pd.read_csv("VQ_Corn.csv")
#cran_df = pd.read_csv("VQ_Cranberries.csv")
#%%
#SoybeanFM
QSoybeanFM = soybeanFM_df.loc[soybeanFM_df["QTY_1_YR"] >= 0]
VSoybeanFM = soybeanFM_df.query("STATE=='-'")
WISoybeanFM = soybeanFM_df.query("STATE=='WI'")

#Sort
QSoybeanFM = QSoybeanFM.sort_values(['YEAR','MONTH'])
VSoybeanFM = VSoybeanFM.sort_values(['YEAR','MONTH'])
WISoybeanFM = WISoybeanFM.sort_values(['YEAR','MONTH'])

#Clean: drop uneccesary columns
drop_list = ["STATE", "ALL_VAL_YR", "E_COMMODITY.1",
             "QTY_2_YR", "QTY_2_YR_FLAG"]
QSoybeanFM = QSoybeanFM.drop(columns=drop_list)

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
VSoybeanFM = VSoybeanFM.drop(columns=drop_list)

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
WISoybeanFM = WISoybeanFM.drop(columns=drop_list)

#Merge
Master_SoybeanFM = VSoybeanFM.merge(QSoybeanFM,
                                    on=['YEAR', 'MONTH', 'E_COMMODITY_LDESC'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
#Check Merge
print("Check Merge:")
print(Master_SoybeanFM['_merge'].value_counts())

#Clean Master DF
Master_SoybeanFM = Master_SoybeanFM.drop(columns= "_merge")

#Add WI data
Master_SoybeanFM = Master_SoybeanFM.merge(WISoybeanFM,
                                          on=['YEAR', 'MONTH', 'E_COMMODITY_LDESC'],
                                          how='outer',
                                          validate='m:m',
                                          indicator=True)

print("Check Merge:")
print(Master_SoybeanFM['_merge'].value_counts())

#Clean Master DF
#Rename Columns
Master_SoybeanFM = Master_SoybeanFM.rename(columns= {'ALL_VAL_YR_x':'National_Value',
                                                     'ALL_VAL_YR_y':'WI_Value'})
Master_SoybeanFM = Master_SoybeanFM.drop(columns= ["_merge",'STATE_x',"STATE_y",
                                                   "E_COMMODITY_x", "E_COMMODITY_LDESC",
                                                   "E_COMMODITY_y", "QTY_1_YR_FLAG",
                                                   "E_COMMODITY"] )
#Write out master to CSV file
Master_SoybeanFM.to_csv("Master_SoybeanFM.csv", index=False)

#%%
#Soybean
#soybean_df=pd.read_csv("VQ_Soybeans.csv")
QSoybean = soybean_df.loc[soybean_df["QTY_1_YR"] >= 0]
VSoybean = soybean_df.query("STATE=='-'")
WISoybean = soybean_df.query("STATE=='WI'")

#Sort
QSoybean = QSoybean.sort_values(['YEAR','MONTH'])
VSoybean = VSoybean.sort_values(['YEAR','MONTH'])
WISoybean = WISoybean.sort_values(['YEAR','MONTH'])

#Clean: drop uneccesary columns
drop_list = ["STATE", "ALL_VAL_YR", "E_COMMODITY.1",
             "QTY_2_YR", "QTY_2_YR_FLAG"]
QSoybean = QSoybean.drop(columns=drop_list)

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
VSoybean = VSoybean.drop(columns=drop_list)

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
WISoybean = WISoybean.drop(columns=drop_list)

#Merge
Master_Soybean = VSoybean.merge(QSoybean,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
#Check Merge
print("Check Merge:")
print(Master_Soybean['_merge'].value_counts())

#Clean Master DF
Master_Soybean = Master_Soybean.drop(columns= "_merge")
#%%
#Add WI data
Master_Soybean = Master_Soybean.merge(WISoybean,
                                          on=['YEAR', 'MONTH'],
                                          how='outer',
                                          validate='m:m',
                                          indicator=True)

print("Check Merge:")
print(Master_Soybean['_merge'].value_counts())

#Clean Master DF
#Rename Columns
Master_Soybean = Master_Soybean.rename(columns= {'ALL_VAL_YR_x':'National_Value',
                                                     'ALL_VAL_YR_y':'WI_Value'})
Master_Soybean = Master_Soybean.drop(columns= ["_merge",'STATE_x',"STATE_y",
                                               "E_COMMODITY_x","E_COMMODITY_LDESC_x",
                                               "E_COMMODITY_y","E_COMMODITY_LDESC_y",
                                               "QTY_1_YR_FLAG","E_COMMODITY",
                                               "E_COMMODITY_LDESC"] )

Master_Soybean.to_csv("Master_Soybean.csv", index=False)

#%%
#whey_df=pd.read_csv("VQ_Whey.csv")
#Whey

#Pull out quantities
QWhey = whey_df.loc[whey_df["QTY_1_YR"] >= 0]
#Drop columns
drop_list = ["E_COMMODITY.1","STATE", "ALL_VAL_YR",
             "QTY_2_YR", "QTY_2_YR_FLAG"]
QWhey = QWhey.drop(columns=drop_list)

#Sort
QWhey = QWhey.sort_values(['YEAR','MONTH'])

#Select Differnt Kinds of Whey Quantity
QModWhey = QWhey.loc[QWhey["E_COMMODITY"] == "404100850"]
#Rename Columns
QModWhey = QModWhey.rename(columns= {"QTY_1_YR":'ModWhey_QTY'})
QModOtherWhey = QWhey.loc[QWhey["E_COMMODITY"] == "404100850"]
#Rename columns
QModOtherWhey = QModOtherWhey.rename(columns= {'QTY_1_YR':'ModOtherWhey_QTY'})
QFluidOtherWhey = QWhey.loc[QWhey["E_COMMODITY"] == "404102000"]
#Rename
QFluidOtherWhey = QFluidOtherWhey.rename(columns= {'QTY_1_YR':'FluidOtherWhey_QTY'})
QDriedOtherWhey = QWhey.loc[QWhey["E_COMMODITY"] == "404104000"]
#Rename
QDriedOtherWhey = QDriedOtherWhey.rename(columns= {'QTY_1_YR':'DriedOtherWhey_QTY'})

#Start merging differnt kinds of whey together
Master_Whey = QModWhey.merge(QModOtherWhey,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)

print("Check Merge:")
print(Master_Whey['_merge'].value_counts())

Master_Whey = Master_Whey.drop(columns= ["_merge", "E_COMMODITY_x",
                                         "E_COMMODITY_LDESC_x","QTY_1_YR_FLAG_x",
                                         "E_COMMODITY_y","E_COMMODITY_LDESC_y",
                                         "QTY_1_YR_FLAG_y"])

Master_Whey = Master_Whey.merge(QFluidOtherWhey,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
print("Check Merge:")
print(Master_Whey['_merge'].value_counts())

Master_Whey = Master_Whey.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC","QTY_1_YR_FLAG"])

Master_Whey = Master_Whey.merge(QDriedOtherWhey,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)

print("Check Merge:")
print(Master_Whey['_merge'].value_counts())

Master_Whey = Master_Whey.drop(columns= ["_merge", "E_COMMODITY",
                                         "E_COMMODITY_LDESC","QTY_1_YR_FLAG"])

#Sum Quantities to HS Level of Values
sum_list = ["ModWhey_QTY","ModOtherWhey_QTY","FluidOtherWhey_QTY",
            "DriedOtherWhey_QTY"]
Master_Whey['Sum'] = Master_Whey[sum_list].sum(axis=1)
#https://moonbooks.org/Articles/How-to-sum-multiple-columns-together-of-a-dataframe-with-pandas-in-python-/
#%%
VWhey = whey_df.query("STATE=='-'")
WIWhey = whey_df.query("STATE=='WI'")

#Sort
VWhey = VWhey.sort_values(['YEAR','MONTH'])
WIWhey = WIWhey.sort_values(['YEAR','MONTH'])

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
VWhey = VWhey.drop(columns=drop_list)

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
WIWhey = WIWhey.drop(columns=drop_list)
#%%
#Merge
Master_Whey = Master_Whey.merge(VWhey,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
#Check Merge
print("Check Merge:")
print(Master_Whey['_merge'].value_counts())

#Clean Master DF
Master_Whey = Master_Whey.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC", "STATE"])

Master_Whey = Master_Whey.rename(columns= {'ALL_VAL_YR':'National_Value'})

#Add WI data
Master_Whey = Master_Whey.merge(WIWhey,
                                          on=['YEAR', 'MONTH'],
                                          how='outer',
                                          validate='m:m',
                                          indicator=True)

print("Check Merge:")
print(Master_Whey['_merge'].value_counts())

Master_Whey = Master_Whey.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC", "STATE"])

Master_Whey = Master_Whey.rename(columns= {'ALL_VAL_YR':'WI_Value'})

Master_Whey.to_csv("Master_Whey.csv", index=False)

#%%
#Ginseng
#Pull out quantities
QGin = gin_df.loc[whey_df["QTY_1_YR"] >= 0]
#Drop columns
drop_list = ["STATE", "ALL_VAL_YR",
             "QTY_2_YR", "QTY_2_YR_FLAG"]
QGin = QGin.drop(columns=drop_list)

#Sort
QGin = QGin.sort_values(['YEAR','MONTH'])

#Select Differnt Kinds of Whey Quantity
QCultGin = QGin.loc[QGin["E_COMMODITY"] == 1211201090]
#Rename Columns
QCultGin = QCultGin.rename(columns= {"QTY_1_YR":'CultGin_QTY'})

#Drop Columns
drop_list = ["E_COMMODITY","E_COMMODITY_LDESC",
          "QTY_1_YR_FLAG","E_COMMODITY.1"]

QCultGin = QCultGin.drop(columns=drop_list)

QWildGin = QGin.loc[QGin["E_COMMODITY"] == 1211201020]
#Rename columns
QWildGin = QWildGin.rename(columns= {'QTY_1_YR':'WildGin_QTY'})

drop_list = ["E_COMMODITY","E_COMMODITY_LDESC",
          "QTY_1_YR_FLAG","E_COMMODITY.1"]

QWildGin = QWildGin.drop(columns=drop_list)
#%%
#Start merging differnt kinds of whey together
Master_Gin = QCultGin.merge(QWildGin,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)

print("Check Merge:")
print(Master_Gin['_merge'].value_counts())

drop_list=["_merge"]
Master_Gin = Master_Gin.drop(columns=drop_list)
                              
#Sum Quantities to HS Level of Values
sum_list = ["CultGin_QTY","WildGin_QTY"]
Master_Gin['Sum'] = Master_Gin[sum_list].sum(axis=1)
#%%
VGin = gin_df.query("STATE=='-'")
WIGin = gin_df.query("STATE=='WI'")

#Sort
VGin = VGin.sort_values(['YEAR','MONTH'])
WIGin = WIGin.sort_values(['YEAR','MONTH'])

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
VGin = VGin.drop(columns=drop_list)

VGin = VGin.rename(columns= {"ALL_VAL-YR":'National_Value'})

drop_list = ["QTY_1_YR", "QTY_1_YR_FLAG", "QTY_2_YR",
             "QTY_2_YR_FLAG", "E_COMMODITY.1"]
WIGin = WIGin.drop(columns=drop_list)

WIGin = WIGin.rename(columns= {"ALL_VAL-YR":'WI_Value'})
#%%
#Merge VGin onto onto Master
Master_Gin = Master_Gin.merge(VGin,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
#Check Merge
print("Check Merge:")
print(Master_Gin['_merge'].value_counts())

#Clean Master DF
Master_Gin = Master_Gin.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC", "STATE"])

#Rename Column
Master_Gin = Master_Gin.rename(columns= {'ALL_VAL_YR':'National_Value'})
#%%
#Add WI data
Master_Gin = Master_Gin.merge(WIGin,
                                          on=['YEAR', 'MONTH'],
                                          how='outer',
                                          validate='m:m',
                                          indicator=True)

print("Check Merge:")
print(Master_Gin['_merge'].value_counts())

Master_Gin = Master_Gin.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC", "STATE"])

Master_Gin = Master_Gin.rename(columns= {'ALL_VAL_YR':'WI_Value'})

Master_Gin.to_csv("Master_Gin.csv", index=False)

#%%
#%%
#Corn
#Pull out quantities
QCorn = corn_df.loc[corn_df["QTY_1_YR"] >= 0]
#Drop columns
drop_list = ["STATE", "ALL_VAL_YR",
             "QTY_2_YR", "QTY_2_YR_FLAG"]
QCorn = QCorn.drop(columns=drop_list)
VCorn = corn_df.query("STATE=='-'")
WICorn = corn_df.query("STATE=='WI'")

#Sort
QCorn = QCorn.sort_values(['YEAR','MONTH'])
VCorn = VCorn.sort_values(['YEAR','MONTH'])
WICorn = WICorn.sort_values(['YEAR','MONTH'])

#Select Differnt Kinds of Whey Quantity
QCornmealCorn = QCorn.loc[QCorn["E_COMMODITY"] == 1103130020]
#Rename Columns
QCronmealCorn = QCornmealCorn.rename(columns= {"QTY_1_YR":'Cornmeal_QTY'})

#Drop Columns
drop_list = ["E_COMMODITY","E_COMMODITY_LDESC",
          "QTY_1_YR_FLAG","E_COMMODITY.1"]

QCornmealCorn = QCornmealCorn.drop(columns=drop_list)

QCornmealCorn = QCornmealCorn.rename(columns= {'QTY_1_YR':'Cornmeal_QTY'})

#Missing data
QOtherCorn = QCorn.loc[QCorn["E_COMMODITY"] == 1103130060]

drop_list = ["E_COMMODITY","E_COMMODITY_LDESC",
          "QTY_1_YR_FLAG","E_COMMODITY.1"]

QOtherCorn = QOtherCorn.rename(columns= {'QTY_1_YR':'Other_QTY'})

QOtherCorn = QOtherCorn.drop(columns=drop_list)
#%%
#Start merging differnt kinds of corn together
master_corn = QCornmealCorn.merge(QOtherCorn,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)

print("Check Merge:")
print(master_corn['_merge'].value_counts())

drop_list=["_merge"]
master_corn = master_corn.drop(columns=drop_list)
                              
#Sum Quantities to HS Level of Values
sum_list = ["Cornmeal_QTY","Other_QTY"]
master_corn['Sum'] = master_corn[sum_list].sum(axis=1)
#%%
#Merge VCorn onto onto Master
master_corn = master_corn.merge(VCorn,
                                    on=['YEAR', 'MONTH'],
                                    how='outer',
                                    validate="m:m",
                                    indicator=True)
#Check Merge
print("Check Merge:")
print(master_corn['_merge'].value_counts())

#Clean Master DF
master_corn = master_corn.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC","STATE",
                                         "QTY_1_YR","QTY_1_YR_FLAG",
                                         "QTY_2_YR","QTY_2_YR_FLAG"])

#Rename Column
master_corn = master_corn.rename(columns= {'ALL_VAL_YR':'National_Value'})
#%%
#Add WI data
master_corn = master_corn.merge(WICorn,
                                          on=['YEAR', 'MONTH'],
                                          how='outer',
                                          validate='m:m',
                                          indicator=True)

print("Check Merge:")
print(master_corn['_merge'].value_counts())

master_corn = master_corn.drop(columns= ["_merge","E_COMMODITY",
                                         "E_COMMODITY_LDESC", "STATE",
                                         "QTY_1_YR", "QTY_1_YR_FLAG",
                                         "QTY_2_YR", "QTY_2_YR_FLAG"])

master_corn = master_corn.rename(columns= {'ALL_VAL_YR':'WI_Value'})

master_corn.to_csv("Master_Corn.csv", index=False)
#Got help from
#https://www.stackvidhya.com/select-rows-from-dataframe/









