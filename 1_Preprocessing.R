# Goodreads Books Analysis 
# Data Preprocessing
# Haifaa Alzahrani
# 21/10/2020

######################################################################################################################

# Initialize packages ----

library(tidyverse)

######################################################################################################################

# Load data  ----
dataset <- read.csv("Goodreads_Books_Recommendation/Data/books.csv")
dataset <- as_tibble(dataset) #Enhanced dataframe

dataset2 <- read.csv("Goodreads_Books_Recommendation/Data/goodreads_books.csv", encoding="UTF-8")
dataset2 <- as_tibble(dataset2) #Enhanced dataframe

# Overview ----
glimpse(dataset)

#### suggestions
# # Enhanced dataframe
# dataset <- read_csv("Goodreads_Books_Recommendation/Data/books.csv")
# glimpse(dataset)
# 
# # dataset <- remove_empty(dataset)
# # glimpse(dataset)
# 
# # Enhanced dataframe 2
# dataset2 <- rio::import("Goodreads_Books_Recommendation/Data/goodreads_books.csv")
# glimpse(dataset2)
####


######################################################################################################################

# Preprocessing ----

# Remove duplicated observations or books with no isbn
dataset <- dataset %>% 
  distinct(isbn, .keep_all = TRUE) # was 11,131 rows - became 11,123 rows

dataset2 <- dataset2 %>% 
  distinct(isbn, .keep_all = TRUE) # was 52199 rows - became 40317 rows

# Remove unwanted columns
dataset <- dataset %>% 
  select(-isbn13)

# Add additional columns (awards and genres)  to first dataset based on isbn
dataset2 <- dataset2 %>% 
  select(isbn, genre_and_votes, awards)
dataset <- 
  left_join(dataset, dataset2, by = "isbn")

# Format publication date to only include the year
dataset$publication_date <- 
  substring(dataset$publication_date, nchar(as.character(dataset$publication_date)) - 3)

# suggestion:
# library(lubridate)
# year(mdy(dataset$publication_date))
####

# Keep only the first author (the others either a translated author name, a translator, etc)
dataset$authors <- 
  word(dataset$authors,1,sep = "\\/")

# Encode all English languages into Eng

# Make it tidy table (because genre_and_votes has multiple values) 
#dataset <- dataset %>%
#  separate_rows(genre_and_votes, sep = ", ") 
# Remove votes
# genres <- as.list(dataset$genre_and_votes)
# genres <- gsub('[[:digit:]]+', '', genres)
# genres
# dataset <- dataset %>%
#  add_column(genres) %>%
#  select(-genre_and_votes)

######################################################################################################################

# Save the resulted dataframe as csv
write.csv(dataset, "Goodreads_Books_Recommendation/Data/full_books.csv")
