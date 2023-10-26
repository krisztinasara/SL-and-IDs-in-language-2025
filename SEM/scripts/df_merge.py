# -*- coding: utf-8 -*-
"""
author: krisztinasara
date: 20230425
title: read dataframes for SEM
"""

import pandas as pd

# read individual dataframes

# =============================================================================
# PROC_SPEED
# vis_RT_med
# ac_RT_med
# vis_dec_RT_med
# ac_dec_RT_med
# =============================================================================
PROC_SPEED = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_YA/data/PROC_SPEED_YA_20231026.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/PROC_SPEED_v2_20231026.csv"
         )
     ]
    )[
      ['ID', 'vis_RT_med', 'ac_RT_med', 'vis_dec_RT_med', 'ac_dec_RT_med']
      ]

# =============================================================================
# digit_span
# =============================================================================
digit_span = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_DigitSpan/data/DigitSpan_20230320.csv"
    )[
      ['ID', 'forward_span', 'backward_span']
      ]

# =============================================================================
# n_back
# nback_1_dprime
# nback_2_dprime
# nback_3_dprime
# =============================================================================
n_back = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Verbal_n_back/data/Verbal_n_back_wide_20230310.csv"
    )[
      ['ID', 'nback_1_dprime', 'nback_2_dprime', 'nback_3_dprime']
      ]

# =============================================================================
# simon
# RT_score
# ACC_score
# =============================================================================
simon = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Simon_nyilas/data/Simon_nyilas_wide_20230307.csv"
    )[
      ['ID', 'RT_score', 'ACC_score']
      ]

# =============================================================================
# stroop
# RT_score
# ACC_score
# =============================================================================
stroop = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_stroop/data/stroop_wide_20230428.csv"
    )[
      ['ID', 'RT_score', 'ACC_score']
      ]

# =============================================================================
# SEGM_AL_adult (SEGM_AL_adult_300ms_2key)
# median RT training
# median RT TRN-RND
# median RT RND-REC
# ACC training
# ACC TRN-RND
# ACC RND-REC
# 2AFC bigram
# 2AFC trigram
# production
# =============================================================================
SEGM_AL_adult = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_YA_2key/data/SEGM_AL_AL_2key_wide_20230129_FINAL_SAMPLE.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2key_300ms_letterID/data/SEGM_AL_2key_letterID_wide_20230427.csv"
         )
     ]
    )[
      ['ID', 'version',
       'medRT_train', 'medRT_TRN3_RND4', 'medRT_RND4_REC5',
       'ACC_train', 'ACC_TRN3_RND4', 'ACC_RND4_REC5',
       '2AFC_bigram', '2AFC_trigram', 'SEGM_prod_data']
      ]
SEGM_AL_adult['version'] = "adult"

# =============================================================================
# SEGM_AL_child (SEGM_online_AL_2keys_child_450ms)
# median RT training
# median RT TRN-RND
# median RT RND-REC
# ACC training
# ACC TRN-RND
# ACC RND-REC
# 2AFC bigram
# 2AFC trigram
# production
# =============================================================================
SEGM_AL_child = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms/data/normRTs_SEGM_AL_children_wide_20220215_FINAL_SAMPLE_dprime_filtered.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_AL_2keys_child_450ms_letterID/data/SEGM_AL_2keys_letterID_wide_20230428.csv"
         )
     ]
    )[
      ['ID', 'version',
       'medRT_train', 'medRT_TRN3_RND4', 'medRT_RND4_REC5',
       'ACC_train', 'ACC_TRN3_RND4', 'ACC_RND4_REC5',
       '2AFC_bigram', '2AFC_trigram', 'SEGM_prod_data']
      ]
SEGM_AL_child['version'] = "child"

SEGM_AL = pd.concat(
    [SEGM_AL_adult, SEGM_AL_child],
    ignore_index = True
    )

# =============================================================================
# SEGM_VN (SEGM_VN_2key_1000ms)
# median RT training
# median RT TRN-RND
# median RT RND-REC
# ACC TRN-RND
# ACC RND-REC
# 2AFC bigram
# 2AFC trigram
# production
# =============================================================================
SEGM_VN = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_DLD_1000ms/data/SEGM_VN_child_1000ms_wide_20220923_FINAL_SAMPLE_dprime_filtered.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SEGM_online_VN_2key_1000ms_letterID/data/SEGM_VN_2key_letterID_wide_20230427.csv"
         )
     ]
    )[
      ['ID',
       'medRT_train', 'medRT_TRN3_RND4', 'medRT_RND4_REC5',
       'ACC_train', 'ACC_TRN3_RND4', 'ACC_RND4_REC5',
       '2AFC_bigram', '2AFC_trigram', 'SEGM_prod_data']
      ]

# =============================================================================
# AGL
# ACC training
# 2AFC bigram trigram
# 2AFC sentence
# production
# =============================================================================
AGL = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/before_20220822/AGL_KS_mod4_pm_wide_20230601.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_online_v3_Knowton_mod4_YA/data/after_20220822/AGL_KS_mod4_wide_AGL_KS_20230601.csv"
         )
     ],
    ignore_index = True
    )[
      ['ID', 'ACC_train', '2AFC_phr', '2AFC_sent', 'prod']
      ]

# =============================================================================
# NAD
# median RT training
# median RT TRN-RND
# median RT RND-REC
# ACC training
# ACC TRN-RND
# ACC RND-REC
# 2AFC position
# 2AFC dependency
# production
# =============================================================================

NAD_v1 = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID/data/AGL_NAD_letterID_wide_20231004.csv"
    )[
      ['ID',
       'medRT_train', 'medRT_TRN4_RND5', 'medRT_RND5_REC6',
       'ACC_train', 'ACC_TRN4_RND5', 'ACC_RND5_REC6',
       'twoAFC_pos', 'twoAFC_dep', 'prod_ACC'
       ]
      ]
NAD_v1.insert(0, 'version', "v1")

NAD_v2 = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_AGL_NAD_letterID_v2/data/AGL_NAD_v2_letterID_wide_20231004.csv"
    )[
      ['ID',
       'medRT_train', 'medRT_TRN4_RND5', 'medRT_RND5_REC6',
       'ACC_train', 'ACC_TRN4_RND5', 'ACC_RND5_REC6',
       'twoAFC_pos', 'twoAFC_dep', 'prod_ACC'
       ]
      ]
NAD_v2.insert(0, 'version', "v2")

NAD = pd.concat(
    [NAD_v1, NAD_v2],
    ignore_index = True
    )

# =============================================================================
# predictive
# RT_score
# ACC score
# =============================================================================
predictive = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Predictive/data/Predictive_wide_20230425.csv"
    )[
      ['ID', 'RT_score', 'ACC_score']
      ]

# =============================================================================
# dichotic
# =============================================================================
dichotic = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_dichotic_mod/data/dichotic_wide_20231004.csv"
    )[
      ['ID', 'nonforced_lat_index', 'left_forced_left_rate', 'right_forced_right_rate']
      ]

# =============================================================================
# trog
# pragm
# =============================================================================
trog = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Adult_trog/data/trog_wide_20230425.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_trog_javitott/data/trog_wide_20230425.csv"
         )
     ]
    )[
      ['ID', 'pragm_ACC_mean']
      ]

# =============================================================================
# MENYET
# =============================================================================
MENYET = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_MENYET/data/MENYET_wide_20230428.csv"
    )[
      ['ID', 'mean_ACC_all']
      ]

# =============================================================================
# selfpaced (filtering: only correct all sentences, no RT filtering)
# sertes_target
# =============================================================================
selfpaced = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/selfpaced_wide_20231014.csv"
    )[
      ['ID', 'target_RT_diff_GP', 'plus1_RT_diff_mellekmondat', 'target_RT_diff_sertes']
      ]

# =============================================================================
# rec_vocab
# =============================================================================
rec_vocab = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_rec_vocab_2.0/data/rec_vocab_2.0_wide_20230428.csv"
    )

# =============================================================================
# OMR
# =============================================================================
OMR = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/OMR_20231014.csv"
    )
OMR = OMR[OMR['compr_acc'] > 0.5][['ID', 'read_syls']]

# merge dataframes

DF = pd.read_excel("C:/Users/Kriszti/GitHub/lendulet_SL_age/data/demography/all_IDs.xlsx")

dfs = [(dichotic, "dichotic"),
       (digit_span, "digit_span"),
       (MENYET, "MENYET"),
       (n_back, "n_back"),
       (OMR, "OMR"),
       (predictive, "predictive"),
       (PROC_SPEED, "PROC_SPEED"),
       (rec_vocab, "rec_vocab"),
       (SEGM_AL, "SEGM_AL"),
       (SEGM_VN, "SEGM_VN"),
       (AGL, "AGL"),
       (NAD, "NAD"),
       (selfpaced, "selfpaced"),
       (simon, "simon"),
       (stroop, "stroop"),
       (trog, "trog")]

for dataframe in dfs:
    df = dataframe[0]
    df['ID'] = df['ID'].astype(str).str.replace(".0", "", regex = False)
    name = dataframe[1]
    df.columns = ["_".join([name, x]) for x in df.columns]
    df.rename(columns = {name + "_ID" : 'ID'}, inplace = True)
    DF = DF.merge(right = df,
                  how = "outer",
                  on = 'ID')
DF = DF[pd.notna(DF['sex'])]

omit_1 = "ADHD|ASD|MX|DAMI|555_|5555|MMII|MMLL"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13",
          "AF100", "AF101", "AF104", "AF105", "AF106", "AF107", "AF110", "AF119", "AF100a", "AF100A",
          "AF120", "AF121", "AF122", "AF123", "AF124", "AF125", "AF127", "AF128", "AF129"]

DF_filt = DF[(DF['ID'].str.contains(omit_1) == False) & (DF['ID'].isin(omit_2) == False)]
DF_filt.drop_duplicates(subset = 'ID', inplace = True)

# calculating sample sizes for task pairings
DF_filt.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/SEM/dataframes/SEM_df.csv")
