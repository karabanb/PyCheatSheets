
import pandas as pd
import numpy as np

df = pd.read_csv('/Users/bkaraban/PycharmProjects/PyCheatSheets/data/train.csv', index_col='PassengerId')

# result = pd.DataFrame()


def df_summary(df):

    types = df.dtypes
    types.name = 'type'

    n_obs = len(df)
    n_nas = np.sum(df.isna()).rename('n_nas')
    pct_nas = (n_nas / n_obs).rename('pct_nas')

    n_zeros = np.sum(df.apply(lambda x: x == 0)).rename('n_zeros')
    pct_zeros = (n_zeros / n_obs).rename('pct_zeros')

    n_distinct = df.nunique().rename('n_distinct')

    quantiles = df.describe().transpose().iloc[:, 1:]

    to_concat = [types, n_distinct, n_nas, pct_nas, n_zeros, pct_zeros]

    result = pd.concat(to_concat, axis=1).sort_values(by='type')
