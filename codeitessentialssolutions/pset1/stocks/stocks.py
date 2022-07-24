
'''
    Stocks (Optional)
        1. Read in a <position-csv-filename> as a command line argument
        2. Store the rows inside the positions list with each row as dict or list
        3. Print the portfolio which made the most profits / least loss
        4. Print the portfolio which made the least profits /  most loss
    
        Note: Write your code in the main() function
'''

def profit(position):
    return (float(position[2]) - float(position[1])) * int(position[3])

def getPortfolios(positions):
    portfolios = {}

    # Store positions in dictionary where key is the portfolio name and value is total profits from that portfolio
    for position in positions:
        stockName = position[0]
        if stockName not in portfolios:
            portfolios[stockName] = 0.0

        portfolios[stockName] += profit(position)

    return portfolios


def getBestPortfolio(positions, portfolios):
    max = None
    best = None

    # Iterate and increase max everytime you encounter a greater portfolio
    for key in portfolios:
        if max == None or portfolios[key] > max:
            max = portfolios[key]
            best = key
    return [best, max]


def getWorstPortfolio(positions, portfolios):
    min = None
    worst = None

    # Iterate and decrease min everytime you encounter a lesser portfolio
    for key in portfolios:
        if min == None or portfolios[key] < min:
            min = portfolios[key]
            worst = key
    return [worst, min]

import csv
from sys import argv

def main():
    # WRITE YOUR CODE HERE
    positions = []
    pass
    if len(argv) < 2:
        print("need a file to read")
        exit()
    filename = argv[1]

    with open(filename, 'r') as csv_file:
        lineCount = 0
        myReader = csv.reader(csv_file)

        for row in myReader:
            if lineCount == 0:
                lineCount += 1
                continue
            positions.append(row)

    # get portfolios
    portfolios = getPortfolios(positions)

    # 1. best portfolio
    bestPortfolio = getBestPortfolio(positions, portfolios)
    if bestPortfolio[1] < 0:
        print(
            "Best portfolio: {}, Profits: -${:.2f}".format(bestPortfolio[0], -bestPortfolio[1]))
    else:
        print("Best portfolio: {}, Profits: ${:.2f}".format(
            bestPortfolio[0], bestPortfolio[1]))

    # 2. worst portfolio
    worstPortfolio = getWorstPortfolio(positions, portfolios)
    if worstPortfolio[1] < 0:
        print(
            "Best portfolio: {}, Profits: -${:.2f}".format(worstPortfolio[0], -worstPortfolio[1]))
    else:
        print("Best portfolio: {}, Profits: ${:.2f}".format(
            worstPortfolio[0], worstPortfolio[1]))

if __name__ == "__main__":
    main()