#data reading
library(readr)
library(tidyverse)

SEM_df_all_participants = read_csv("SEM_df_all_participants.csv")

#select proper IDs
include_IDs = read_csv("~/GitHub/lendulet_language_SL/data/include_IDs.csv")
ids = as.vector(t(include_IDs))

#selecting and renaming variables
selected_data = SEM_df_all_participants %>% 
  select(c(ID,
           sex,
           age_years,
           right_handedness,
           years_in_education,
           highest_education_level,
           current_education_level,
           digit_span_forward_span,
           digit_span_backward_span,
           MENYET_mean_ACC_all,
           n_back_nback_1_dprime,
           n_back_nback_2_dprime,
           n_back_nback_3_dprime,
           OMR_read_syls,
           predictive_RT_score,
           predictive_ACC_score,
           PROC_SPEED_vis_RT_med,
           PROC_SPEED_ac_RT_med,
           PROC_SPEED_vis_dec_RT_med,
           SEGM_AL_medRT_train,
           SEGM_AL_medRT_TRN3_RND4,
           SEGM_AL_medRT_RND4_REC5,
           SEGM_AL_ACC_train,
           SEGM_AL_ACC_TRN3_RND4,
           SEGM_AL_ACC_RND4_REC5,
           SEGM_AL_2AFC_bigram,
           SEGM_AL_2AFC_trigram,
           SEGM_AL_SEGM_prod_data,
           AGL_ACC_train,
           AGL_2AFC_phr,
           AGL_2AFC_sent,
           AGL_prod,
           selfpaced_target_RT_diff_GP,
           selfpaced_target_RT_diff_sertes,
           simon_RT_score,
           simon_ACC_score,
           stroop_RT_score,
           stroop_ACC_score,
           trog_pragm_ACC_mean)) %>% 
  rename(c(digit_span_forward = digit_span_forward_span,
           digit_span_backward = digit_span_backward_span,
           grammatical_sensitivity = MENYET_mean_ACC_all,
           nback_1_back_dprime = n_back_nback_1_dprime,
           nback_2_back_dprime = n_back_nback_2_dprime,
           nback_3_back_dprime = n_back_nback_3_dprime,
           one_minute_reading = OMR_read_syls,
           predictive_sent_proc_RT = predictive_RT_score,
           predictive_sent_proc_accuracy = predictive_ACC_score,
           perceptual_speed_visual_RT = PROC_SPEED_vis_RT_med,
           perceptual_speed_auditory_RT = PROC_SPEED_ac_RT_med,
           perceptual_speed_visual_decision = PROC_SPEED_vis_dec_RT_med,
           SEGM_RT_training = SEGM_AL_medRT_train,
           SEGM_RT_TRN3_RND4 = SEGM_AL_medRT_TRN3_RND4,
           SEGM_RT_RND4_REC5 = SEGM_AL_medRT_RND4_REC5,
           SEGM_ACC_training = SEGM_AL_ACC_train,
           SEGM_ACC_TRN3_RND4 = SEGM_AL_ACC_TRN3_RND4,
           SEGM_ACC_RND4_REC5 = SEGM_AL_ACC_RND4_REC5,
           SEGM_2AFC_bigram = SEGM_AL_2AFC_bigram,
           SEGM_2AFC_trigram = SEGM_AL_2AFC_trigram,
           SEGM_production = SEGM_AL_SEGM_prod_data,
           AGL_ACC_training = AGL_ACC_train,
           AGL_2AFC_phrase = AGL_2AFC_phr,
           AGL_2AFC_sentence = AGL_2AFC_sent,
           AGL_production = AGL_prod,
           selfpaced_gardenpath_target = selfpaced_target_RT_diff_GP,
           selfpaced_violation_processing_target = selfpaced_target_RT_diff_sertes,
           simon_RT = simon_RT_score,
           simon_accuracy = simon_ACC_score,
           stroop_RT = stroop_RT_score,
           stroop_accuracy = stroop_ACC_score,
           pragmatic_comprehension = trog_pragm_ACC_mean))

#raw data for publication
data_raw = selected_data %>% 
  filter(ID %in% ids)

#standardised data for publication
data_std = selected_data %>% 
  mutate_at(-c(1:7), ~(scale(.) %>% as.vector)) %>% 
  filter(ID %in% ids)

