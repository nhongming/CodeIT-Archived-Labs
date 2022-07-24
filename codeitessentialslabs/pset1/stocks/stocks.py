
'''
    Stocks (Optional)
        1. Read in a <position-csv-filename> as a command line argument
        2. Store the rows inside the positions list with each row as dict or list
        3. Print the portfolio which made the most profits / least loss
        4. Print the portfolio which made the least profits /  most loss
    
    Note: Write your code in the main() function
'''

import csv
from sys import argv

# MAIN
def main():
    
    # WRITE YOUR CODE HERE

    position_dict = {}

    if len(argv) < 2:

        print("required file name")

    else:

        with open(argv[1], 'r') as csv_file:

            myReader = csv.reader(csv_file)

            lineCount = 0

            for row in myReader:
                if lineCount == 0:
                    lineCount += 1
                    continue

                stock = row[0]
                buy = float(row[1])
                sell = float(row[2])
                shares = int(row[3])
                profits = (sell - buy)*(shares)

                if stock not in position_dict:
                    position_dict[stock] = profits
                else:
                    position_dict[stock] += profits

    
    stock_list = [ stocks for stocks in position_dict.items() ]
    # print(stock_list)
    highest_profits = stock_list[0][1]
    best_portfolio = stock_list[0][0]
    lowest_profits = stock_list[0][1]
    worst_portfolio = stock_list[0][0]

    for stock,stock_profit in stock_list:
        if stock_profit > highest_profits:
            highest_profits = stock_profit
            best_portfolio = stock
        if stock_profit < lowest_profits:
            lowest_profits = stock_profit
            worst_portfolio = stock

    print("Best portfolio: {}, Profits: ${}".format(best_portfolio,highest_profits))
    print("Worst portfolio: {}, Profits: ${}".format(worst_portfolio,lowest_profits))


if __name__ == '__main__':
    main()

