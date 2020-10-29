# Goodreads_Books 
# Descriptive Statistics
# Haifaa Alzahrani
# 21/10/2020

######################################################################################################################

# Theoretical Probability Distribution ----
# Empirical frequency distribution (on the sample = dataset)
# It is distributions of a variable that we observe in a given sample.

# Overview 
summary(dataset)

# Average rating distribution
ggplot(dataset,aes(x=average_rating)) +      
  geom_density(alpha= 0.5,fill='#8dd3c7')+ 
  geom_vline(aes(xintercept=mean(average_rating)), linetype='dashed')+
  geom_text(aes(x=4.1, y=.8, label='mean'), size=3)+
  ggtitle('Average Rating Destribution')

# Ratings count distribution
dataset %>% 
  ggplot(aes(x=ratings_count)) + 
  geom_histogram(bins = 30, fill = "#bebada")+ 
  ggtitle('Ratings Count Destribution')

# Review count distribution
dataset %>% 
  ggplot(aes(x= text_reviews_count)) + 
  geom_histogram(bins=30, fill = "#fdb462")+ 
  ggtitle('Review Count Destribution')

# Page Number distribution
dataset %>% 
  ggplot(aes(x=num_pages)) + 
  geom_histogram(bins = 30, fill = "#bebada")+ 
  ggtitle('Page Number Destribution')

######################################################################################################################

# Understanding the relationships among the variables ----

# Which factor is most highly-correlated with the average rating of the book?

# Do the awards correlate with the average rating of the book?

# Is the number of pages and rating counts correlated?
