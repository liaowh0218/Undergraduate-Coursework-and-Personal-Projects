# 算35的95%信賴區間，上傳次數(約95000次左右)
from scipy.stats import norm, binom
import numpy as np

np.random.seed(234)
for n in range(31,41):
    counter = 0
    for i in range(100000):
        phat = binom.rvs(n , 0.3 , size=1 )/n
        z = norm.ppf(0.975)
        if phat - z*(phat*(1-phat)/n)**0.5 <= 0.3 <= phat + z*(phat*(1-phat)/n)**0.5:
            counter += 1

    print(f'n={n}, {counter}')