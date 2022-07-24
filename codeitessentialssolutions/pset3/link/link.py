import csv
from sys import argv


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

def linkRecurse(parent, friends, user1, user2):

    if user1 == user2:
        return [user2]
        
    else:
        for v in friends[user1]:
            if v != parent:
                result = linkRecurse(user1, friends, v, user2)
                if result != None:
                    result.insert(0, user1)
                    return result
    return None

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
    if user1 not in friends:
        print('{} does not exist'.format(user1))
        return []
    elif user2 not in friends:
        print('{} does not exist'.format(user2))
        return []
    
    result = linkRecurse(None, friends, user1, user2)
    if result != None:
        return result
    else: 
        return []

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