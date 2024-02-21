import pandas as pd
import numpy as np

# solution 1
customer_df = pd.read_csv('unit_2_exercise1.csv')
print(customer_df)

# solution 2
customer_df['Age'] = np.abs(customer_df['Age'])
print(customer_df)

# solution 3
mean_value = np.nanmean(customer_df['PurchaseAmount'])
customer_df['PurchaseAmount'] = customer_df['PurchaseAmount'].fillna(
    value=mean_value)

# also correct
# customer_df['PurchaseAmount'].fillna(value=mean_value, inplace=True)
print(customer_df)

# solution 4
# customer_df['PurchaseDate'][2] = '2021-03-31'
customer_df.loc[2, 'PurchaseDate'] = '2021-03-31'
customer_df['PurchaseDate'] = pd.to_datetime(customer_df['PurchaseDate'])
print(customer_df)

# solution 5
customer_df['Gender'] = customer_df['Gender'].replace({'Fmale': 'Female'})
print(customer_df)
