# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 02:13:05 2024

@author: lerato vinolia
"""

import pandas as pd
df=pd.read_csv(r"C:/Users/lerato vinolia/Downloads/P1/P1/movie_dataset.csv")
print("file")

# Display the first few rows of the original DataFrame
print("Original DataFrame:")
print(df.head())

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

# Fill missing values (you can choose a different strategy based on your data)
# For example, filling missing values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Display the first few rows of the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df.head())

# Remove spaces from column names
df.columns = df.columns.str.replace(' ', '_')

#QUESTON 1
# Find the highest-rated movie
highest_rated_movie = df.nlargest(1, 'Rating') 

print("Highest Rated Movie:")
print(highest_rated_movie)


#QUESTION 2
# Calculate the average revenue, ignoring missing values
if 'Revenue' in df.columns:
    average_revenue = df['Revenue'].mean()
    print("Average Revenue of All Movies:", average_revenue)
# Print the column names to verify the correct name for revenue
print("Column Names:", df.columns)

    
#QUESTION 3
#Convert 'Release_Date' column to datetime format
df['Release_Date'] = pd.to_datetime(df['Release_Date'])

# Filter movies released from 2015 to 2017
filtered_df = df[(df['Release_Date'].dt.year >= 2015) & (df['Release_Date'].dt.year <= 2017)]

# Calculate the average revenue, ignoring missing values
average_revenue = filtered_df['Revenue'].mean()

# Display the average revenue
print("Average Revenue of Movies from 2015 to 2017:", average_revenue)

print("Column Names:", df.columns)
print("Column Names:", df.columns.tolist())

#QUESTION 4 average


#QUESTION 5 many released movies
movies_released = df[df['Year']==2016].count()

#QUESTION 6
rating_at_least_eight_point_zero=len(df[df['Rating']]>=8
print(rating_at_least_eight_point_zero)

#QUESTION 7
median_rating=dy[df['director']=='Christopher Nolan'].median_rating
print)(median_rating)

#QUESTION 8
average_rating_by_year=df.groupby('Year')
print(average_rating_by_year)

#QUESTION 9%
# Filter movies released in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Calculate the number of movies made in 2006 and 2016
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print("Percentage increase in number of movies between 2006 and 2016:", percentage_increase, "%")

#QUESTION 10 common actor 
actors=df['actors'].str.split(', ').explode()
actor_counts=actor.value_counts()
most_common_actor=actor_counts.idmax()
print(most_common_actor)

#QUESTION 11 unique g
genres=df['Genre'].str.split(',')explode()
print(unique_genres_count)