import pandas as pd

dispensario_df = pd.read_csv('unit_2_dispensario.csv')
print(dispensario_df)

print(dispensario_df[['dispensario', 'pueblo']])

print(dispensario_df['pueblo'].unique())

print(dispensario_df.head(-1))

print(dispensario_df.info())


print(dispensario_df.describe())


print(dispensario_df[dispensario_df['Age'] < 21])

dispensario_df['Pago'] = 'Credit'

print(dispensario_df.head(5))

# Applying a function to a column
dispensario_df['Ventas in 10 Years'] = dispensario_df['ventas'].apply(lambda x: x * 1/10000)

print(dispensario_df)

print(dispensario_df.groupby('ventas').count())

print(dispensario_df.groupby('pueblo').count())

print(dispensario_df.groupby('Age').count())


print(dispensario_df)
average_ventas = dispensario_df['ventas'].mean()

# dispensario_df.dropna(inplace=True)
dispensario_df.fillna(value=average_ventas, inplace=True)
print(dispensario_df['Age'].unique())
print(dispensario_df)
