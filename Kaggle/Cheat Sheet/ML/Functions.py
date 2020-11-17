import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
from IPython.display import display

%matplotlib inline




def missing_values(df):
    missing=pd.DataFrame(df.isnull().sum()/len(data))*100
    missing.columns = ['missing_values(%)']
    missing['missing_values(numbers)'] = pd.DataFrame(df.isnull().sum())
    return missing.sort_values(by='missing_values(%)', ascending=False)
