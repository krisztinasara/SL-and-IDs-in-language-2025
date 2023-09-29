# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:35:34 2023

@author: Kriszti
"""

import pandas as pd

RT = pd.read_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/Self_paced_reading/data/selfpaced_sentdiffs_RTs.csv")
ACC = pd.read_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/Self_paced_reading/data/selfpaced_sentdiffs_compr.csv")

RT_desc = RT.describe()
ACC_desc = ACC.describe()

raw = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/selfpaced_rawRTs_20220202.csv")
raw_desc = raw.groupby(['condition', 'type', 'sent_cat_ID']).agg({'question_resp.corr' : 'mean'})
