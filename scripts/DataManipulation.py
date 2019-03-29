import pandas as pd

path = '/Users/bkaraban/PycharmProjects/PyCheatSheets/data/train.csv'

titanic = pd.read_csv(path, index_col='PassengerId')

''' selecting rows '''

first_few_rows = titanic[0:5]
first_few_rows_loc = titanic.loc[0:5]
first_few_rows_iloc = titanic.iloc[0:5]


''' selecting columns'''

one_col = titanic['Pclass']                                 # in this way we reached pandas.Series type
one_col = titanic[['Pclass']]                               # but like that we got pandas.DataFrame type

# slicing columns

one_col = titanic.loc[:, 'Pclass']                          # pandas.Series
one_col = titanic.loc[:, ['Pclass']]                        # pandas.Dataframe

one_col = titanic.iloc[:, 1]                                # pandas.Series

few_cols = titanic[['Pclass', 'Sex', 'Survived']]
few_cols = titanic.loc[:, ['Pclass', 'Sex', 'Survived']]

few_cols_iloc = titanic.iloc[:, 0:4]
