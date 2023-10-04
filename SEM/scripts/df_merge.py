# -*- coding: utf-8 -*-
"""
author: krisztinasara
date: 20230425
title: dataframe merge for SEM
"""

import pandas as pd

# calculating sample sizes for task pairings

dfs = [(dichotic, "dichotic"),
       (digit_span, "digit_span"),
       (MENYET, "MENYET"),
       (n_back, "n_back"),
       (OMR, "OMR"),
       (predictive, "predictive"),
       (PROC_SPEED, "PROC_SPEED"),
       (rec_vocab, "rec_vocab"),
       (SAT, "SAT"),
       (SEGM_AL, "SEGM_AL"),
       (SEGM_VN, "SEGM_VN"),
       (AGL, "AGL"),
       (NAD, "NAD"),
       (selfpaced, "selfpaced"),
       (simon, "simon"),
       (stroop, "stroop"),
       (trog, "trog")]

subj_n = pd.DataFrame(columns = ['df1', 'df2', 'subj_n'])
i = 0
for one in dfs:
    for two in dfs:
        df1 = one[0]
        df1['ID'] = df1['ID'].astype(str).str.replace(".0", "", regex = False)
        name1 = one[1]
        df2 = two[0]
        df2['ID'] = df2['ID'].astype(str).str.replace(".0", "", regex = False)
        name2 = two[1]
        if name1 != name2:
            subj_n.loc[i, 'df1'] = name1
            subj_n.loc[i, 'df2'] = name2
            subj_n.loc[i, 'subj_n'] = len(df1.merge(df2, "inner", "ID"))
            i = i + 1

del i, one, two, df1, df2, name1, name2

# merging dataframes

DF = pd.DataFrame(columns = ['ID'])

for dataframe in dfs:
    df = dataframe[0]
    df['ID'] = df['ID'].astype(str).str.replace(".0", "", regex = False)
    name = dataframe[1]
    df.columns = ["_".join([name, x]) for x in df.columns]
    df.rename(columns = {name + "_ID" : 'ID'}, inplace = True)
    DF = DF.merge(right = df,
                  how = "outer",
                  on = 'ID')
