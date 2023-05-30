import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('/mnt/data/avocado-updated-2020.csv')

# Convert 'date' column 
data['date'] = pd.to_datetime(data['date'])

# Define the list of regions to include in the analysis
regions_to_include = ['California', 'Great Lakes', 'Midsouth', 'Northeast', 'Plains', 'Southeast', 'South Central', 'West']

# Filter the data to include only the specified regions
data_filtered = data[data['geography'].isin(regions_to_include)]

# Plot the distribution of average price
sns.histplot(data=data_filtered, x="average_price", kde=True)
plt.title('Distribution of Average Price')
plt.xlabel('Average Price')
plt.ylabel('Frequency')
plt.show()

# Calculate the total sales volume for organic and conventional types
total_volume_type = data_filtered.groupby('type')['total_volume'].sum()

# Calculate the average price for organic and conventional types
avg_price_type = data_filtered.groupby('type')['average_price'].mean()

# Calculate the percentage of total volume for organic and conventional types
percentage_volume_type = total_volume_type / total_volume_type.sum() * 100

# Plot the average price for organic and conventional types
avg_price_type.plot(kind='bar', figsize=(12,6))
plt.title('Average Price for Organic and Conventional Types')
plt.xlabel('Type')
plt.ylabel('Average Price')
plt.show()

# Plot the percentage of total volume for organic and conventional types
percentage_volume_type.plot(kind='bar', figsize=(12,6))
plt.title('Percentage of Total Volume for Organic and Conventional Types')
plt.xlabel('Type')
plt.ylabel('Percentage of Total Volume')
plt.show()

