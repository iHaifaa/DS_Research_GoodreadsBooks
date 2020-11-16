# Exploratory Data Analysis (EDA)
# Haifaa Alzahrani
29/10/2020

# %%
# Import packages
import math
import pandas as pd # For DataFrame 
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting

# %%
# Read the dataset
books = pd.read_csv("~/MISK_DSI/R/DS_Research_GoodreadsBooks/Data/full_books.csv")

# %%
# Examine the dataset
books.info()
books.shape
books.head(10)
# %%
# Drop unwanted columns and rows
books = books.dropna(axis=1, how='all') #drop any column filled only with NaN 
books = books.drop(['Unnamed: 0'], axis = 1)
books = books.drop_duplicates()

# %%
# Number of authors
len(books['authors'].unique())

# %%
# Number of books per author
books['authors'].value_counts()

# %%
# There are duplicated books due to adding different parts or edition as separated books
books['title'].value_counts()
# %%
# There are duplicated books due to adding different parts or edition as separated books.
# To view the top 25 highest repeated books


# %%
#The most 10 popular authors according to rating count for their books


# %% 
#The books that got the highest 25 number ratings.
#To learn the most popular books.

# %%
#The books that got the highest 25 count of reviews. 
#To know which books motivate readers to discuss about them 


# %%
#Popular books that got the highest 25 ratings.
#To know the most favorite books.


# %%
#Top 25 years according to the number of the published books


# %% 
#Does the number of pages affect rating counts? 
