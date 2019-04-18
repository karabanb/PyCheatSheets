


import pandas as pd
import numpy as np

df = pd.read_csv('/Users/bkaraban/PycharmProjects/PyCheatSheets/data/train.csv', index_col='PassengerId')

result = pd.DataFrame()
# def df_summary(df):
types = df.dtypes
types.name = 'type'

n_obs = len(df)
nas_count = sum(df.isna()).rename('na_cnt')
pct_nas = (nas_count/n_obs).rename('na_pct')
n_unique = df.nunique().rename('n_unique')


quantiles = df.describe().transpose().iloc[:, 1:]

result = pd.concat([types, nas_count, pct_nas, n_unique, quantiles], axis=1, sort=False).sort_values(by='type')


df.apply(lambda x: pd.unique(x))




