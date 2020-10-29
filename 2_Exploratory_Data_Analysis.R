# Goodreads_Books 
# Exploratory Data Analysis (EDA)
# Haifaa Alzahrani
# 21/10/2020

######################################################################################################################

# Initialize packages ----

library(tidyverse)

######################################################################################################################

# A brief discussion about the dataset ----

# The dataset has systematical error (bias):
# 1) Selection bias: 
# 2) Technology bias: 

# In addition, it has duplication issues and need to manually verified. 

######################################################################################################################

# Load data  ----

dataset <- read.csv("Goodreads_Books_Recommendation/Data/full_books.csv", encoding="UTF-8")
dataset <- as_tibble(dataset) #Enhanced dataframe

# Overview
glimpse(dataset)

# Remove X
dataset <- dataset %>%
  select(-X.1, -X)

## suggestion
# Use library(janitor)
# remove_empty()

######################################################################################################################

# The dataset's variables
tribble(
  ~"Variable", ~"Continuous/Numerical/Quantitave", ~"Categorical/Discrete/Qualitative/Factors",
  names(dataset)[1], "Ratio", "X",
  names(dataset)[2], "X", "Nominal",
  names(dataset)[3], "X", "Nominal",
  names(dataset)[4], "Ratio", "X",
  names(dataset)[5], "X", "Nominal",
  names(dataset)[6], "X", "Nominal",
  names(dataset)[7], "Ratio", "X",
  names(dataset)[8], "Ratio", "X",
  names(dataset)[9], "Ratio", "X",
  names(dataset)[10], "Ordinal", "X",
  names(dataset)[11], "X", "Nominal",
  names(dataset)[12], "X", "Nominal",
  names(dataset)[13], "X", "Nominal"
)

######################################################################################################################

# Exploratory Data Analysis (EDA) ----

# Number of authors
dataset$authors %>% 
  unique() %>% length() # 4215

# Visualization

# Repeated books' titles
dataset$title %>% 
  length() - dataset$title %>% 
  unique() %>% length() # 775 repeated titles

# sum(duplicated(dataset$title))

# There are duplicated books due to adding different parts or edition as separated books
dataset %>%
  group_by(title) %>%
  summarise(Number = n()) %>%
  arrange(-Number) %>%
  head(n=25) %>% 
  ggplot(aes(x=reorder(title, Number), y=Number, fill = Number)) +
  geom_col() +
  coord_flip() +
  labs(x="Title", y="Number of books")+
  ggtitle('Repeated books titles')

######################################################################################################################

# Questions ----

# The most 10 popular authors according to rating count for their books
dataset %>%
  group_by(authors) %>%
  summarise(rating_sum = sum(ratings_count)) %>%
  arrange(-rating_sum)  %>%
  top_n(10) %>%
  ggplot(aes(x = reorder(authors, rating_sum), y = rating_sum)) + 
  geom_col(alpha=0.7, fill = "red") +
  labs(x = "Author", y = "Sum of Ratings") +
  ggtitle("Most Popular Authors")+
  coord_flip()

# The books that got the highest 25 number ratings 
# To learn the most popular books
dataset %>%
  group_by(title) %>%
  arrange(-ratings_count) %>%
  top_n(25)  %>%
  select(title, authors, ratings_count, average_rating)
  #ggplot(aes(x = reorder(title, ratings_count), y = ratings_count)) + 
  #geom_col(alpha=0.7) +
  #scale_fill_brewer(palette = "Set3") +
  #labs(x = "Book Title", y = "Number of Ratings") +
  #ggtitle("Most Popular Books")+
  #coord_flip()

# The books that got the highest 25 count of reviews 
# To know which books motivate readers to discuss about them 
dataset %>%
  group_by(title) %>%
  arrange(-text_reviews_count) %>%
  top_n(25)  %>%
  select(title, authors, text_reviews_count, average_rating)

# Popular books that got the highest 25 ratings
# To know the most favorite books
dataset %>%
  group_by(title) %>%
  arrange(-average_rating) %>%
  top_n(25)  %>%
  select(title, authors, average_rating)

# Top 25 years according to the number of the published books
# Inaccurate results!
dataset %>%
  group_by(publication_date) %>%
  summarise(rating_sum = sum(ratings_count)) %>%
  arrange(-rating_sum) %>%
  top_n(25)
