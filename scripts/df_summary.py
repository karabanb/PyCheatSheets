
import pandas as pd
import numpy as np

def df_summary(df):

    stat_cont = df.describe().transpose()

