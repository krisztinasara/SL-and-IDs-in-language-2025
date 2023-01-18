# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:28:29 2022

@author: Kriszti
"""

import pandas as pd
import numpy as np
import seaborn as sns
from random import sample

# 1. Functions

def list_RTs(mean, SD, num):
    RTs = list(
        map(int,
            list(
                np.around(
                    np.random.normal(
                        # mean of distribution
                        loc = mean,
                        # SD of distribution
                        scale = SD,
                        # number of generated numbers
                        size = num
                        )
                    )
                )
            )
        )
    return RTs

def normalize(numbers):
    normalized = (numbers - min(numbers)) / (max(numbers) - min(numbers))
    return normalized

def training_RT_score(TRN_first, TRN_last):
    score = TRN_first - TRN_last
    return score

def difference_RT_score(TRN_last, RND, REC):
    score = ((RND - TRN_last) + (RND - REC)) / 2
    return score

def select_random_IDs(table, subj_var_name, num):
    IDs = [x for x in list(table[subj_var_name].unique()) if x != float('nan')]
    sampled_IDs = sample(IDs, num)
    sampled_table = table[table[subj_var_name].isin(sampled_IDs)]
    return sampled_table

# 2. Procedure

# 2.1. Modeling participants

# Simulated participants
RTs = {
       # high baseline RTs with steep learning curve
       's1': {
          'TRN1': {
              'mean': 600,
              'SD': 50
              },
          'TRN2': {
              'mean': 400,
              'SD': 50
              },
          'TRN3': {
              'mean': 200,
              'SD': 50
              },
          'RND4': {
              'mean': 700,
              'SD': 50
              },
          'REC5': {
              'mean': 200,
              'SD': 50
              }
           },
       # high baseline RTs with moderate smooth/moderate learning curve
       's2': {
          'TRN1': {
              'mean': 650,
              'SD': 50
              },
          'TRN2': {
              'mean': 600,
              'SD': 50
              },
          'TRN3': {
              'mean': 550,
              'SD': 50
              },
          'RND4': {
              'mean': 700,
              'SD': 50
              },
          'REC5': {
              'mean': 550,
              'SD': 50
              }
           },
       # low achieved RTs with smooth/moderate learning curve
       's3': {
          'TRN1': {
              'mean': 300,
              'SD': 50
              },
          'TRN2': {
              'mean': 250,
              'SD': 50
              },
          'TRN3': {
              'mean': 200,
              'SD': 50
              },
          'RND4': {
              'mean': 350,
              'SD': 50
              },
          'REC5': {
              'mean': 200,
              'SD': 50
              }
           },
       # low baseline RTs with steep learning curve
       's4': {
          'TRN1': {
              'mean': 400,
              'SD': 50
              },
          'TRN2': {
              'mean': 200,
              'SD': 50
              },
          'TRN3': {
              'mean': 0,
              'SD': 50
              },
          'RND4': {
              'mean': 500,
              'SD': 50
              },
          'REC5': {
              'mean': 0,
              'SD': 50
              }
           },
       # low baseline RTs with smooth/moderate learning curve
       's5': {
          'TRN1': {
              'mean': 450,
              'SD': 50
              },
          'TRN2': {
              'mean': 400,
              'SD': 50
              },
          'TRN3': {
              'mean': 350,
              'SD': 50
              },
          'RND4': {
              'mean': 500,
              'SD': 50
              },
          'REC5': {
              'mean': 350,
              'SD': 50
              }
           },
       # low baseline RTs with smooth/moderate learning curve
       's6': {
          'TRN1': {
              'mean': 100,
              'SD': 50
              },
          'TRN2': {
              'mean': 50,
              'SD': 50
              },
          'TRN3': {
              'mean': 0,
              'SD': 50
              },
          'RND4': {
              'mean': 150,
              'SD': 50
              },
          'REC5': {
              'mean': 0,
              'SD': 50
              }
           }
       }

data = pd.DataFrame()

size = 15
iters = 100

for it in range(iters):
    for subject in ['s1', 's2', 's3', 's4', 's5', 's6']:
        for block in ['TRN1', 'TRN2', 'TRN3', 'RND4', 'REC5']:
            these_RTs = list_RTs(
                mean = RTs[subject][block]['mean'],
                SD = RTs[subject][block]['SD'],
                num = size)
            data = pd.concat([data,
                              pd.DataFrame(
                                  {
                                      'iter': it,
                                      'subject': size * [subject],
                                      'block': size * [block],
                                      'RT': these_RTs,
                                      'norm_RT': size * float('nan')
                                      }
                                  )
                              ]
                             )
        data.loc[data['subject'] == subject, 'norm_RT'] = normalize(data.loc[data['subject'] == subject, 'RT'])

# block should be factor
data['block'] = data['block'].astype('category').cat.reorder_categories(
    ['TRN1', 'TRN2', 'TRN3', 'RND4', 'REC5']
    )

# BTW how would it have been done with map???

# Clear up unnecessary variables
del block, subject, these_RTs

# Plotting
data_grouped = data.groupby(
    ['iter', 'subject', 'block']
    ).agg(
        {
            'RT': 'median',
            'norm_RT': 'median'
            }
        ).groupby(
            ['subject', 'block']
            ).agg(
            {
                'RT': 'median',
                'norm_RT': 'median'
                }
            ).reset_index(
            drop = False
            )
for subject in ['s1', 's2', 's3', 's4', 's5', 's6']:
    data_grouped.loc[data_grouped['subject'] == subject, 'RT_train'] = training_RT_score(
        TRN_first = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN1')
            ]['RT']),
        TRN_last = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN3')
            ]['RT'])
            )
    data_grouped.loc[data_grouped['subject'] == subject, 'norm_RT_train'] = training_RT_score(
        TRN_first = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN1')
            ]['norm_RT']),
        TRN_last = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN3')
            ]['norm_RT'])
            )
    data_grouped.loc[data_grouped['subject'] == subject, 'RT_diff'] = difference_RT_score(
        TRN_last = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN3')
            ]['RT']),
        RND = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'RND4')
            ]['RT']),
        REC = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'REC5')
            ]['RT'])
            )
    data_grouped.loc[data_grouped['subject'] == subject, 'norm_RT_diff'] = difference_RT_score(
        TRN_last = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'TRN3')
            ]['norm_RT']),
        RND = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'RND4')
            ]['norm_RT']),
        REC = float(data_grouped.loc[
            (data_grouped['subject'] == subject) & (data_grouped['block'] == 'REC5')
            ]['norm_RT'])
            )

g = sns.FacetGrid(data_grouped, col = 'subject')
g.map(sns.lineplot,
      'block',
      'RT')

g = sns.FacetGrid(data_grouped, col = 'subject')
g.map(sns.lineplot,
      'block',
      'norm_RT')

# Gathering indexes from aggregated data
data_indices = data_grouped.pivot(
    index = 'subject',
    columns = 'block',
    values = ['RT', 'norm_RT']
    ).merge(data_grouped.groupby(
        ['subject']
        ).agg(
            {
                'RT_train': 'mean',
                'norm_RT_train': 'mean',
                'RT_diff': 'mean',
                'norm_RT_diff': 'mean'
                }
            ),
            how = "left",
            on = 'subject'
    )

# Write data
data_indices.to_excel(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/AGL_KS_mod4/data/RT_indices.xlsx"
    )

# Conclusion of the data:
# normalizing RTs only magnifies learning effects in the case of steeper learning curves,
# completely ignoring baseline reaction times. This is only good if it is a typical
# scenario that subject with steep learning curves tend to have high baseline RTs (s4)
# while subjects with smooth/moderate learning curves have low baseline RTs (s6). But how
# actual data look like in 1) different SL tasks and 2) different subjects?

# 2.2. Plotting of randomly chosen individual data for visual inspection

# Importing data
NAD = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/normRTs_AGL_NAD_letterID_online_20220215.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/AGL_NAD_v2_letterID_online_20220511.csv"
         )
     ]
    ).reset_index(
        drop = True
        )
AGL = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/AGL_KS_mod4_online_processed_knowlton_20220926.csv"
    )
SEGM = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_2key_300ms_letterID_online_20220922_dprime_filtered.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_2keys_450ms_letterID_online_20220924_dprime_filtered.csv"
         )
     ]
    ).reset_index(
        drop = True
        )

# Plotting
for task in [(SEGM, 'word segmentation'), (AGL, 'AGL'), (NAD, 'NAD')]:
    df = select_random_IDs(task[0], 'ID', 60)
    g = sns.FacetGrid(df, col = 'ID', col_wrap = 10)
    g.map(sns.lineplot, 'block', 'RT', ci = None)
    g.fig.suptitle(task[1])