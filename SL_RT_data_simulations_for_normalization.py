# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:28:29 2022

@author: Kriszti
"""

import pandas as pd
import numpy as np
import seaborn as sns

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

# 2. Procedure

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

for subject in ['s1', 's2', 's3', 's4', 's5', 's6']:
    for block in ['TRN1', 'TRN2', 'TRN3', 'RND4', 'REC5']:
        these_RTs = list_RTs(
            mean = RTs[subject][block]['mean'],
            SD = RTs[subject][block]['SD'],
            num = size)
        data = pd.concat([data,
                          pd.DataFrame(
                              {
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
