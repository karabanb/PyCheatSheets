
import pandas as pd

path = '/Users/bkaraban/PycharmProjects/PyCheatSheets/data/train.csv'
titanic = pd.read_csv(path, index_col='PassengerId')

########################################## SELECTING COLUMNS ###########################################################

# single column

one_col = titanic['Pclass']                                 # in this way we reached pandas.Series type
one_col = titanic[['Pclass']]                               # but like that we got pandas.DataFrame type

# slicing columns

one_col_loc = titanic.loc[:, 'Pclass']                          # pandas.Series
one_col_loc = titanic.loc[:, ['Pclass']]                        # pandas.Dataframe

one_col_iloc = titanic.iloc[:, 1]                                # pandas.Series

few_cols = titanic[['Pclass', 'Sex', 'Survived']]
few_cols_loc = titanic.loc[:, ['Pclass', 'Sex', 'Survived']]

few_cols_iloc = titanic.iloc[:, 0:4]

slice_from_left = titanic.loc[:, :'Sex']
slice_from_right = titanic.loc[:, 'Sex':]
slice_left_right = titanic.loc[:, 'Sex':'Ticket']

# selecting columns by list

cols = ['Sex', 'Age', 'Survived']
sel_by_list = titanic.loc[:, cols]

############################################# SELECTING ROWS ###########################################################

first_few_rows = titanic[0:5]
first_few_rows_loc = titanic.loc[0:5]
first_few_rows_iloc = titanic.iloc[0:5]

############################################# FILTERING ROWS ###########################################################


