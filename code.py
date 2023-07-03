# -*- coding: utf-8 -*-

import pandas as pd

# reading Data
df = pd.read_csv('data.csv', sep = ';', encoding ='utf-8')

# removing nulls from SiteID column
df= df.dropna(subset = ['SiteID'])

print('\nBEFORE NULL REMOVAL\n')
print(df.isna().sum())

# replacing numms with the columns's median
df = df.fillna(df.median().iloc[0])
print('\n')
print('*'*25)
print('\nAFTER NULL REMOVAL\n')
print(df.isna().sum())
