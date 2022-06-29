# import packages
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
 
 
# generate data
data =stats.norm(scale=3, loc=70).rvs(100)
 
# plotting a histogram
ax = sns.distplot(data,
                  bins=50,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()










# import packages
import scipy.stats as stats
import seaborn as sns
import  matplotlib.pyplot as plt

 
# generate data
data =stats.norm(scale=2.5, loc=64.5).rvs(100)
 
# plotting a histogram
ax = sns.distplot(data,
                  bins=50,
                  kde=True,
                  color='pink',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()
























