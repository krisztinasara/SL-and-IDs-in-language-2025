# -*- coding: utf-8 -*-
"""
author: krisztinasara
date: 20230425
title: read dataframes for SEM
"""

import pandas as pd

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
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_YA/data/PROC_SPEED_YA_20230201.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_PR_SPEED_vis_ac_v2_acdec/data/PROC_SPEED_v2_20230320.csv"
         )
     ]
    )[
      ['ID', 'vis_RT_med', 'ac_RT_med', 'vis_dec_RT_med', 'ac_dec_RT_med']
      ]

# =============================================================================
# simon
# RT_score
# =============================================================================
simon = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Simon_nyilas/data/Simon_nyilas_wide_20230307.csv"
    )[
      ['ID', 'RT_score']
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
# SEGM_AL_adult (SEGM_AL_adult_300ms_2key)
# median RT training
# median RT TRN-RND
# median RT RND-REC
# ACC training
# ACC TRN-RND
# ACC RND-REC
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
      ['ID',
       'medRT_train', 'medRT_TRN3_RND4', 'medRT_RND4_REC5',
       'ACC_train', 'ACC_TRN3_RND4', 'ACC_RND4_REC5',
       'SEGM_prod_data']
      ]

# =============================================================================
# SEGM_AL_child (SEGM_online_AL_2keys_child_450ms)
# ACC_train
# ACC_TRN3_RND4
# ACC_RND4_REC5
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
      ['ID', 'ACC_train', 'ACC_TRN3_RND4', 'ACC_RND4_REC5']
      ]

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
# 2AFC
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
       '2AFC_all', 'SEGM_prod_data']
      ]

# =============================================================================
# predictive
# RT_score
# =============================================================================
predictive = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Predictive/data/Predictive_wide_20230425.csv"
    )[
      ['ID', 'RT_score']
      ]

# =============================================================================
# dichotic
# =============================================================================
dichotic = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_dichotic_mod/data/dichotic_wide_20230310.csv"
    )[
      ['ID', 'nonforced_lat_index']
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
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/selfpaced_wide_20230428.csv"
    )[
      ['ID', 'target_RT_diff_sertes']
      ]

# =============================================================================
# rec_vocab
# =============================================================================
rec_vocab = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_rec_vocab_2.0/data/rec_vocab_2.0_wide_20230428.csv"
    )

# =============================================================================
# digit_span
# =============================================================================
digit_span = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_DigitSpan/data/DigitSpan_20230320.csv"
    )[
      ['ID', 'forward_span', 'backward_span']
      ]

# =============================================================================
# OMR
# =============================================================================
OMR = pd.read_csv(
    "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_Self_paced_reading/data/OMR_20230428.csv"
    )
OMR = OMR[OMR['compr_acc'] > 0.5][['ID', 'read_syls']]

# =============================================================================
# SAT
# =============================================================================
SAT = pd.concat(
    [
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SAT_MC_II/data/SAT_MC_II_wide_20230428.csv"
         ),
     pd.read_csv(
         "C:/Users/Kriszti/LENDULET/kiserletek/elemzesek/AN_SAT_MC_II_with_sound/data/SAT_MC_II_wide_20230428.csv"
         )
     ]
    )[
      ['ID', 'ACC']
      ]
