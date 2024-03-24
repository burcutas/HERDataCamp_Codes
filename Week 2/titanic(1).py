import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
pd.set_option('display.max_columns', None)
df.head()
df.columns
df.info()

# how many people were on the titanic
total = df['who'].count()

# how many female were on the titanic
df[df['sex'] == 'female']['sex'].count()

# how many male were on the titanic
df[df['sex'] == 'male']['sex'].count()

# unique values in columns
df.nunique()

# pclass unique value count
df['pclass'].nunique()

# pclass and parch unique value count
df[['pclass', 'parch']].nunique()

# embarked type and change it to category
df['embarked'].dtype
df['embarked'] = df['embarked'].astype('category')
df['embarked'].dtype

# embarked value c
df[df['embarked'] == 'C']['embarked'].head()

# embarked value not s
df[df['embarked'] != 'S']['embarked'].head()

# age under 30 and female
df[(df['age'] < 30) & (df['sex'] == 'female')].head()

# fare over 500 or age over 70
df[(df['fare'] > 500) | (df['age'] > 70)].head()

# columns null values sum
df.isnull().sum()

# drop who variable
df.drop(columns=['who'], inplace=True)
df.columns

# deck's null values mode fill
embarked_mode = df['embarked'].mode()
df['embarked'].fillna(value=embarked_mode, inplace=True)

# age's null values median fill
age_median = df['age'].median()
df['age'].fillna(value=age_median, inplace=True)

grouped_data = df.groupby(['survived', 'pclass', 'sex'])
grouped_data.agg({'survived': ('sum', 'count', 'mean')})

def func(age):
    if age < 30:
        return 1
    else:
        return 0

df['age_flag'] = df['age'].apply(lambda x: func(x))


