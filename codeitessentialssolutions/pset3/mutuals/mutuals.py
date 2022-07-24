import csv
from sys import argv


def addFriends(friends, friend1, friend2):
    # add to friend1's list
    if friend1 in friends:
        friends[friend1].append(friend2)
    else:
        friends[friend1] = []
        friends[friend1].append(friend2)


def getMutuals(friends, user1, user2):
    if user1 not in friends:
        return []
    elif user2 not in friends:
        return []

    # O (N^2) Solution
    # mutuals = []

    # list1 = friends[user1]
    # list2 = friends[user2]

    # for friend in list1:
    #     for mutual in list2:
    #         if mutual == friend and mutual != user2:
    #             mutuals.append(mutual)
    #             break

    # O (N logN) Solution
    list1 = sorted(friends[user1])
    list2 = sorted(friends[user2])

    mutuals = []
    n1, n2, i = 0, 0, 0

    while n1 < len(list1) and n2 < len(list2):
        if list1[n1] == list2[n2] and list1[n1]:
            mutuals.append(list1[n1])
            i += 1
            n1 += 1
            n2 += 1
        elif list1[n1] < list2[n2]:
            n1 += 1
        else:
            n2 += 1

    return mutuals


'''
    loadFriends:
        - This function should read in a file, where the filename is a command line argument
        - It should read each row of friendship and store it in the friends dictionary
        - The friends dictionary should operate such that it stores each name as a key, and the value is a list of his / her friends
        - For instance, according to network1.csv, the friends dictionary might look something like the following: 
            {
                'John': ['Alice'], 
                'Alice': ['John', 'Charlie', 'Daniel'], 
                'Charlie': ['Alice'], 
                'Daniel': ['Alice'], 
                'Jake': ['Jerome'], 
                'Jerome': ['Jake']
            }
        - Friendships are two ways. If Alice is in John's list of friends, then John should be in Alice's list of friends
'''


def loadFriends():
    friends = {}

    with open(argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] not in friends:
                friends[row[0]] = []
            if row[1] not in friends:
                friends[row[1]] = []

            friends[row[0]].append(row[1])
            friends[row[1]].append(row[0])

    return friends


# MAIN
def main():
    if len(argv) != 2:
        print('input a csv file')
        return

    friends = loadFriends()

    print("Input 2 users to find mutual friends between them!")
    user1 = input("User 1: ")
    user2 = input('User 2: ')

    print(getMutuals(friends, user1, user2))


if __name__ == '__main__':
    main()
