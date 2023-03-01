# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:48:52 2023

@author: Kriszti
"""

import pandas as pd

df = pd.read_csv()

to_omit = ''
long = df[df['ID'].str.contains(to_omit) == False]

wide = pd.pivot_table(long,
                      values = [],
                      index = 'ID',
                      columns = [])

wide.to_csv("")
