import pandas as pd
import numpy as np
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/liaoweihong/Desktop/Code/Python/國經專題/data!.csv')

# to numeric
data['INDPRO'] = pd.to_numeric(data['INDPRO'], errors='coerce')
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# take ln, to decimal
data['INDPRO'] = np.log(data['INDPRO'])
data['Price'] = np.log(data['Price'])
data['CPI'] = data['CPI']/100
data['FFR'] = data['FFR']/100
# data['Unexp R'] = data['Unexp R']/100

# date to datetime
data['DATE'] = pd.to_datetime(data['DATE'])
data.set_index('DATE', inplace=True)

# select numeric columns
df = data.select_dtypes(include=['number'])

# difference
df_diff = df.diff().dropna()

# robustness
for col in df_diff.columns:
    result = adfuller(df_diff[col])
    print(f"ADF 檢驗 {col}: p-value = {result[1]}")

model = VAR(df_diff)

selected_lags = model.select_order(maxlags=4)
print(selected_lags.summary())

result = model.fit(selected_lags.aic)
print(result.summary())

# impulse response function
irf = result.irf(40)
irf.plot(orth=False)  # orth=False 表示不進行正交化
plt.show()
