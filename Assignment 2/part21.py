# import the necessary libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from statsmodels import api
from scipy import stats
from scipy.optimize import minimize

  import pandas.util.testing as tm
# create an independent variable 
x = np.linspace(-10, 30, 100)

# create an exponential distributed 
e = np.random.exponential(0.025, 10, 200)

# generate ground truth
y = 10 + 4*x + e

df = pd.DataFrame({'x':x, 'y':y})
df.head()