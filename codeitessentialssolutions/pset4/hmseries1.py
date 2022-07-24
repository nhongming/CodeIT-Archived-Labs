
'''
    Series 1

    Your Task:
        1. Read from series.csv and add each row into the series list as a Series object
        2. Read from movies.csv and add each row into the movies list as a Movie object
        3. Set each series' movies attribute to contain a list of the movies belonging to that series
        4. Print out each series and the movies it contains

        Note: 
            - Think about making use of class methods to create abstraction
            - Write your code in the main() function 
'''

class Series: 
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = []

    def get_movies(self,movie_list):
        for movie in movie_list:
            movie_series_id = movie.series_id
            if movie_series_id == self.id:
                self.movies.append(movie.title)

class Movie: 
    def __init__(self, id, title, series_id):
        self.id = id
        self.title = title
        self.series_id = series_id

import csv 

def main():
    series = []
    movies = [] 
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

    for series_code in series:
        series_code.get_movies(movies)
        print(f"{series_code.name}:")
        for series_code_movie in series_code.movies:
            print(series_code_movie)
        print(end="\n")
        
if __name__ == '__main__':
    main()