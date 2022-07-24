
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

    Your Task: Implement getPlayersInRange
        1. getPlayerInRange takes in:
            - min: minimum rating
            - max: maximum rating
            - players: BST of fifa players

        2. This function should search the players BST and return a dictionary which contains:
            - A key for each rating within the min and max rating, inclusive of both
            - The value for each key should be it's list of players (essentially the TreeNode's value)
'''


from bst import BST
import csv


def traverseAndPrint(node, min, max, result):
    if node == None:
        return
    if node.key >= min:
        traverseAndPrint(node.left, min, max, result)

    if node.key >= min and node.key <= max:
        result[node.key] = node.value
    if node.key <= max:
        traverseAndPrint(node.right, min, max, result)
    return


def getPlayersInRange(min, max, players):
    result = {}
    traverseAndPrint(players.root, min, max, result)
    return result


def main():
    players = BST()
    with open("players.csv", 'r') as csv_file:
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
