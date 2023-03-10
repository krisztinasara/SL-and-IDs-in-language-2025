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

omit_1 = "AF|ADHD|ASD|MX|DAMI|555_|5555"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13"]

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

vis_rt = vis_rt[vis_rt['ID'].str.contains(omit_1) == False]
vis_rt = vis_rt[vis_rt['ID'].isin(omit_2) == False]

ac_rt = ac_rt[ac_rt['ID'].str.contains(omit_1) == False]
ac_rt = ac_rt[ac_rt['ID'].isin(omit_2) == False]

vis_dec = vis_dec[vis_dec['ID'].str.contains(omit_1) == False]
vis_dec = vis_dec[vis_dec['ID'].isin(omit_2) == False]

ac_dec = ac_dec[ac_dec['ID'].str.contains(omit_1) == False]
ac_dec = ac_dec[ac_dec['ID'].isin(omit_2) == False]

# iternum
iternum = 100

# reliabilities
rs = {'vis_RT_med' : [],
      'ac_RT_med' : [],
      'vis_dec_score' : [],
      'vis_dec_RT_med' : [],
      'ac_dec_score' : [],
      'ac_dec_RT_med' : []
      }

# collect IDs
vis_rt_IDs = list(vis_rt.ID.unique())
ac_rt_IDs = list(ac_rt.ID.unique())
vis_dec_IDs = list(vis_dec.ID.unique())
ac_dec_IDs = list(ac_dec.ID.unique())

for i in range(0, iternum):
    print(i)
    # vis rt
    df = vis_rt.copy()
    for ID in vis_rt_IDs:
        df.loc[df['ID'] == ID, 'div_num'] = divide_trials(df[df['ID'] == ID])
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    one_data = pd.DataFrame()
    two_data = pd.DataFrame()
    for ID in vis_rt_IDs:
        one_data.loc[ID, 'vis_RT_med'] = one[one['ID'] == ID]['visRT_key_resp.rt'].median()
        two_data.loc[ID, 'vis_RT_med'] = two[two['ID'] == ID]['visRT_key_resp.rt'].median()
    all_data = one_data.join(two_data, how = "outer",
                             lsuffix = "_one", rsuffix = "_two")
    r = all_data['vis_RT_med_one'].corr(all_data['vis_RT_med_two'], method = 'pearson')
    rs['vis_RT_med'].append((2 * r) / (1 + r))

    # ac rt
    df = ac_rt.copy()
    for ID in ac_rt_IDs:
        df.loc[df['ID'] == ID, 'div_num'] = divide_trials(df[df['ID'] == ID])
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    one_data = pd.DataFrame()
    two_data = pd.DataFrame()
    for ID in ac_rt_IDs:
        one_data.loc[ID, 'ac_RT_med'] = one[one['ID'] == ID]['acRT_key_resp.rt'].median()
        two_data.loc[ID, 'ac_RT_med'] = two[two['ID'] == ID]['acRT_key_resp.rt'].median()
    all_data = one_data.join(two_data, how = "outer",
                             lsuffix = "_one", rsuffix = "_two")
    r = all_data['ac_RT_med_one'].corr(all_data['ac_RT_med_two'], method = 'pearson')
    rs['ac_RT_med'].append((2 * r) / (1 + r))

    # vis dec
    df = vis_dec.copy()
    for ID in vis_dec_IDs:
        df.loc[df['ID'] == ID, 'div_num'] = divide_trials(df[df['ID'] == ID])
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    one_data = pd.DataFrame()
    two_data = pd.DataFrame()
    for ID in vis_dec_IDs:
        one_data.loc[ID, 'vis_dec_RT_med'] = one[(one['ID'] == ID) & (one['trial_vischoice_key_resp.corr'] == 1)]['trial_vischoice_key_resp.rt'].median()
        one_data.loc[ID, 'vis_dec_ACC'] = one[one['ID'] == ID]['trial_vischoice_key_resp.corr'].mean()
        one_data.loc[ID, 'vis_dec_score'] = 1 - ((one_data.at[ID, 'vis_dec_RT_med']) * (1 - (one_data.at[ID, 'vis_dec_ACC'])))
        two_data.loc[ID, 'vis_dec_RT_med'] = two[(two['ID'] == ID) & (two['trial_vischoice_key_resp.corr'] == 1)]['trial_vischoice_key_resp.rt'].median()
        two_data.loc[ID, 'vis_dec_ACC'] = two[two['ID'] == ID]['trial_vischoice_key_resp.corr'].mean()
        two_data.loc[ID, 'vis_dec_score'] = 1 - ((two_data.at[ID, 'vis_dec_RT_med']) * (1 - (two_data.at[ID, 'vis_dec_ACC'])))
    all_data = one_data.join(two_data, how = "outer",
                             lsuffix = "_one", rsuffix = "_two")
    for index in ['vis_dec_RT_med', 'vis_dec_score']:
        r = all_data[index + '_one'].corr(all_data[index + '_two'], method = 'pearson')
        rs[index].append((2 * r) / (1 + r))

    # ac dec
    df = ac_dec.copy()
    for ID in ac_dec_IDs:
        df.loc[df['ID'] == ID, 'div_num'] = divide_trials(df[df['ID'] == ID])
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    one_data = pd.DataFrame()
    two_data = pd.DataFrame()
    for ID in ac_dec_IDs:
        one_data.loc[ID, 'ac_dec_RT_med'] = one[(one['ID'] == ID) & (one['trial_acchoice_key_resp.corr'] == 1)]['trial_acchoice_key_resp.rt'].median()
        one_data.loc[ID, 'ac_dec_ACC'] = one[one['ID'] == ID]['trial_acchoice_key_resp.corr'].mean()
        one_data.loc[ID, 'ac_dec_score'] = 1 - ((one_data.at[ID, 'ac_dec_RT_med']) * (1 - (one_data.at[ID, 'ac_dec_ACC'])))
        two_data.loc[ID, 'ac_dec_RT_med'] = two[(two['ID'] == ID) & (two['trial_acchoice_key_resp.corr'] == 1)]['trial_acchoice_key_resp.rt'].median()
        two_data.loc[ID, 'ac_dec_ACC'] = two[two['ID'] == ID]['trial_acchoice_key_resp.corr'].mean()
        two_data.loc[ID, 'ac_dec_score'] = 1 - ((two_data.at[ID, 'ac_dec_RT_med']) * (1 - (two_data.at[ID, 'ac_dec_ACC'])))
    all_data = one_data.join(two_data, how = "outer",
                             lsuffix = "_one", rsuffix = "_two")
    for index in ['ac_dec_RT_med', 'ac_dec_score']:
        r = all_data[index + '_one'].corr(all_data[index + '_two'], method = 'pearson')
        rs[index].append((2 * r) / (1 + r))

results = pd.DataFrame()
for index in rs:
    try:
        results.loc[index, 'reliability'] = mean(rs[index])
    except:
        pass

results.to_excel(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/results/processing_speed_reliabilities.xlsx"
    )
