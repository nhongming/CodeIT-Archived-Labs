'''
    Fifa
        - main has been implemented for you to help you test your code
        - We read from our players.csv file
        - We store each row as a TreeNode in our players BST with overall rating as key and player name as value
        - Ask the user for a min and max rating
        - Call the getPlayersInRange function which searches our players BST and returns a dictionary where 
        each rating within our min and max, inclusive, is a key
        The list of players with that rating is a value
        - Print the result

    Your Task:
    
    getPlayersInRange
        - getPlayersInRange takes in:
            -> min: minimum rating
            -> max: maximum rating
            -> players: BST of fifa players
        - This function should search the players BST and return a dictionary which contains:
            -> A key for each rating within the min and max rating, inclusive of both
            -> The value for each key should be it's list of players (essentially the TreeNode's value)
'''

from bst import BST
import csv

def getPlayersInRange(min, max, players):
    # TO IMPLEMENT
    filter_results = {}
    if players.root == None:
        return
    else:
        for rating in range(min, max + 1):
            # filtering for values of min or max out of the given permissible range
            # that is currently stored by players BST
            if players.search(rating) != None: 
                matching_node = players.search(rating) # search() BST Class method handles the matching here as implemented by bst.py
                matched_rating = matching_node.key
                matched_players_arr = matching_node.value
                if matched_rating not in filter_results:
                    filter_results[matched_rating] = matched_players_arr
    return filter_results


def main():
    players = BST()
    with open("players.csv", 'r', encoding='utf8') as csv_file:
        reader = csv.reader(csv_file)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
                continue
            playerName = row[0]
            playerRating = int(row[1])
            players.insert(playerRating, playerName)

    min = int(input("min: "))
    max = int(input("max: "))
    print(30 * '-')

    searchResult = getPlayersInRange(min, max, players)
    for rating in searchResult:
        print('overall: {}'.format(rating))
        print(searchResult[rating])
        print()


if __name__ == '__main__':
    main()
