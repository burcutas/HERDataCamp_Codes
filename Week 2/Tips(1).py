import seaborn as sns
import pandas as pd

df = sns.load_dataset('tips')
pd.set_option('display.max_columns', None)
df.head()

df.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean'])

df.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])

df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')].groupby('day').agg({
    'total_bill': ['sum', 'min', 'max', 'mean'],
    'tip': ['sum', 'min', 'max', 'mean']
})

df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()

df['total_bill_sum'] = df['total_bill'] + df['tip']


sort_value = df.sort_values(by='total_bill_sum', ascending=False)
df_new = sort_value.head(30)