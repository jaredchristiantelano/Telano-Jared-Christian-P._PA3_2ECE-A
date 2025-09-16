# Telano-Jared-Christian-P._PA3_2ECE-A

This assignment uses pandas to perform the following problems. 

Problem 1 

In this problem, a .csv file was turned into a data frame using pandas. The first 5 rows and the last 5 rows of the dataframe were then appended together in a single dataframe. 

Code
```
import pandas as pd                              # Loads the pandas library 

cars = pd.read_csv('cars.csv')                   # Reads and loads the CSV file into a dataframe named 'cars'
firstFive = cars.head(5)                         # Obtains the first five rows of the data frame
lastFive = cars.tail(5)                          # Obtains the last five rows of the data frame
cars_5 = pd.concat([firstFive, lastFive])        # Appends the first five rows and the last five rows in a single dataframe
cars_5                                           # Displays the dataframe
```

Problem 2 

In this problem, the previous dataframe was also utilized in this problem. First, the first five rows with odd-numbered columns were located and displayed. Then, the problem called for the row that contains the 'Model' of 'Mazda RX4'. After that, the number of cylinders of the car model 'Camaro Z28' was determined. Lastly, the number of cylinders and the gear type of selected car models were determined. All of this information were extracted using subsetting, splicing, and indexing operations through pandas. 

Code 
```
# a. Display the first five rows with odd-numbered columns of cars 

cars.iloc[:5, 0::2]   # Uses integer-location indexing 
                      # :5     - Gets the first five rows 
                      # 0::2   - Gets every second column of the dataframe

# b. Display the row that contains the 'Model' of 'Mazda RX4' 
cars[cars['Model'] == 'Mazda RX4']    # Locates the row where the model is equal to 'Mazda RX4' as index is used

# c. Number of cylinders 'Camaro Z28' have
cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].item()   # Locates first the model Camaro Z28 
                                                        # .item() returns the number of cylinder from that model

# d. Number of cylinders and the gear type of car models Mazda RX4 Wag, Ford Pantera L, and Honda Civic have
cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']] 

# .isin()                    -  to locate the needed models 
# ['Model', 'cyl', 'gear']   -  to select the needed columns from the dataframe
```
