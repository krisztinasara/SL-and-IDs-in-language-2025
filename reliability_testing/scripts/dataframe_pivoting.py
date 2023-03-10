# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:48:52 2023

@author: Kriszti
"""

import pandas as pd

df = pd.read_csv()

omit_1 = "AF|ADHD|ASD|MX|DAMI|555_|5555"
omit_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
          "553_13"]
long = df[(df['ID'].str.contains(omit_1) == False) & (df['ID'].isin(omit_2) == False)]

wide = long.pivot(values = [],
                  index = 'ID',
                  columns = [])

wide.to_csv("")
