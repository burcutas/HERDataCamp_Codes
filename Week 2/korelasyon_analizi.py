import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv('Breast_Cancer.csv')
df = df.iloc[:, 1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

corr = df[num_cols].corr()

sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap='RdBu')
plt.show()


cor_matrix = df.corr().abs()
upper_triangle = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
drop_columns = [col for col in upper_triangle.columns if any(upper_triangle[col] > 0.90)]
df.drop(columns=drop_columns, inplace=True)

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
    drop_columns = [col for col in upper_triangle.columns if any(upper_triangle[col] > corr_th)]
    if plot:
        sns.heatmap(corr, cmap='RdBu')
        plt.show()
    return drop_columns

high_correlated_cols(df, plot=True, corr_th=0.90)