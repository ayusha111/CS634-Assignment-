#Importing required modules
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
 
#Applying the expon class methods
x = np.linspace(0.25,10, 200)
pdf = expon.pdf(x)
 
#Visualizing the results
sb.set_style('whitegrid')
plt.plot(x, pdf , 'r-', lw=2, alpha=0.6, label='expon pdf' , color = 'k')
plt.xlabel('intervals')
plt.ylabel('Probability Density')
plt.show()