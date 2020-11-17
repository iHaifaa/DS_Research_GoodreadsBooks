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
# Number of authors
len(books['authors'].unique())

# %%
# Number of books per author
books['authors'].value_counts()

# %%
# There are duplicated books due to adding different parts or edition as separated books
#most_repeated = books['title'].value_counts().head(25)

# To view the top 25 highest repeated books
#books_subset = books[books['title'].isin(repeated)]
#sns.barplot(data = books_subset, x='title')

sns.barplot(data = books, x='title', order=books.title.value_counts().iloc[:3].index)

# %%
#The most 10 popular authors according to rating count for their books
popular_authors = books.groupby('authors').sum().ratings_count.nlargest(25)
sns.barplot(popular_authors.index, popular_authors.values)

# %% 
#The books that got the highest 25 number ratings.
#To learn the most popular books.
popular_books = books.groupby('title').sum().ratings_count.nlargest(25)
sns.barplot(popular_books.index, popular_books.values)

# %%
#The books that got the highest 25 count of reviews. 
#To know which books motivate readers to discuss about them 
interesting_books = books.groupby('title').sum().text_reviews_count.nlargest(25)
sns.barplot(interesting_books.index, interesting_books.values)

# %%
#Popular books that got the highest 25 ratings.
#To know the most favorite books.
favorite_books = books.groupby('title').sum().average_rating.nlargest(25)
sns.barplot(favorite_books.index, favorite_books.values)

# %%
#Top 25 years according to the number of the published books
years = books.groupby('publication_date').sum().title.nlargest(25)
sns.barplot(years.index, years.values)

# %% 
#Does the number of pages affect rating counts? 
sns.distplot(books['ratings_count'], books['ratings_count'])
