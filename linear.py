#coding on hand skills
#taking a dataset from sklearn.datasets (like Boston housing)
import numpy as np
from sklearn.datasets import load_boston
import pandas as pd

df = pd.DataFrame(load_boston().data, columns=load_boston().feature_names)
print(df.head())
df.summary()
