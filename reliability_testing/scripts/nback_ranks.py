# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 07:25:40 2023

@author: Kriszti
"""

import numpy as np
import pandas as pd
from scipy.stats import norm
Z = norm.ppf

# Functions

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

def d_prime_calc(hits, false_alarms, targets, foils):
    # Calculate hit_rate and avoid d' infinity
    hit_rate = hits / targets
    if hit_rate == 1: 
        hit_rate = 0.99999
    if hit_rate == 0: 
        hit_rate = 0.00001
    # Calculate false alarm rate and avoid d' infinity
    fa_rate = false_alarms / foils
    if fa_rate == 1: 
        fa_rate = 0.99999
    if fa_rate == 0: 
        fa_rate = 0.00001
    # Return d'
    d_prime = Z(hit_rate) - Z(fa_rate)
    return(d_prime)

# Procedure

DF = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Verbal_n_back/data/Verbal_n_back_long_20230310.csv")
omit_1 = "AF|ADHD|ASD|MX|DAMI|555_|5555"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13"]
DF = DF[DF['ID'].str.contains(omit_1) == False]
DF = DF[DF['ID'].isin(omit_2) == False]

DF['div_num'] = float('nan')
rs = {'nback_1_dprime' : [],
      'nback_2_dprime' : [],
      'nback_3_dprime' : [],
      'nback_1_2_mean_dprime' : [],
      'nback_1_2_3_mean_dprime' : []}

for i in range(1):
    print(i)
    df = DF.copy()
    for name, group in df.groupby(['ID', 'block', 'type']):
        ID = group['ID'].unique()[0]
        block = group['block'].unique()[0]
        typ = group['type'].unique()[0]
        group['div_num'] = divide_trials(group)
        df.loc[(df['ID'] == ID) & (df['block'] == block) & (df['type'] == typ)] = group
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    tables = {'one' : [],
              'two' : []}
    for this in [(one, 'one'), (two, 'two')]:
        wide = pd.DataFrame()
        for name, group in this[0].groupby(['ID', 'back_num']):
            ID = group['ID'].unique()[0]
            hs = len(group[(group['type'] == 'target') & (group['ACC'] == 1)])
            fa = len(group[((group['type'] == 'lure_min') | (group['type'] == 'lure_plus')) & (group['ACC'] == 0)])
            ts = len(group[group['type'] == 'target'])
            fs = len(group[(group['type'] == 'lure_min') | (group['type'] == 'lure_plus')])
            wide.loc[ID, 'nback_' + str(name[1]) + '_dprime'] = d_prime_calc(hits = hs,
                                                                             false_alarms = fa,
                                                                             targets = ts,
                                                                             foils = fs)
        wide['nback_1_2_mean_dprime'] = (wide['nback_1_dprime'] + wide['nback_2_dprime']) / 2
        wide['nback_1_2_3_mean_dprime'] = (wide['nback_1_dprime'] + wide['nback_2_dprime'] + wide['nback_3_dprime']) / 3
        tables[this[1]] = wide
    for index in ['nback_1_dprime', 'nback_2_dprime', 'nback_3_dprime', 'nback_1_2_mean_dprime', 'nback_1_2_3_mean_dprime']:
        r = tables['one'][index].corr(tables['two'][index], method = 'spearman')
        rs[index].append(r)

results = pd.DataFrame({'nback_1_dprime' : rs['nback_1_dprime'],
                        'nback_2_dprime' : rs['nback_2_dprime'],
                        'nback_3_dprime' : rs['nback_3_dprime'],
                        'nback_1_2_mean_dprime' : rs['nback_1_2_mean_dprime'],
                        'nback_1_2_3_mean_dprime' : rs['nback_1_2_3_mean_dprime']})

results.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/n_back/data/nback_ranks.csv",
               index = False)
