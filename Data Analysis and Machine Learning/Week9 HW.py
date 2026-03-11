import numpy as np
import pandas as pd

data=np.array(pd.read_csv('/Users/liaoweihong/Desktop/Python/DAML/olympic100m.csv', header=None))
n=len(data)
np.random.seed(234)
# np.random.shuffle(data)
train, test = np.split(data, [19])

test_x = np.array([test[:, 0]])
test_y = np.array([test[:, 1]])
train_x = np.array([train[:, 0]])
train_y = np.array([train[:, 1]])

def err(a):
    '''a is the power of x, which means the order of polynomial'''
    X = []
    test_X = []
    for i in range(a):
        X.append(train_x**i)
        test_X.append(test_x**i)
    
    X = np.array(X)
    test_X = np.array(test_X)
    w = np.linalg.inv(X @ X.T) @ X @ train_y
    
    print(np.mean((test_y - test_X@w)**2))

err(2)