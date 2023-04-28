# -*- coding: utf-8 -*-
"""
author: krisztinasara
date: 20230428
title: filter and label dataframes for SEM
"""

omit_1 = "ADHD|ASD|MX|DAMI|555_|5555|MMII|MMLL"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13",
          "AF100", "AF101", "AF104", "AF105", "AF106", "AF107", "AF110", "AF119", "AF100a",
          "AF120", "AF121", "AF122", "AF123", "AF124", "AF125", "AF127", "AF128", "AF129"]

DF_filt = DF[(DF['ID'].str.contains(omit_1) == False) & (DF['ID'].isin(omit_2) == False)]
DF_filt.drop_duplicates(subset = 'ID', inplace = True)

DF_child = DF_filt[(DF_filt['ID'].str.startswith("61")) |
              (DF_filt['ID'].str.startswith("62")) |
              (DF_filt['ID'].str.startswith("KO1")) |
              (DF_filt['ID'].str.startswith("BS")) |
              (DF_filt['ID'].str.startswith("KOR2")) |
              (DF_filt['ID'].str.startswith("GYS"))]

DF_adult = DF_filt[((DF_filt['ID'].str.startswith("61")) |
               (DF_filt['ID'].str.startswith("62")) |
               (DF_filt['ID'].str.startswith("KO1")) |
               (DF_filt['ID'].str.startswith("BS")) |
               (DF_filt['ID'].str.startswith("KOR2")) |
               (DF_filt['ID'].str.startswith("GYS"))) == False]

DF_filt.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/SEM/dataframes/DF_allparticipants_20230428.csv", index = False)
DF_adult.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/SEM/dataframes/DF_adults_20230428.csv", index = False)
DF_child.to_csv("C:/Users/Kriszti/GitHub/lendulet_language_SL/SEM/dataframes/DF_children_20230428.csv", index = False)
