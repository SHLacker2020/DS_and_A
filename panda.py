import pandas as pd


df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [15, 25, 35, 45]})

df['C'] = df['A'] + df['B']
df['D'] = df['C'].apply(lambda x: x/2 if x>50 else x)
max_value = df['D'].max()

print(max_value)
print()


df2 = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'],
     'B': [1, 2, 3, 4],
     'C': [5, 6, 7, 8]})

df22 = df2.groupby('A')
mean_df = df22.mean()

print(mean_df)

"E" = 23

"B" = 44
