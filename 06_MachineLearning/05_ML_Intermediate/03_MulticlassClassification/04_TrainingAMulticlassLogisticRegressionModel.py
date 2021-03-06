# origin -- Integer and Categorical. 1: North America, 2: Europe, 3: Asia.

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# read csv files
cars = pd.read_csv('auto.csv')

# create dummy variables for the categorical variables
dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
dummy_years = pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

# drop the dummy originating columns
cars = cars.drop(['cylinders', 'year'], axis=1)

# Split the shuffled_cars Dataframe into 2 Dataframes: train and test.
# Assign the first 70% of the shuffled_cars to train.
# Assign the last 30% of the shuffled_cars to test.
np.random.seed(1)
shuffled_index = np.random.permutation(cars.index)
shuffled_cars = cars.reindex(shuffled_index)
seventy_percent = round(len(shuffled_cars) * 0.7)
train = shuffled_cars.iloc[0:seventy_percent]
test = shuffled_cars.iloc[seventy_percent:]

# For each value in unique_origins, train a logistic regression model with the following parameters:
    # X: Dataframe containing just the cylinder & year binary columns.
    # y: list (or Series) of Boolean values:
        # True if observation's value for origin matches the current iterator variable.
        # False if observation's value for origin doesn't match the current iterator variable.
# Add each model to the models dictionary with the following structure:
    # key: origin value (1, 2, or 3),
    # value: relevant LogistcRegression model instance.

features = [c for c in train.columns if c.startswith("cyl") or c.startswith("year")]

unique_origins = cars['origin'].unique()
unique_origins.sort()
models = {}

for origin in unique_origins:
    # Generate boolean list based upon current target
    target = train['origin'] == origin
        
    # instantiate LogisticRegression object
    model = LogisticRegression()
    
    # Train LogisticRegression model
    model.fit(train[features], target)
    
    # Add the model to the dictionary
    models[origin] = model
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    