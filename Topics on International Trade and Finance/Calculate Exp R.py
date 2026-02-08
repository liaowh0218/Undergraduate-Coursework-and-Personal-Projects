import pandas as pd
import numpy as np
import statsmodels.api as sm

ExpInf = pd.read_csv('Exp Inf.csv')
RealR = pd.read_csv('real R.csv')

ExpInf['Exp Inf'] = 1 + ExpInf['Exp Inf']/100
RealR['Real R'] = 1 + RealR['Real R']/100
ExpR = (ExpInf['Exp Inf'] * RealR['Real R']) - 1
ExpInf['Exp R'] = ExpR

# to datetime
ExpInf['DATE'] = pd.to_datetime(ExpInf['DATE'])
RealR['DATE'] = pd.to_datetime(RealR['DATE'])

# merge on 'DATE' to align data
merged = pd.merge(ExpInf, RealR, on='DATE', how='inner')

merged.to_csv('Exp R.csv', index=False)
