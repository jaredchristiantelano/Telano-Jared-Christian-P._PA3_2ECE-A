#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1

import pandas as pd                              # Loads the pandas library 

cars = pd.read_csv('cars.csv')                   # Reads and loads the CSV file into a dataframe named 'cars'
firstFive = cars.head(5)                         # Obtains the first five rows of the data frame
lastFive = cars.tail(5)                          # Obtains the last five rows of the data frame
cars_5 = pd.concat([firstFive, lastFive])        # Appends the first five rows and the last five rows in a single dataframe
cars_5                                           # Displays the dataframe


# In[ ]:




