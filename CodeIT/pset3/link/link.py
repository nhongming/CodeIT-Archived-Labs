
'''
    Social Network (Hard): Link
'''

import csv
from sys import argv

'''
    getLink:
        - This function takes in the friends dictionary after it is loaded, as well as the names of two users
        - It should return the path between user1 to user2, if any, inclusive of user1 and user2
        - For instance, if John is friends with Alice and Alice is friends with Charlie, 
          getLink("John", "Charlie") -> ["John", "Alice", "Charlie"]        
        - If either of the users does not exist in the dictionary, or there is no link, then it should return an empty array
        - You may assume that no cycles exist in the network of friendships
        - You may assume that for any two users there will only be one link
'''
def getLink(friends, user1, user2):
    # TO IMPLEMENT
    user1_network = friends[user1]
    network_link = []
    for network in range(len(user1_network)):
        if user1_network[network] == user2:
            network_link.append(user1)
            network_link.append(user2)
        else:
            getLink(friends, network, user2)
    return network_link

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
    # TO IMPLEMENT
    with open(argv[1],'r') as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            user = row[0]
            network = row[1]
            if user not in network:
                friends[user] = [network]
            else:
                friends[user].append(network)
        
            if network not in friends:
                friends[network] = [user]
            else:
                friends[network].append(user)

    return friends


def main():
    if len(argv) != 2:
        print('input a csv file')
        return 

    friends = loadFriends() 

    print("Input 2 users to determine a link between them")
    user1 = input("User 1: ")
    user2 = input('User 2: ')

    print(getLink(friends, user1, user2))

if __name__ == '__main__':
    main()
