# -*- coding: utf-8 -*-
"""Assignment for Business Analyst Intern @Jar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11DIkjxrr7Q_tm_Yy106i8f77pkeK3hIO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

import pandas as pd
Data = pd.read_csv('BA Assignment Walmart Sales (1).csv')
Data

Data.head()

Data = Data.drop(columns=['Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17','Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', ])
print(Data)

Data.head()

"""**Performance of sales and revenue at the city and branch level**"""

# Calculate total sales
Data['Total Sales'] = Data['Unit price'] * Data['Quantity']

# Group by City and Branch
city_branch_sales = Data.groupby(['City', 'Branch']).agg({'Total Sales': 'sum'}).reset_index()

# Display the result
print(city_branch_sales)

import matplotlib.pyplot as plt
import seaborn as sns

# Set the plot size
plt.figure(figsize=(12, 6))

# Create a barplot for sales performance by City and Branch
sns.barplot(data=city_branch_sales, x='City', y='Total Sales', hue='Branch')
plt.title('Total Sales by City and Branch')
plt.xlabel('City')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

"""**Average price of an item sold at each branch of the city**"""

# Group by City and Branch and calculate the mean of Unit Price
average_price = Data.groupby(['City', 'Branch']).agg({'Unit price': 'mean'}).reset_index()

# Display the result
print(average_price)

"""Performance of sales and revenue, Month over Month across the
Product line, Gender, and Payment Method, and identify the focus areas to get better sales for April 2019
"""

# Convert 'Date' column to datetime format
Data['Date'] = pd.to_datetime(Data['Date'])

# Extract month and year from 'Date' column
Data['Month'] = Data['Date'].dt.month
Data['Year'] = Data['Date'].dt.year

# Calculate total sales
Data['Total Sales'] = Data['Unit price'] * Data['Quantity']

# Display the updated DataFrame
print(Data.head())

"""Analyze Sales Month-over-Month Across Product Line"""

# Group by 'Year', 'Month', and 'Product Line', and calculate total sales
monthly_sales_product_line = Data.groupby(['Year', 'Month', 'Product line']).agg({'Total Sales': 'sum'}).reset_index()

# Display the result
print("Monthly Sales Across Product Lines:")
print(monthly_sales_product_line)

"""Visualization - Monthly Sales Across Product Line"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(14, 8))
sns.lineplot(data=monthly_sales_product_line, x='Month', y='Total Sales', hue='Product line', marker='o')
plt.title('Monthly Sales Across Product Lines')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))
plt.legend(title='Product Line', loc='upper right')
plt.grid(True)
plt.show()

"""Analyze Sales Month-over-Month Across Gender"""

# Group by 'Year', 'Month', and 'Gender', and calculate total sales
monthly_sales_gender = Data.groupby(['Year', 'Month', 'Gender']).agg({'Total Sales': 'sum'}).reset_index()

# Display the result
print("\nMonthly Sales Across Gender:")
print(monthly_sales_gender)

"""Visualization - Monthly Sales Across Gender"""

plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales_gender, x='Month', y='Total Sales', hue='Gender', marker='o')
plt.title('Monthly Sales Across Gender')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))
plt.legend(title='Gender', loc='upper right')
plt.grid(True)
plt.show()

"""Analyze Sales Month-over-Month Across Payment Method

"""

# Group by 'Year', 'Month', and 'Payment', and calculate total sales
monthly_sales_payment = Data.groupby(['Year', 'Month', 'Payment']).agg({'Total Sales': 'sum'}).reset_index()

# Display the result
print("\nMonthly Sales Across Payment Method:")
print(monthly_sales_payment)

"""Visualization - Monthly Sales Across Payment Method"""

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales_payment, x='Month', y='Total Sales', hue='Payment', marker='o')
plt.title('Monthly Sales Across Payment Method')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))
plt.legend(title='Payment Method', loc='upper right')
plt.grid(True)
plt.show()





