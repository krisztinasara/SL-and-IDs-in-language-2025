# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:28:24 2023

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

def extract_block_data(df, var, method):
    df = pd.pivot_table(df[['ID', 'block', var]].groupby(['ID', 'block']).agg(
        {var : method}
        ).reset_index(),
        values = var,
        index = 'ID',
        columns = ['block']
        )
    return df

# 2. Procedure

corr_met = input("Correlation method: ")
if corr_met == "":
    corr_met = 'pearson'

omit_1 = "AF|ADHD|ASD|MX|DAMI|555_|5555"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13"]

SEGM_AL_child = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms/data/SEGM_AL_child_450ms_pm_online_20230130.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_child_450ms_letterID_pm_online_20230130.csv"
         )
    ]
    )
SEGM_AL_child = SEGM_AL_child[SEGM_AL_child['type'] == "stream"]
SEGM_AL_child = SEGM_AL_child[SEGM_AL_child['ID'].str.contains(omit_1) == False]
SEGM_AL_child = SEGM_AL_child[SEGM_AL_child['ID'].isin(omit_2) == False]

SEGM_AL_adult = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_online_20230129_FINAL_SAMPLE.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_AL_YA_2key_300ms_letterID_online_20230129.csv"
         )
    ]
    )
SEGM_AL_adult = SEGM_AL_adult[SEGM_AL_adult['type'] == "stream"]
SEGM_AL_adult = SEGM_AL_adult[SEGM_AL_adult['ID'].str.contains(omit_1) == False]
SEGM_AL_adult = SEGM_AL_adult[SEGM_AL_adult['ID'].isin(omit_2) == False]

SEGM_VN = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_DLD_1000ms/data/SEGM_VN_child_1000ms_online_pm_20220923.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_2key_1000ms_letterID/data/SEGM_VN_2key_1000ms_letterID_online_pm_20230130.csv"
         )
     ]
    )
SEGM_VN = SEGM_VN[SEGM_VN['type'] == "stream"]
SEGM_VN = SEGM_VN[SEGM_VN['ID'].str.contains(omit_1) == False]
SEGM_VN = SEGM_VN[SEGM_VN['ID'].isin(omit_2) == False]

AGL = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/AGL_KS_mod4_pm_online_20230129.csv"
    )
AGL = AGL[AGL['ID'].str.contains(omit_1) == False]
AGL = AGL[AGL['ID'].isin(omit_2) == False]

NAD = pd.concat(    
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/AGL_NAD_letterID_online_pm.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/NAD_v2_letterID_online_pm_20230128.csv"
         )
     ]
    )
NAD = NAD[NAD['ID'].str.contains(omit_1) == False]
NAD = NAD[NAD['ID'].isin(omit_2) == False]

SEGM_AL_adult_IDs = list(SEGM_AL_adult['ID'].unique())
SEGM_AL_child_IDs = list(SEGM_AL_child['ID'].unique())
SEGM_VN_IDs = list(SEGM_VN['ID'].unique())
AGL_IDs = list(AGL['ID'].unique())
NAD_IDs = list(NAD['ID'].unique())

blocks = {
    'SEGM_AL_adult': {'train_first': 'TRN1',
                      'train_last': 'TRN3',
                      'rnd': 'RND4',
                      'rec': 'REC5'},
    'SEGM_AL_child': {'train_first': 'TRN1',
                      'train_last': 'TRN3',
                      'rnd': 'RND4',
                      'rec': 'REC5'},
    'SEGM_VN': {'train_first': 'TRN1',
                'train_last': 'TRN3',
                'rnd': 'RND4',
                'rec': 'REC5'},
    'AGL': {'train_first': 'BLOCK1',
            'train_last': 'BLOCK3',
            'rnd': 'BLOCK4',
            'rec': 'BLOCK5'},
    'NAD': {'train_first': 'TRN1',
            'train_last': 'TRN4',
            'rnd': 'RND5',
            'rec': 'REC6'}}

rs = {'SEGM_AL_adult': {'RT_trn': [],
                        'RT_trn_rnd': [],
                        'RT_rnd_rec': [],
                        'ACC_trn': [],
                        'ACC_trn_rnd': [],
                        'ACC_rnd_rec': []},
      'SEGM_AL_child': {'RT_trn': [],
                        'RT_trn_rnd': [],
                        'RT_rnd_rec': [],
                        'ACC_trn': [],
                        'ACC_trn_rnd': [],
                        'ACC_rnd_rec': []},
      'SEGM_VN': {'RT_trn': [],
                  'RT_trn_rnd': [],
                  'RT_rnd_rec': [],
                  'ACC_trn': [],
                  'ACC_trn_rnd': [],
                  'ACC_rnd_rec': []},
      'AGL': {'RT_trn': [],
              'RT_trn_rnd': [],
              'RT_rnd_rec': [],
              'ACC_trn': [],
              'ACC_trn_rnd': [],
              'ACC_rnd_rec': []},
      'NAD': {'RT_trn': [],
              'RT_trn_rnd': [],
              'RT_rnd_rec': [],
              'ACC_trn': [],
              'ACC_trn_rnd': [],
              'ACC_rnd_rec': []}
      }

iternum = 100

for dtls in [(SEGM_AL_adult, SEGM_AL_adult_IDs, 'SEGM_AL_adult', 'syl'),
             (SEGM_AL_child, SEGM_AL_child_IDs, 'SEGM_AL_child', 'syl'),
             (SEGM_VN, SEGM_VN_IDs, 'SEGM_VN', 'img'),
             (AGL, AGL_IDs, 'AGL', 'syl'),
             (NAD, NAD_IDs, 'NAD', 'w')]:
    IDs = dtls[1]
    task = dtls[2]
    item = dtls[3]
    train_first = blocks[task]['train_first']
    train_last = blocks[task]['train_last']
    rnd = blocks[task]['rnd']
    rec = blocks[task]['rec']
    
    for i in range(iternum):
        print(i, task)
        df = dtls[0].copy()
        df = df[df[item] == df['target']]
        
        for ID in IDs:
            for block in df['block'].unique():
                df.loc[(df['ID'] == ID) & (df['block'] == block), 'div_num'] = divide_trials(df[(df['ID'] == ID) & (df['block'] == block)])
        
        one = df[df['div_num'] % 2 == 1]
        two = df[df['div_num'] % 2 == 0]
        
        one_RTs = extract_block_data(one[one['ACC'] == 1], 'RT', 'median')
        one_RTs['trn'] = one_RTs[train_first] - one_RTs[train_last]
        one_RTs['trn_rnd'] = one_RTs[rnd] - one_RTs[train_last]
        one_RTs['rnd_rec'] = one_RTs[rnd] - one_RTs[rec]
        one_ACCs = extract_block_data(one, 'ACC', 'mean')
        one_ACCs['trn'] = one_ACCs[train_last] - one_ACCs[train_first]
        one_ACCs['trn_rnd'] = one_ACCs[train_last] - one_ACCs[rnd]
        one_ACCs['rnd_rec'] = one_ACCs[rec] - one_ACCs[rnd]
        
        two_RTs = extract_block_data(two[two['ACC'] == 1], 'RT', 'median')
        two_RTs['trn'] = two_RTs[train_first] - two_RTs[train_last]
        two_RTs['trn_rnd'] = two_RTs[rnd] - two_RTs[train_last]
        two_RTs['rnd_rec'] = two_RTs[rnd] - two_RTs[rec]
        two_ACCs = extract_block_data(two, 'ACC', 'mean')
        two_ACCs['trn'] = two_ACCs[train_last] - two_ACCs[train_first]
        two_ACCs['trn_rnd'] = two_ACCs[train_last] - two_ACCs[rnd]
        two_ACCs['rnd_rec'] = two_ACCs[rec] - two_ACCs[rnd]
        
        RTs = one_RTs.join(two_RTs, how = "outer",
                           lsuffix = "_one", rsuffix = "_two")
        ACCs = one_ACCs.join(two_ACCs, how = "outer",
                             lsuffix = "_one", rsuffix = "_two")
        
        for index in ['trn', 'trn_rnd', 'rnd_rec']:
            RT_r = RTs[index + '_one'].corr(RTs[index + '_two'], method = 'pearson')
            rs[task]['RT_' + index].append((2 * RT_r) / (1 + RT_r))
            ACC_r = ACCs[index + '_one'].corr(ACCs[index + '_two'], method = 'pearson')
            rs[task]['ACC_' + index].append((2 * ACC_r) / (1 + ACC_r))
    
results = pd.DataFrame()
for task in rs:
    for index in rs[task]:
        results.loc[task, index] = mean(rs[task][index])

results.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/SL_online_reliabilities.csv")

# Composite scores

# =============================================================================
# blocks = {
#     'SEGM_AL_adult': {'train_first': 'TRN1',
#                       'train_last': 'TRN3',
#                       'rnd': 'RND4',
#                       'rec': 'REC5'},
#     'SEGM_AL_child': {'train_first': 'TRN1',
#                       'train_last': 'TRN3',
#                       'rnd': 'RND4',
#                       'rec': 'REC5'},
#     'SEGM_VN': {'train_first': 'TRN1',
#                 'train_last': 'TRN3',
#                 'rnd': 'RND4',
#                 'rec': 'REC5'},
#     'AGL': {'train_first': 'BLOCK1',
#             'train_last': 'BLOCK3',
#             'rnd': 'BLOCK4',
#             'rec': 'BLOCK5'},
#     'NAD': {'train_first': 'TRN1',
#             'train_last': 'TRN4',
#             'rnd': 'RND5',
#             'rec': 'REC6'}}
# 
# rs = {'SEGM_AL_adult': {'RT_diff': [],
#                         'ACC_diff': []},
#       'SEGM_AL_child': {'RT_diff': [],
#                         'ACC_diff': []},
#       'SEGM_VN': {'RT_diff': [],
#                   'ACC_diff': []},
#       'AGL': {'RT_diff': [],
#               'ACC_diff': []},
#       'NAD': {'RT_diff': [],
#               'ACC_diff': []}}
# 
# iternum = 100
# 
# for dtls in [(SEGM_AL_adult, SEGM_AL_adult_IDs, 'SEGM_AL_adult', 'syl'),
#              (SEGM_AL_child, SEGM_AL_child_IDs, 'SEGM_AL_child', 'syl'),
#              (SEGM_VN, SEGM_VN_IDs, 'SEGM_VN', 'img'),
#              (AGL, AGL_IDs, 'AGL', 'syl'),
#              (NAD, NAD_IDs, 'NAD', 'w')]:
#     IDs = dtls[1]
#     task = dtls[2]
#     item = dtls[3]
#     train_last = blocks[task]['train_last']
#     rnd = blocks[task]['rnd']
#     rec = blocks[task]['rec']
#     
#     for i in range(iternum):
#         print(i, task)
#         df = dtls[0].copy()
#         df = df[df[item] == df['target']]
#         
#         for ID in IDs:
#             for block in df['block'].unique():
#                 df.loc[(df['ID'] == ID) & (df['block'] == block), 'div_num'] = divide_trials(df[(df['ID'] == ID) & (df['block'] == block)])
#         
#         one = df[df['div_num'] % 2 == 1]
#         two = df[df['div_num'] % 2 == 0]
#         
#         one_RTs = extract_block_data(one, 'RT', 'median')
#         one_RTs['diff'] = ((one_RTs[rnd] - one_RTs[train_last]) + (one_RTs[rnd] - one_RTs[rec])) / 2
#         one_ACCs = extract_block_data(one, 'ACC', 'mean')
#         one_ACCs['diff'] = ((one_ACCs[train_last] - one_ACCs[rnd]) + (one_ACCs[rec] - one_ACCs[rnd])) / 2
#         
#         two_RTs = extract_block_data(two, 'RT', 'median')
#         two_RTs['diff'] = ((two_RTs[rnd] - two_RTs[train_last]) + (two_RTs[rnd] - two_RTs[rec])) / 2
#         two_ACCs = extract_block_data(two, 'ACC', 'mean')
#         two_ACCs['diff'] = ((two_ACCs[train_last] - two_ACCs[rnd]) + (two_ACCs[rec] - two_ACCs[rnd])) / 2
#         
#         RTs = one_RTs.join(two_RTs, how = "outer",
#                            lsuffix = "_one", rsuffix = "_two")
#         ACCs = one_ACCs.join(two_ACCs, how = "outer",
#                              lsuffix = "_one", rsuffix = "_two")
#         
#         for index in ['diff']:
#             RT_r = RTs[index + '_one'].corr(RTs[index + '_two'], method = 'pearson')
#             rs[task]['RT_' + index].append((2 * RT_r) / (1 + RT_r))
#             ACC_r = ACCs[index + '_one'].corr(ACCs[index + '_two'], method = 'pearson')
#             rs[task]['ACC_' + index].append((2 * ACC_r) / (1 + ACC_r))
#     
# results = pd.DataFrame()
# for task in rs:
#     for index in rs[task]:
#         results.loc[task, index] = mean(rs[task][index])
# 
# results.to_excel("C:/Users/Kriszti/GitHub/lendulet_language_SL/etc/SL_online_reliabilities/SL_online_reliabilities_diff_composite_scores.xlsx")
# =============================================================================

