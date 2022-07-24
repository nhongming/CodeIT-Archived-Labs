import csv
from sys import argv


items = []
prices = []


'''
    This function should 
        1. Return a list containing all pairs of companies that sum up to budget
        2. Make use of a python dict / set (hash table)
        3. Have worst case time complexity O(N) [Assuming hash table insertion is constant]
'''
def doubles(companies, prices, budget):
    
    memo = {}
    for i, price in enumerate(prices):
        memo[price] = i

    results = []
    
    for i, price in enumerate(prices):
        targetPrice = budget - price
        if targetPrice in memo and targetPrice != price:
            results.append([
				companies[i], 
				companies[memo[targetPrice]]
			])

            if price in memo:
                del memo[price]
            if targetPrice in memo:
                del memo[targetPrice]

    return results



'''
    This function should
        1. Return a list containing all triplets of stock names with prices that sum up to budget
        2. It should call the doubles function
'''
def triples(companies, prices, budget):
    

    result = []

    for i in range(len(prices) - 2):
        targetPairPrice = budget - prices[i]
        res = doubles(companies[i + 1:], prices[i + 1:], targetPairPrice)

        for j in range(len(res)):
            res[j].append(companies[i])
            result.append(res[j])

    return result


def main():
    if len(argv) != 3:
        print('missing filename or budget as command line argument')
        return

    filename = argv[1]
    budget = int(argv[2])

    companies = []
    prices = []
    with open('prices/' + filename, 'r') as csv_file:
        myReader = csv.reader(csv_file)
        lineCount = 0
        for row in myReader:
            if lineCount == 0:
                lineCount += 1
                continue

            companies.append(row[0])
            prices.append(int(row[1]))


    print("doubles result:", doubles(companies, prices, budget))
    print()
    print("triples result:", triples(companies, prices, budget))

if __name__ == "__main__":
    main()

# def doublesBruteForce(items, prices, budget):
#     result = []
#     for i in range(len(prices) - 1):
#         for j in range(i + 1, len(prices)):
#             if prices[i] + prices[j] == budget:
#                 result.append([items[i], items[j]])

#     return result


# def triplesBruteForce(items, prices, budget):
#     result = []
#     for i in range(len(prices) - 2):
#         for j in range(i + 1, len(prices) - 1):
#             for k in range(j + 1, len(prices)):
#                 if prices[i] + prices[j] + prices[k] == budget:
#                     result.append([items[i], items[j], items[k]])

#     return result


# if __name__ == "__main__":
#     main()
