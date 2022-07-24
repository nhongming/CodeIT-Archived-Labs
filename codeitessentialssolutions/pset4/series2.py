import csv


class Series:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.movies = []
        self.averageRating = None

    def setMovies(self, movies):
        for movie in movies:
            if movie.series_id == self.id:
                self.movies.append(movie)
        return

    def setAverageRating(self):
        total = 0
        for movie in self.movies:
            total += float(movie.rating)
        self.averageRating = total / len(self.movies)
        return


class Movie:
    def __init__(self, id, title, series_id):
        self.id = id
        self.title = title
        self.series_id = series_id
        self.rating = None

    def setRating(self, ratings):
        self.rating = ratings[self.id]
        return


def load():
    series = []
    movies = []
    ratings = {}

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

    with open("ratings.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
                continue
            ratings[row[0]] = row[1]

    return series, movies, ratings

# MAIN


def main():
    series, movies, ratings = load()

    for i in range(len(movies)):
        movies[i].setRating(ratings)

    for i in range(len(series)):
        series[i].setMovies(movies)
        series[i].setAverageRating()

    max = 0
    best = None
    for singleSeries in series:
        if singleSeries.averageRating > max:
            max = singleSeries.averageRating
            best = singleSeries

    print("SERIES WITH HIGHEST RATING")
    print("series: {}".format(best.name))
    print("average rating: {:.2f}".format(best.averageRating))


if __name__ == '__main__':
    main()
