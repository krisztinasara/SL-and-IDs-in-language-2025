# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:44:01 2023

@author: Kriszti
"""

import pandas as pd

df = pd.read_excel("C:/Users/Kriszti/LENDULET/projektek/giga/elemzesek/SL_nyelvi_kepesseg/SL_lang_data.xlsx")

len(df[(df['dem_age_years'] >= 14) & (df['dem_sex_char'] == "female") & (pd.notna(df['SEGM_AL_ID']))])
len(df[(df['dem_age_years'] >= 14) & (df['dem_sex_char'] == "male") & (pd.notna(df['SEGM_AL_ID']))])

df[(df['dem_age_years'] >= 14)]['dem_age_years'].mean()
