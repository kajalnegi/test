import numpy as np
import pandas as pd
from collections import Counter
from sklearn.preprocessing import OneHotEncoder
from test3 import k_labels

def categorical_or_not(x):
    if isinstance(x.dtype, pd.api.types.CategoricalDtype) or x.dtype == bool or isinstance(x.dtypes, pd.api.types.IntervalDtype) or \
            isinstance(x.dtype, pd.api.types.PeriodDtype):
        return True
    elif isinstance(x.dtype, pd.api.types.DatetimeTZDtype):
        return False
    elif (len(np.unique(x))*1.0)/len(x) <= 0.34:
        return True
    return False


def regroup_category(data, i):
    data = pd.DataFrame(data)
    y = data[0]
    x = data[i]
    print("------------     Data type of column is ", x.dtypes,'\n')
    if categorical_or_not(x):
        print("------------     Data type of column is classified as Categorical \n")
        print("------------     Original unique count in column ", np.unique(x))
        if x.dtype == bool or len(np.unique(x)) <= 5:
            enc = OneHotEncoder(categories='auto', drop='first').fit_transform(pd.DataFrame(x))
            return enc.toarray()

        k, labels = k_labels(pd.DataFrame(y))
        print("------------     New category count ", k)
        print("(Old, New) labels ", list(zip(x,labels)))
        enc = OneHotEncoder(categories='auto', drop='first').fit_transform(labels)
        return enc.toarray()




x = pd.DataFrame([[1.1, 1],[1.2, 2],[1.3, 2],[1.4, 1],[1.5, 2],[1.6, 1]])
print(regroup_category(x,1))

