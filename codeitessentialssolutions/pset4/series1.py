class Series: 
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = []
    
    def setMovies(self, movies):
        for movie in movies:
            if movie.series_id == self.id:
                self.movies.append(movie)

class Movie: 
    def __init__(self, id, title, series_id):
        self.id = id
        self.title = title
        self.series_id = series_id
        self.rating = None
    

# MAIN
import csv 

def load():
    series = []
    movies = [] 

    with open("series.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
                continue
            series.append(Series(row[0], row[1]))
    
    with open("movies.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
                continue
            movies.append(Movie(row[0], row[1], row[2]))
            
    return series, movies
            
def main():
    series = []
    movies = []
    series, movies = load()

    for i in range(len(series)):
        series[i].setMovies(movies)

    for i in series:
        print("{}: ".format(i.name))
        for movie in i.movies:
            print(movie.title)
        print()


if __name__ == '__main__':
    main()
