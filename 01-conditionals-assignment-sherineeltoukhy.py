# creating a conda environment
c:\Users\eltoukhysm>conda create -n pandas python=3.6 pandas
c:\Users\eltoukhysm>activate pandas
c:\Users\eltoukhysm>python

# importing pandas and numpy
import pandas as pd
import numpy as np

# reading in csv file of tweets
df = pd.read_csv(r'c:\Users\eltoukhysm\Biof309_Fall2017\Assignments\Conditionals_assignment\tweets.csv')
df.head()

#finding unique entries in State column
df['state'].unique()

#Getting the mean favored and retweeted by State and saving it to a new dataframe
stats = df.groupby('state').mean()
stats.describe()

#creating a function with values low, medium, high based on quartiles grouped by states
f = []
for row in df['favorite_count']:
    if row <= 0.11:
        f.append('low')
    elif row > 0.12 and row < 0.24:
        f.append('medium')
    else:
        f.append('high')

#creating a function with values low, medium, high based on quartiles grouped by states
r = []
for row in df['retweet_count']:
    if row <= 211.20:
        r.append('low')
    elif row > 212 and row < 299:
        r.append('medium')
    else:
        r.append('high')

df['f'] = f
df['r'] = r

df.head()

#counting categories of favored tweets and retweets by state
df.groupby('state')['f'].value_counts()
df.groupby('state')['r'].value_counts()
