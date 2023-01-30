# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:17:43 2023

@author: Kriszti
"""

import pandas as pd

# SEGM_AL_child

SEGM_AL_child_2AFC = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms/data/SEGM_AL_child_450ms_pm_2AFC_20230130_long.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_child_450ms_letterID_pm_2AFC_20230130_long.csv"
         )
    ]
    )

SEGM_AL_child_prod = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms/data/SEGM_AL_child_450ms_pm_prod_20230130_long.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_child_450ms_letterID_pm_prod_20230130_long.csv"
         )
    ]
    )

SEGM_AL_child_2AFC_pivot = SEGM_AL_child_2AFC.pivot(
    index = 'ID',
    columns = ['seq_length_2AFC', 'contrast_group', 'trials_2AFC.thisIndex'],
    values = '2AFC_acc'
    )

SEGM_AL_child_prod_pivot = SEGM_AL_child_prod.pivot(
    index = 'ID',
    columns = 'trials_prod.thisIndex',
    values = 'prod_acc'
    )

SEGM_AL_child_2AFC_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_online_AL_child_450ms_letterID/data/SEGM_AL_child_2AFC_wide.csv"
    )
SEGM_AL_child_prod_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_online_AL_child_450ms_letterID/data/SEGM_AL_child_prod_wide.csv"
    )

# SEGM_AL_adult

SEGM_AL_adult_2AFC = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_2AFC_20230129_FINAL_SAMPLE.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_AL_YA_2key_300ms_letterID_2AFC_20230129.csv"
         )
    ]
    )

SEGM_AL_adult_prod = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_prod_20230129_FINAL_SAMPLE.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_AL_YA_2key_300ms_letterID_prod_20230129.csv"
         )
    ]
    )

SEGM_AL_adult_2AFC_pivot = SEGM_AL_adult_2AFC.pivot(
    index = 'ID',
    columns = ['seq_length_2AFC', 'contrast_group', 'trials_2AFC.thisIndex'],
    values = '2AFC_acc'
    )

SEGM_AL_adult_prod_pivot = SEGM_AL_adult_prod.pivot(
    index = 'ID',
    columns = 'trials_prod.thisIndex',
    values = 'prod_acc'
    )

SEGM_AL_adult_2AFC_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_AL_adult_300ms_2key/data/SEGM_AL_adult_2AFC_wide.csv"
    )
SEGM_AL_adult_prod_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_AL_adult_300ms_2key/data/SEGM_AL_adult_prod_wide.csv"
    )

# SEGM_VN

SEGM_VN_2AFC = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_DLD_1000ms/data/SEGM_VN_child_1000ms_2AFC_pm_20220923_long.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_2key_1000ms_letterID/data/SEGM_VN_2key_1000ms_letterID_2AFC_pm_20230130.csv"
         )
     ]
    )

SEGM_VN_prod = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_DLD_1000ms/data/SEGM_VN_child_1000ms_prod_pm_20220923_long.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_2key_1000ms_letterID/data/SEGM_VN_2key_1000ms_letterID_prod_pm_20230130.csv"
         )
     ]
    )

SEGM_VN_2AFC_pivot = SEGM_VN_2AFC.pivot(
    index = 'ID',
    columns = ['seq_length_2AFC', 'contrast_group', 'trials_2AFC.thisIndex'],
    values = '2AFC_acc'
    )

SEGM_VN_prod_pivot = SEGM_VN_prod.pivot(
    index = 'ID',
    columns = 'trials_prod.thisIndex',
    values = 'prod_acc'
    )

SEGM_VN_2AFC_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_VN_2key_1000ms/data/SEGM_VN_2AFC_wide.csv"
    )
SEGM_VN_prod_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/SEGM_VN_2key_1000ms/data/SEGM_VN_prod_wide.csv"
    )

# AGL

AGL_2AFC = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/AGL_KS_mod4_pm_2AFC_20230129_long.csv"
    )

AGL_prod = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/AGL_KS_mod4_pm_prod_20230129_long.csv"
    )

AGL_2AFC_pivot = AGL_2AFC.pivot(
    index = 'ID',
    columns = ['Trial_type', 'forced_choice_trials.thisIndex'],
    values = 'choice_resp.corr'
    )

AGL_prod_pivot = AGL_prod.pivot(
    index = 'ID',
    columns = 'production_trials.thisIndex',
    values = 'production_resp.corr'
    )

AGL_2AFC_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/AGL_KS_mod4/data/AGL_KS_mod4_2AFC_wide.csv"
    )
AGL_prod_pivot.to_csv(
    "C:/Users/Kriszti/GitHub/lendulet_language_SL/task_data/AGL_KS_mod4/data/AGL_KS_mod4_prod_wide.csv"
    )


# NAD - later!!!

NAD_2AFC = pd.concat(    
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/NAD_letterID_2AFC_pm_20230128.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/NAD_v2_letterID_2AFC_pm_20230128_long.csv"
         )
     ]
    )

NAD_prod = pd.concat(    
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/NAD_letterID_prod_pm_20230128.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/NAD_v2_letterID_prod_pm_20230128_long.csv"
         )
     ]
    )

NAD_2AFC_pivot = NAD_2AFC.pivot()

NAD_prod_pivot = NAD_prod.pivot()
