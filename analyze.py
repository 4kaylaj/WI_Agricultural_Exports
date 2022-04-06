#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:35:26 2022

@author: kayla
"""
#Import modules
import pandas as pd

#Read csv file into a variable
master_df = pd.read_csv("121130_joined.csv")

#Group data
grouped = master_df.groupby(["STATE", "YEAR"])

#%%


