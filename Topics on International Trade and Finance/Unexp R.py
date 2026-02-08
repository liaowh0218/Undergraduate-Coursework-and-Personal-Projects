import pandas as pd
import numpy as np
import statsmodels.api as sm

ExpR = pd.read_csv('Exp R.csv')
R = pd.read_csv('R.csv')

UnexpR = R['1-year_r']/100 - ExpR['Exp R']
ExpR['Unexp R'] = UnexpR

# to datetime
ExpR['DATE'] = pd.to_datetime(ExpR['DATE'])
R['DATE'] = pd.to_datetime(R['DATE'])

# merge on 'DATE' to align data
merged = pd.merge(ExpR, R, on='DATE', how='inner')

merged.to_csv('Unexp R.csv', index=False)
