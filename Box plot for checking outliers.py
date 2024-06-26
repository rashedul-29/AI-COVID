#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# I will read the excel file first
df = pd.read_excel(r'C:\Users\ASUS\Downloads\merged_data2.xlsx')

# Now I will convert all non-numeric values to NaN for all columns
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Let me drop all columns with non-numeric values
df_numeric = df_numeric.select_dtypes(include='number')

# I will create now box plots for each column
for column in df_numeric.columns:
    # This is about selecting the column data
    data = df_numeric[column]

    # NaN values will be removed now
    data = data.dropna()

    # Creation of box plot
    sns.boxplot(y=data)

    # Setting uo all plot labels and title
    plt.ylabel(column)
    plt.title(f'Box Plot of {column}')

    # Displaying the plot finally
    plt.show()


# In[ ]:




