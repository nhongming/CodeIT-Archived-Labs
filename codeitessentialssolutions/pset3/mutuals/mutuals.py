import csv
from sys import argv

'''
    getMutuals:
        - This function takes in the friends dictionary after it is loaded, as well as the names of two users
        - It should return a list containing all mutuals between user1 and user2
        - For instance, referring to friends1.csv, getMutuals("John", "Mark") -> ["Aran", "Daniel"]
        - If either of the users is not a key in the dictionary, or there are no mutuals, then it should return an empty array
        - Bonus: Can you implement the getMutuals function such that it runs in O(NlogN) time? Think about merge sort and how it takes O(NlogN) and how you can use that to implement your program! You are allowed to use the .sort() method in Python and may assume it runs in O(NlogN) time
'''
def getMutuals(friends, user1, user2):
    # TO IMPLEMENT
    if user1 not in friends or user2 not in friends:
        return []
    user1_friends = friends[user1]
    user2_friends = friends[user2]
    mutual_friends = []
    for friend1 in user1_friends:
        if friend1 in user2_friends:
            mutual_friends.append(friend1)
    if len(mutual_friends) == 0:
        return []
    else:
        return mutual_friends

# - Bonus: Can you implement the getMutuals function such that it runs in O(NlogN) time? 
def getMutuals(friends, user1, user2):
    # TO IMPLEMENT
    if user1 not in friends or user2 not in friends:
        return []
    user1_friends = sorted(friends[user1])
    user2_friends = sorted(friends[user2])
    count_user1_friends = len(user1_friends)
    count_user2_friends = len(user2_friends)

    i,j = 0,0
    mutual_friends = []
    while i < count_user1_friends and j < count_user2_friends:
        if user1_friends[i] < user2_friends[j]:
            i+=1
        elif user2_friends[j] < user1_friends[i]:
            j+=1
        else:
            mutual_friends.append(user2_friends[j])
            j+=1
            i+=1
    if len(mutual_friends) != 0:
        return mutual_friends
    else:
        return []

'''
    loadFriends:
        - This function should read in a file, where the filename is a command line argument
        - It should read each row of friendship and store it in the friends dictionary
        - The friends dictionary should operate such that it stores each user's name as a key, and the value is a list of his / her friends
        - For instance, according to friends.csv, the friends dictionary might look something like the following: 
            {
                'John': ['Aran', 'Daniel'], 
                'Mark': ['Luke', 'Daniel', 'Aran'],
                'Aran': ['John', 'Mark'],
                'Daniel': ['John', 'Mark'], 
                'Luke': ['Mark']
            }
        - Friendships are two ways. If Aran is in John's list of friends, then John should be in Aran's list of friends
'''
def loadFriends():
    friends = {}
    # TO IMPLEMENT
    with open(argv[1],'r') as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            user = row[0]
            friend = row[1]
            if user not in friends:
                friends[user] = [friend]
            else:
                friends[user].append(friend)
        
            if friend not in friends:
                friends[friend] = [user]
            else:
                friends[friend].append(user)
    return friends

# MAIN
def main():
    if len(argv) != 2:
        print('input a csv file')
        return 

    friends = loadFriends()
    print(friends)

    print("Input 2 users to find mutual friends between them!")
    user1 = input("User 1: ")
    user2 = input('User 2: ')
    
    print(getMutuals(friends, user1, user2))

if __name__ == '__main__':
    main()

