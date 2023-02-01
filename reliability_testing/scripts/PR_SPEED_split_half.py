# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:21:22 2023

@author: Kriszti
"""

import numpy as np
import pandas as pd
from statistics import mean

# 1. Functions

def divide_trials(df):
    if len(df) % 2 == 1:
    # if len1 != len2:
        x = np.random.choice([1, 2])
        if x == 1:
            lengroup1 = (len(df) - 1) / 2
            lengroup2 = ((len(df) - 1) / 2) + 1
        elif x == 2:
            lengroup1 = ((len(df) - 1) / 2) + 1
            lengroup2 = (len(df) - 1) / 2
    else:
        lengroup1 = len(df) / 2
        lengroup2 = len(df) / 2    
    div = [1] * int(lengroup1) + [2] * int(lengroup2)
    np.random.shuffle(div)    
    return div

corr_met = input("Correlation method: ")
if corr_met == "":
    corr_met = 'pearson'

# 2. Procedure

vis_rt = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_YA/data/visrt_pm.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/visrt_pm.csv"
         )
     ]
    )

ac_rt = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_YA/data/acrt_pm.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/acrt_pm.csv"
         )
     ]
    )

vis_dec = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_YA/data/visdec_pm.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/visdec_pm.csv"
         )
     ]
    )

ac_dec = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/acdec_pm.csv"
    )

# collect IDs or something


ac_rt_IDs = list(ac_rt.ID.unique())
vis_dec_IDs = list(vis_dec.ID.unique())
ac_dec_RTs = list(ac_dec.ID.unique())

# vis rt

vis_rt_IDs = list(vis_rt.ID.unique())

for i in range(0, iternum):
    df = vis_rt.copy()
    for ID in vis_rt_IDs:
        df.loc[df['ID'] == ID]['div_num'] = divide_trials(df[(df['ID'] == ID) & (df['block'] == block)])
    



