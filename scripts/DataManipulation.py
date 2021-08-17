
import pandas as pd

path = '/Users/bkaraban/PycharmProjects/PyCheatSheets/data/train.csv'
titanic = pd.read_csv(path, index_col='PassengerId')


########################################## SELECTING COLUMNS ###########################################################

# single column

one_col = titanic['Pclass']                                     # in this way we reached pandas.Series type
one_col = titanic[['Pclass']]                                   # but like that we got pandas.DataFrame type

one_col_loc = titanic.loc[:, 'Pclass']                          # pandas.Series
one_col_loc = titanic.loc[:, ['Pclass']]                        # pandas.DataFrame

one_col_iloc = titanic.iloc[:, 1]                               # pandas.Series

few_cols = titanic[['Pclass', 'Sex', 'Survived']]
few_cols_loc = titanic.loc[:, ['Pclass', 'Sex', 'Survived']]

# few columns

cols = ['Sex', 'Age', 'Survived']                               # by list
sel_by_list = titanic.loc[:, cols]

sel_by_loc = titanic.loc[:, ['Sex', 'Age', 'Survived']]

# slicing DataFrame

slice_cols_iloc = titanic.iloc[:, 0:4]
slice_from_left = titanic.loc[:, :'Sex']
slice_from_right = titanic.loc[:, 'Sex':]
slice_left_right = titanic.loc[:, 'Sex':'Ticket']


############################################# SELECTING ROWS ###########################################################

first_few_rows = titanic[0:5]
first_few_rows_loc = titanic.loc[0:5]
first_few_rows_iloc = titanic.iloc[0:5]


############################################# FILTERING ROWS ###########################################################

# filtering by boolean array

survived = titanic['Survived'] == 1
survived = titanic.loc[survived, :]


############################################# FILTERING NA's ###########################################################

rows_at_least_one_na = titanic.dropna(how='any')            # drop rows with at least one NA
rows_all_nas = titanic.dropna(how='all')                    # drop rows with all NA's

cols_at_least_one_na = titanic.dropna(axis=1, how='any')    # drop cols with at least one NA
cols_all_nas = titanic.dropna(axis=1, how='all')            # drop cols with all NA's

cols_at_least_thresh = titanic.dropna(axis=1, thresh=100)   # drop cols with at least 100 Na's

print('Heelo word')
