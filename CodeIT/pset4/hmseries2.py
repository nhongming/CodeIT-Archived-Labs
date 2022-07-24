'''
    Series 2

    Your Task: 
        1. Read from movies.csv, series.csv and store each row 
           as it's respective object in it's respective list

        2. Read from ratings.csv and set the ratings and averageRatings attribute 
           of every movie and series appropriately
        
        3. Print the series with the highest average rating in the following format:
            SERIES WITH HIGHEST RATING
            series: <series-name>
            average rating: <series-average-rating>
        
        4. Your program should work regardless of the contents of the csv file

        Note: 
        - Think about making use of class methods and the new attributes to create abstraction
        - Write your code in the main() function
'''

class Series: 
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = []
        self.averageRating = None
    def get_movies(self,movie_list): # class method to obtain matched series movies
        for movie in movie_list:
            movie_series_id = movie.series_id
            if movie_series_id == self.id:
                self.movies.append(movie.title)
    def get_avgRating(self,movies,ratings): # class method to tabulate the average rating for the particular series
        sum_movie_rating = 0
        count_matched_movies = len(self.movies)
        for movie in movies:
            if movie.title in self.movies:             
                sum_movie_rating += movie.get_ratings(ratings)
        self.averageRating = sum_movie_rating / count_matched_movies

class Movie: 
    def __init__(self, id, title, series_id):
        self.id = id
        self.title = title
        self.series_id = series_id
        self.rating = None
    def get_ratings(self,ratings): #class method to obtain the movie rating and to be return for tabulation of average series rating
        if (self.id) in ratings:
            self.rating = ratings[self.id]
        return self.rating

import csv

def main():
    movies = []
    series = []
    # WRITE YOUR CODE HERE
    with open('series.csv', 'r') as series_file:
        seriesReader = csv.reader(series_file)
        lineCount = 0
        for row in seriesReader:
            if lineCount == 0:
                lineCount += 1
                continue
            series_id = row[0]
            series_name = row[-1]
            series_detail = Series(series_id,series_name)
            series.append(series_detail)

    with open('movies.csv', 'r') as movies_file:
        moviesReader = csv.reader(movies_file)
        lineCount = 0
        for row in moviesReader:
            if lineCount == 0:
                lineCount += 1
                continue
            movie_id = row[0]
            movie_title = row[1]
            movie_series_id = row[-1]
            movies_detail = Movie(movie_id,movie_title,movie_series_id)
            movies.append(movies_detail)

    ratings = {} #storing the movie_id and ratings as key-value pairs for easy access 
    with open('ratings.csv', 'r') as ratings_file:
        ratingsReader = csv.reader(ratings_file)
        lineCount = 0
        for row in ratingsReader:
            if lineCount == 0:
                lineCount += 1
                continue
            movie_id = row[0]
            movie_rating = float(row[-1])
            if movie_id not in ratings:
                ratings[movie_id] = movie_rating

    # instantiating the variables to be stored inside the 
    # avr_rating_list as tuple pairs (series_name,avr_rating)
    avr_rating_list = []
    for series_code in series:
        series_code.get_movies(movies)
        series_name = series_code.name
        for movie in movies:
            if movie.title in series_code.movies:
                movie.get_ratings(ratings)
                series_code.get_avgRating(movies,ratings)
        avg_series_rating = series_code.averageRating
        avr_rating_list.append((series_name,avg_series_rating))
    
    # sorting the avr_rating_list according to the rating value 
    # as the key sorting identifier
    descending_avr_rating_list = sorted(avr_rating_list, key=lambda x:x[1], reverse=True)
    highest_rating = descending_avr_rating_list[0]
    highest_rated_series = highest_rating[0]
    corr_avg_rating = highest_rating[-1] 
    # need to debug why round() cannot be used here, 
    # here variable is in float Type
    
    # printing of matched results
    print("SERIES WITH HIGHEST RATING", end='\n')
    print(f"series: {highest_rated_series}", end='\n')
    print(f"average rating: {corr_avg_rating:.2f}")

if __name__ == '__main__':
    main()