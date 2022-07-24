import csv
from sys import argv

'''
    This function should 
        1. Return a list containing all pairs of companies that sum up to budget
        2. Make use of a python dict / set (hash table)
        3. Have worst case time complexity O(N) [Assuming hash table insertion is constant]
'''
def doubles(companies, prices, budget):
    # TO IMPLEMENT
    matched_companies_pairs = []
    matching_hashmap = dict()

    companies_portfolio = {}
    for company,price in zip(companies,prices):
        if price in companies_portfolio:
            companies_portfolio[price].append(company)
        else:
            companies_portfolio[price] = company

    for company,price in zip(companies,prices):
        target_price = budget - price
        if target_price in matching_hashmap:
            price_index = matching_hashmap[target_price]
            if price_index > 1:
                for j in range(companies_portfolio[target_price]):
                    matched_companies_pairs.append([companies_portfolio[target_price][j],company])
            else:
                matched_companies_pairs.append([companies_portfolio[target_price],company])
        if price in matching_hashmap:
            matching_hashmap[price]+=1
        else:
            matching_hashmap[price]=1
    
    return matched_companies_pairs


'''
    This function should
        1. Return a list containing all triplets of stock names with prices that sum up to budget
        2. Have worst case time complexity O(N^2) [Assuming hash table insertion is constant]

    Hint: If your doubles function runs in O(N) time, think about how you can call it in triples
'''
def triples(companies, prices, budget):
    # TO IMPLEMENT
    matched_companies_triplets = []
    arr_size = len(companies)

    companies_portfolio = {}
    for company,price in zip(companies,prices):
        if price in companies_portfolio:
            companies_portfolio[price].append(company)
        else:
            companies_portfolio[price] = company

    for i in range(0,arr_size-1):
        matching_hashmap = set()
        curr_target_price = budget-prices[i]
        for j in range(i+1,arr_size):
            if (curr_target_price-prices[j]) in matching_hashmap:
                matched_companies_triplets.append([companies_portfolio[prices[i]],companies_portfolio[prices[j]],companies_portfolio[curr_target_price-prices[j]]])
            matching_hashmap.add(prices[j])

    return matched_companies_triplets


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
