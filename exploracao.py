import pandas as pd
df = pd.read_csv('vehicles_us.csv')

df['is_4wd'] = df['is_4wd'].fillna(0.0)
df['odometer'] = df['odometer'].fillna(df['odometer'].median())
df['model_year'] = df['model_year'].fillna(df['model_year'].median())
df['cylinders'] = df['cylinders'].fillna(df['cylinders'].median())
df['paint_color'] = df['paint_color'].fillna('unknown')

print(df.head())
print(df.describe())
print(df.info())
