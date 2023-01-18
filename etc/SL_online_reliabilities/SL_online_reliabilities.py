# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:28:24 2023

@author: Kriszti
"""

import numpy as np
import pandas as pd
from sklearn import linear_model
from scipy.stats import t
from itertools import product

# 1. Functions

def divide_trials(len1, len2):
    if len1 != len2:
        x = np.random.choice([1, 2])
        if x == 1:
            lengroup1 = len1
            lengroup2 = len2
        elif x == 2:
            lengroup1 = len2
            lengroup2 = len1
    else:
        lengroup1 = len1
        lengroup2 = len2    
    div = [1] * lengroup1 + [2] * lengroup2
    np.random.shuffle(div)    
    return div

# 2. Procedure

corr_met = input("Correlation method: ")
if corr_met == "":
    corr_met = 'pearson'

SEGM_AL_child = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms/data/normRTs_SEGM_AL_children_online_20220215_FINAL_SAMPLE_dprime_filtered.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_2keys_450ms_letterID_online_20220924_dprime_filtered.csv"
         )
    ]
    )
SEGM_AL_adult = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_2keys_online_20220215_FINAL_SAMPLE.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_2key_300ms_letterID_online_20220922_dprime_filtered.csv"
         )
    ]
    )
SEGM_VN = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_DLD_1000ms/data/SEGM_VN_child_1000ms_online_20220923_FINAL_SAMPLE_dprime_filtered.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_2key_1000ms_letterID/data/SEGM_VN_2key_1000ms_letterID_online_20220923_dprime_filtered.csv"
         )
     ]
    )
AGL = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/all_online_processed_knowlton_agl_20220919.csv"
    )
NAD = pd.concat(    
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/normRTs_AGL_NAD_letterID_online_20220215.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/AGL_NAD_v2_letterID_online_20220222.csv"
         )
     ]
    )

AL_online_IDs = list(AL_online['ID'].unique())
AL_2AFC_IDs = list(AL_2AFC['ID'].unique())
VN_online_IDs = list(VN_online['ID'].unique())
VN_2AFC_IDs = list(VN_2AFC['ID'].unique())

online_columns = ['RT_1_3_diff', 'RT_4_3_diff', 'RT_4_5_diff',
                  'ACC_3_1_diff', 'ACC_3_4_diff', 'ACC_5_4_diff',
                  'RT_1_3_resid', 'RT_4_3_resid', 'RT_4_5_resid',
                  'ACC_3_1_resid', 'ACC_3_4_resid', 'ACC_5_4_resid'] 
offline_columns = ['overall', 'w_p', 'w_n', 'p_n']
corr_tables = {'AL': {}, 'VN': {}}
for mod in ['AL', 'VN']:
    for col in online_columns + offline_columns:
        corr_tables[mod][col] = pd.DataFrame()

iternum = 1000

# Online

online_tables = {}

for mod, source, IDs in [
        ("AL", AL_online, AL_online_IDs),
        ("VN", VN_online, VN_online_IDs),
        ]:
    online_tables[mod] = {}
    for i in range(iternum):
        online_tables[mod][i] = {}
        print('online', mod, i)
        online = source.copy()
        
        for ID in IDs:
            for block in [1, 2, 3, 4, 5]:
                online.loc[(online['ID'] == ID) & (online['block'] == block), 'div_num'] = divide_trials(len1 = 7, len2 = 8)
        
        online_one = online[online['div_num'] % 2 == 1]
        online_two = online[online['div_num'] % 2 == 0]
        
        online_one_wide = pd.DataFrame(columns = ['RT_1', 'RT_2', 'RT_3', 'RT_4', 'RT_5',
                                                  'ACC_1', 'ACC_2', 'ACC_3', 'ACC_4', 'ACC_5'])
        online_two_wide = pd.DataFrame(columns = ['RT_1', 'RT_2', 'RT_3', 'RT_4', 'RT_5',
                                                  'ACC_1', 'ACC_2', 'ACC_3', 'ACC_4', 'ACC_5'])
        for divided, target, one_two in [(online_one, online_one_wide, "one"),
                                         (online_two, online_two_wide, "two")]:
            for ID in IDs:

                this = divided[divided['ID'] == ID]
                for block in [1, 2, 3, 4, 5]:
                    target.loc[ID, 'RT_' + str(block)] = this[this['block'] == block]['RT'].median()
                    target.loc[ID, 'ACC_' + str(block)] = this[this['block'] == block]['ACC'].mean()
            target.fillna(target.mean(), inplace = True)    
            for measure_name, v1, v2 in [
                    ("RT_1_3_diff", 'RT_1', 'RT_3'),
                    ("RT_4_3_diff", 'RT_4', 'RT_3'),
                    ("RT_4_5_diff", 'RT_4', 'RT_5'),
                    ("ACC_3_1_diff", 'ACC_3', 'ACC_1'),
                    ("ACC_3_4_diff", 'ACC_3', 'ACC_4'),
                    ("ACC_5_4_diff", 'ACC_5', 'ACC_4')
                    ]:
                target[measure_name] = target[v1] - target[v2]
            
            for measure_name, v1, v2 in [
                    ("RT_1_3_resid", 'RT_1', 'RT_3'),
                    ("RT_4_3_resid", 'RT_4', 'RT_3'),
                    ("RT_4_5_resid", 'RT_4', 'RT_5'),
                    ("ACC_3_1_resid", 'ACC_3', 'ACC_1'),
                    ("ACC_3_4_resid", 'ACC_3', 'ACC_4'),
                    ("ACC_5_4_resid", 'ACC_5', 'ACC_4')
                    ]:
                try:
                    model = linear_model.LinearRegression().fit(target[[v1]], target[[v2]])
                    prediction = model.predict(target[[v1]])
                    target[measure_name] = target[[v2]] - prediction
                except:
                    pass
            target.index.names = ['ID']
            online_tables[mod][i][one_two] = target.astype(float)
        
for mod in ['AL', 'VN']:
    for i in range(len(online_tables[mod])):
        for col in online_columns:
            corr_tables[mod][col].loc[i, 'corrcoef_' + corr_met] = online_tables[mod][i]['one'][col].corr(online_tables[mod][i]['two'][col], method = corr_met)

# 2AFC

offline_tables = {}

for mod, source, IDs in [
        ("AL", AL_2AFC, AL_2AFC_IDs),
        ("VN", VN_2AFC, VN_2AFC_IDs),
        ]:
    offline_tables[mod] = {}
    for i in range(iternum):
        offline_tables[mod][i] = {}
        print("offline", mod, i)
        offline = source.copy()

        for ID in IDs:
            for contrast in ['w_p', 'w_n', 'p_n']:
                offline.loc[(offline['ID'] == ID) & (offline['contrast'] == contrast), 'div_num'] = divide_trials(len1 = 4, len2 = 4)
        
        offline_one = offline[offline['div_num'] % 2 == 1]
        offline_two = offline[offline['div_num'] % 2 == 0]
        
        offline_one_wide = pd.DataFrame(columns = ['overall', 'w_p', 'w_n', 'p_n'])
        offline_two_wide = pd.DataFrame(columns = ['overall', 'w_p', 'w_n', 'p_n'])
        for divided, target, one_two in [(offline_one, offline_one_wide, "one"),
                                         (offline_two, offline_two_wide, "two")]:
            for ID in IDs:

                this = divided[divided['ID'] == ID]
                target.loc[ID, 'overall'] = this['ACC'].mean()
                for contrast in ['w_p', 'w_n', 'p_n']:
                    target.loc[ID, contrast] = this[this['contrast'] == contrast]['ACC'].mean()
            
            target.index.names = ['ID']
            offline_tables[mod][i][one_two] = target.astype(float)

for mod in ['AL', 'VN']:
    for i in range(len(offline_tables[mod])):
        for col in offline_columns:
            corr_tables[mod][col].loc[i, 'corrcoef_' + corr_met] = offline_tables[mod][i]['one'][col].corr(offline_tables[mod][i]['two'][col], method = corr_met)

for mod in ['AL', 'VN']:
    for var in corr_tables[mod]:
        corr_tables[mod][var][
            'corrcoef_' + corr_met + '_spearman_brown_corrected'
            ] = (2 * corr_tables[mod][var]['corrcoef_' + corr_met]) / (1 + corr_tables[mod][var]['corrcoef_' + corr_met])

mods = ['AL', 'VN']
columns = online_columns + offline_columns
indices = list(product(mods, columns))
split_half_rel_SB_corr = pd.DataFrame(index = pd.MultiIndex.from_tuples(indices))
for mod in ['AL', 'VN']:
    for var in corr_tables[mod]:
        mean = corr_tables[mod][var]['corrcoef_' + corr_met + '_spearman_brown_corrected'].mean()
        std = corr_tables[mod][var]['corrcoef_' + corr_met + '_spearman_brown_corrected'].std()
        length = len(corr_tables[mod][var]['corrcoef_' + corr_met + '_spearman_brown_corrected'])
        dof = length - 1
        conf = 0.95
        t_crit = np.abs(t.ppf((1 - conf) / 2, dof))
        CI_lower = mean - std * t_crit / np.sqrt(length)
        CI_upper = mean + std * t_crit / np.sqrt(length)
        split_half_rel_SB_corr.loc[(mod, var), 'CI_lower'] = CI_lower
        split_half_rel_SB_corr.loc[(mod, var), 'mean'] = mean
        split_half_rel_SB_corr.loc[(mod, var), 'CI_upper'] = CI_upper

split_half_rel_SB_corr.to_excel("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_VN_DYSLEXIA/results/split_half_rel_SB_corr.xlsx")
