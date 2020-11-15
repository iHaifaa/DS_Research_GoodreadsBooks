# Exploratory Data Analysis (EDA)
# Haifaa Alzahrani
29/10/2020


# Import packages
import math
import pandas as pd # For DataFrame 
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting

# Read the dataset
books = pd.read_csv("Data/full_books.csv")

# Examine the dataset
books.info()
books.shape
books.describe()
books.head(10)

# Drop unwanted columns and rows
books = books.dropna(axis=1, how='all') #drop any column filled only with NaN 
books = books.drop(['Unnamed: 0'], axis = 1)
books = books.drop_duplicates()

# Number of authors
len(books['authors'].unique())

# Number of books per author
books['authors'].value_counts()

# There are duplicated books due to adding different parts or edition as separated books
books['title'].value_counts()