# -*- coding: utf-8 -*-
"""
author: krisztinasara
date: 20231101
This code creates wide dataframes for calculating reliabilities in JASP.
"""

import pandas as pd

include = list(pd.read_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/only_SEM_data/include_IDs.csv")['ID'])

SEGM_trigram = pd.concat(
    [
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_2key_letterID_2AFC_20230427.csv"),
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_2AFC_20230129_FINAL_SAMPLE.csv")
     ]
    )
SEGM_trigram['ID'] = SEGM_trigram['ID'].astype(str)
SEGM_trigram = SEGM_trigram[
    (SEGM_trigram['seq_length_2AFC'] == "trigram")
    &
    (SEGM_trigram['ID'].isin(include))
    ].pivot(
    index = 'ID', columns = 'trials_2AFC.thisIndex', values = '2AFC_acc'
    )

SEGM_prod = pd.concat(
    [
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_2key_letterID_prod_20230427.csv"),
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_prod_20230129_FINAL_SAMPLE.csv")
     ]
    )
SEGM_prod['ID'] = SEGM_prod['ID'].astype(str)
SEGM_prod = SEGM_prod[
    SEGM_prod['ID'].isin(include)
    ].pivot(
    index = 'ID', columns = 'trials_prod.thisIndex', values = 'prod_acc'
    )

AGL_phr = pd.concat(
    [
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/after_20220822/AGL_KS_mod4_2AFC_knowlton_agl_20230601.csv"),
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/before_20220822/AGL_KS_mod4_pm_2AFC_20230129_long.csv")
    ]
    )
AGL_phr['ID'] = AGL_phr['ID'].astype(str)
AGL_phr = AGL_phr[
    (AGL_phr['Trial_type'] == 'phrase')
    &
    (AGL_phr['ID'].isin(include))
    ].pivot(
    index = 'ID', columns = 'forced_choice_trials.thisIndex', values = 'choice_resp.corr'
    )

AGL_sent = pd.concat(
    [
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/after_20220822/AGL_KS_mod4_2AFC_knowlton_agl_20230601.csv"),
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/before_20220822/AGL_KS_mod4_pm_2AFC_20230129_long.csv")
    ]
    )
AGL_sent['ID'] = AGL_sent['ID'].astype(str)
AGL_sent = AGL_sent[
    (AGL_sent['Trial_type'] == 'string')
    &
    (AGL_sent['ID'].isin(include))
    ].pivot(
        index = 'ID', columns = 'forced_choice_trials.thisIndex', values = 'choice_resp.corr'
        )

AGL_prod = pd.concat(
    [
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/after_20220822/AGL_KS_mod4_prod_knowlton_agl_20230601.csv"),
    pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/before_20220822/AGL_KS_mod4_pm_prod_20230129_long.csv")
    ]
    )
AGL_prod['ID'] = AGL_prod['ID'].astype(str)
AGL_prod = AGL_prod[
    AGL_prod['ID'].isin(include)
    ].pivot(
        index = 'ID', columns = 'production_trials.thisIndex', values = 'production_resp.corr'
        )

MENYET = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_MENYET/data/MENYET_by_trial_20230428.csv")
MENYET['ID'] = MENYET['ID'].astype(str)
MENYET = MENYET[
    (MENYET['ID'].isin(include))
    &
    (MENYET['trial'].isin([2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 16, 17]))
    ].pivot(
        index = 'ID', columns = 'trial', values = 'ACC'
        )

TROG = pd.concat(
    [
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_trog_javitott/data/trog_by_trial_20230425.csv"),
     pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Adult_trog/data/trog_by_trial_20230425.csv")
     ]
    )
TROG['ID'] = TROG['ID'].astype(str)
TROG = TROG[
    (TROG['ID'].isin(include))
    &
    (TROG['condition'] == "pragm")
    ].pivot(
        index = 'ID', columns = 'trial', values = 'ACC'
        )

read_GP = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/selfpaced_sentdiffs_target_20231014.csv")
read_GP['ID'] = read_GP['ID'].astype(str).str.replace(".0", "", regex = False)
read_GP = read_GP[
    (read_GP['ID'].isin(include))
    &
    (read_GP['type'] == "GP")
    ].pivot(
        index = 'ID', columns = 'sent_cat_ID', values = 'target_RT_diff'
        )

read_sertes = pd.read_csv("C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/selfpaced_sentdiffs_target_20231014.csv")
read_sertes['ID'] = read_sertes['ID'].astype(str).str.replace(".0", "", regex = False)
read_sertes = read_sertes[
    (read_sertes['ID'].isin(include))
    &
    (read_sertes['agg_type'] == "sertes") &
    (((read_sertes['type'] == "morf") & (read_sertes['sent_cat_ID'] == 2)) == False)
    ].pivot(
        index = 'ID', columns = ['sent_cat_ID', 'type'], values = 'target_RT_diff'
        )

AGL_phr.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/AGL_2AFC_phr.csv")
AGL_prod.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/AGL_prod.csv")
AGL_sent.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/AGL_2AFC_sent.csv")
MENYET.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/MENYET.csv")
read_GP.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/selfpaced_target_RT_diff_GP.csv")
read_sertes.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/selfpaced_target_RT_diff_sertes.csv")
SEGM_prod.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/SEGM_AL_SEGM_prod_data.csv")
SEGM_trigram.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/SEGM_AL_2AFC_trigram.csv")
TROG.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/reliability_testing/task_dataframes/TROG.csv")
