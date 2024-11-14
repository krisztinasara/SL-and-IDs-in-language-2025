# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:25:44 2023

@author: Kriszti
"""

import numpy as np
import pandas as pd

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

# Procedure

DF = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Predictive/data/Predictive_long_20230309.csv")
omit_1 = "AF|ADHD|ASD|MX|DAMI|555_|5555"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13"]
DF = DF[DF['ID'].str.contains(omit_1) == False]
DF = DF[DF['ID'].isin(omit_2) == False]

DF['div_num'] = float('nan')
rs = {'RTs' : [],
      'ACCs' : []}

for i in range(100):
    print(i)
    df = DF.copy()
    for name, group in df.groupby(['ID', 'condition']):
        ID = group['ID'].unique()[0]
        condition = group['condition'].unique()[0]
        group['div_num'] = divide_trials(group)
        df.loc[(df['ID'] == ID) & (df['condition'] == condition)] = group
    one = df[df['div_num'] % 2 == 1]
    two = df[df['div_num'] % 2 == 0]
    tables = {'RTs' : {'one' : [],
                       'two' : []},
              'ACCs' : {'one' : [],
                        'two' : []}}
    for this in [(one, 'one'), (two, 'two')]:
        rts = this[0][this[0]['ACC'] == 1].groupby(['ID', 'condition']).agg({'RT' : "median"}).reset_index(
            drop = False
            ).pivot(
                index = 'ID',
                columns = 'condition',
                values = 'RT'
                ).reset_index(drop = False)
        rts['RT_score'] = rts['nonpred'] - rts['pred']
        tables['RTs'][this[1]] = rts
        accs = this[0].groupby(['ID', 'condition']).agg({'ACC' : "mean"}).reset_index(
            drop = False
            ).pivot(
                index = 'ID',
                columns = 'condition',
                values = 'ACC'
                ).reset_index(drop = False)
        accs['ACC_score'] = accs['pred'] - accs['nonpred']
        tables['ACCs'][this[1]] = accs
    RTs = tables['RTs']['one'].merge(tables['RTs']['two'],
                                     on = 'ID',
                                     how = 'outer')
    ACCs = tables['ACCs']['one'].merge(tables['ACCs']['two'],
                                       on = 'ID',
                                       how = 'outer')
    for t in [(RTs, 'RTs', 'RT_score'), (ACCs, 'ACCs', 'ACC_score')]:
        r = t[0][t[2] + "_x"].corr(t[0][t[2] + "_y"], method = 'pearson')
        rs[t[1]].append((2 * r) / (1 + r))

results = pd.DataFrame({'RTs' : rs['RTs'],
                        'ACCs' : rs['ACCs']})
results.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/predictive/data/predictive_reliability_split_half_iterations.csv",
               index = False)
