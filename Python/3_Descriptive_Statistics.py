# Descriptive Statistics
# date: 21/10/2020
# Haifaa Alzahrani

# %%
# Theoretical Probability Distribution
# It is empirical frequency distribution (on the sample = dataset),
# which reflects the distributions of a variable that we observe in a given sample.

# %%
# Import packages
import math
import pandas as pd # For DataFrame 
import numpy as np # Array and numerical processing
import matplotlib.pyplot as plt # Low level plotting
import seaborn as sns # High level Plotting

# %%
# Read the dataset
books = pd.read_csv("~/MISK_DSI/R/DS_Research_GoodreadsBooks/Data/full_books_Python.csv")

# Overview on descriptive statistics
books.describe()

# %%
# Average rating distribution.
sns.distplot(books['average_rating'])

# %% 
# Ratings count distribution.
sns.distplot(books['ratings_count'])


# %% 
# Review count distribution
sns.distplot(books['text_reviews_count'])

# %% 
# Page Number distribution
sns.distplot(books['num_pages'])

# %%
books.head()
