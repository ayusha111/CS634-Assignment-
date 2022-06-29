import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df = pd.read_csv('weight-height.csv')
df.head()
pearson_correlation = df.corr(method='pearson')
print(pearson_correlation)
sb.heatmap(pearson_correlation, 
            xticklabels=pearson_correlation.columns,
            yticklabels=pearson_correlation.columns,
            cmap="YlGnBu",
            annot=True,
            linewidth=0.5)
spearman_correlation=df.corr(method='spearman')
print(spearman_correlation)
kendall_correlation=df.corr(method='kendall')
print(kendall_correlation)

