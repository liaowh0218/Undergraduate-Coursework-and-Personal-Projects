import pandas as pd
import numpy as np
import statsmodels.api as sm

ip = pd.read_csv('ip.csv')
SP = pd.read_csv('SP 500.csv')
UnexpR = pd.read_csv('Unexp R.csv')
FFR = pd.read_csv('FFR.csv')
CPI = pd.read_csv('CPI.csv')

# to datetime
ip['DATE'] = pd.to_datetime(ip['DATE'])
SP['DATE'] = pd.to_datetime(SP['DATE'])
UnexpR['DATE'] = pd.to_datetime(UnexpR['DATE'])
FFR['DATE'] = pd.to_datetime(FFR['DATE'])
CPI['DATE'] = pd.to_datetime(CPI['DATE'])

# merge on 'DATE' to align data
merged = pd.merge(ip, CPI, on='DATE', how='inner')
merged = pd.merge(merged, FFR, on='DATE', how='inner')
merged = pd.merge(merged, UnexpR, on='DATE', how='inner')
merged = pd.merge(merged, SP, on='DATE', how='inner')

merged.to_csv('data!.csv', index=False)
