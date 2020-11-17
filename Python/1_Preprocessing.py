# Preprocessing
# Haifaa Alzahrani
29/10/2020

# %%
# Import packages
import math
import pandas as pd # For DataFrame 
import numpy as np # Array and numerical processing

# %%
# Loading csv
dataset1 = pd.read_csv("~/MISK_DSI/R/DS_Research_GoodreadsBooks/Data/books.csv")
dataset1.info()
dataset1.head()

# %%
dataset2 = pd.read_csv("~/MISK_DSI/R/DS_Research_GoodreadsBooks/Data/goodreads_books.csv")
dataset2.info()
dataset2.head()

# %%
# Removing unwanted columns and observations
dataset1.info()
dataset2.info()

# Remove empties
dataset1.dropna(axis=1, how='all')
dataset2.dropna(axis=0, how='all')
dataset1.dropna(axis=1, how='all')
dataset2.dropna(axis=0, how='all')

# Remove duplicated observations or books with no isbn
dataset1.drop_duplicates(keep=False, inplace=True) # was 11,131 rows - became 11,123 rows
dataset2.drop_duplicates(keep=False, inplace=True) # was 52199 rows - became 40317 rows

# Remove unwanted columns
dataset1 = dataset1.drop('isbn13', axis = 1)
dataset2 = dataset2.drop('isbn13', axis = 1)

dataset1.info()
dataset2.info()

# %% 
# Format publication date to only include the year
dataset1['publication_date'] = dataset1['publication_date'].str.strip().str[-4:]
dataset1['publication_date'].astype(int)

#import datetime as dt
#dataset1['publication_date'] = pd.to_datetime(dataset1.publication_date)
#dataset1['publication_date'].dt.strftime('%d-%m-%Y')
#dataset1.style.format({"publication_date": lambda t: t.strftime('%d-%m-%Y')})
#dataset1['publication_date'] = pd.to_datetime(dataset1['publication_date'], dayfirst = True)
#dataset1['publication_date'] = pd.to_datetime(dataset1['publication_date'], format='%m/%d/%y')
#dataset1['publication_date'] = pd.DatetimeIndex(dataset1['publication_date']).year

dataset1.head()

# %%
# Add additional columns (awards and genres)  to first dataset based on isbn
dataset1.shape
dataset2.shape

dataset2 = dataset2[['isbn', 'genre_and_votes', 'awards']]
#dataset = pd.concat([dataset1, dataset2], axis=1, sort=False)

dataset = pd.merge(dataset1, dataset2, on='isbn', how='left')
dataset = dataset.drop('Unnamed: 12', axis = 1)

dataset.shape
dataset.head()

# %%
# Keep only the first author (the others either a translated author name, a translator, etc)
dataset['authors'] = dataset['authors'].str.split('\/').str[1].str.strip()

# %%
# Drop unwanted columns and rows
dataset = dataset.dropna(axis=1, how='all') #drop any column filled only with NaN 
#books = books.drop(['Unnamed: 0'], axis = 1)
dataset = dataset.drop_duplicates()

# %%
# Save the resulted dataframe as csv
dataset.to_csv("~/MISK_DSI/R/DS_Research_GoodreadsBooks/Data/full_books_Python.csv")

# %%
dataset.head()
dataset.shape

# %%
