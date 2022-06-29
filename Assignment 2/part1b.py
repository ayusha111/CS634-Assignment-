#Importing required libraries
from scipy.stats import uniform
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
 
#taking random variables from Uniform distribution
data = uniform.rvs(size = 1000, loc = 4, scale=200)
 
#Plotting the results
sb.set_style('whitegrid')
ax = sb.distplot(data, bins = 30, color = 'k')
ax.set(xlabel = 'interval')
plt.show()