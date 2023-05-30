# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('/mnt/data/avocado-updated-2020.csv')

# Convert 'date' column
data['date'] = pd.to_datetime(data['date'])

# Define the list of regions to include in the analysis
regions_to_include = ['California', 'Great Lakes', 'Midsouth', 'Northeast', 'Plains', 'Southeast', 'South Central', 'West']

# Filter the data to include only the specified regions
data_filtered = data[data['geography'].isin(regions_to_include)]

# Calculate total sales volume by region and PLU
total_sales_plu_region_4046 = data_filtered.groupby('geography')['4046'].sum()
total_sales_plu_region_4225 = data_filtered.groupby('geography')['4225'].sum()
total_sales_plu_region_4770 = data_filtered.groupby('geography')['4770'].sum()

# Concat the data into a single df
plu_region_df = pd.concat([total_sales_plu_region_4046, total_sales_plu_region_4225, total_sales_plu_region_4770], axis=1)

# Rename the columns
plu_region_df.columns = ['4046', '4225', '4770']

# Calculate the total value of each PLU by region
total_value_plu_region_4046 = (data_filtered['4046'] * data_filtered['average_price']).groupby(data_filtered['geography']).sum()
total_value_plu_region_4225 = (data_filtered['4225'] * data_filtered['average_price']).groupby(data_filtered['geography']).sum()
total_value_plu_region_4770 = (data_filtered['4770'] * data_filtered['average_price']).groupby(data_filtered['geography']).sum()

# Calculate the average price of each PLU by region
avg_price_plu_region_4046 = total_value_plu_region_4046 / total_sales_plu_region_4046
avg_price_plu_region_4225 = total_value_plu_region_4225 / total_sales_plu_region_4225
avg_price_plu_region_4770 = total_value_plu_region_4770 / total_sales_plu_region_4770

# Concatenate the data into a single DataFrame
avg_price_plu_region_df = pd.concat([avg_price_plu_region_4046, avg_price_plu_region_4225, avg_price_plu_region_4770], axis=1)

# Rename the columns
avg_price_plu_region_df.columns = ['4046', '4225', '4770']

# Order the sales volume data by descending total volume
ordered_sales_volume = plu_region_df.sum(axis=1).sort_values(ascending=False).index
plu_region_df = plu_region_df.loc[ordered_sales_volume]

# Order the average price data by descending average price
ordered_avg_price = avg_price_plu_region_df.mean(axis=1).sort_values(ascending=False).index
avg_price_plu_region_df = avg_price_plu_region_df.loc[ordered_avg_price]

# Plot the ordered sales volume data
plu_region_df.plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Total Sales Volume by Region and PLU')
plt.xlabel('Region')
plt.ylabel('Total Sales Volume')
plt.legend(title='PLU')
plt.show()

# Plot the ordered average price data
avg_price_plu_region_df.plot(kind='bar', stacked=False, figsize=(12,6))
plt.title('Average Price by Region and PLU')
plt.xlabel('Region')
plt.ylabel('Average Price')
plt.legend(title='PLU')
plt.show()

