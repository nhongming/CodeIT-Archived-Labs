from linked_list import LinkedList
from sys import argv

'''
    Browser (Easy)

    Your Task

    1. printSites:
        - printSites takes in the linked list sites
        - Implement the printSites function such that it prints the linked list of sites like so:
        "last <- www.netflix.com <- www.instagram.com <- www.spotify.com <- www.twitter.com <- www.facebook.com <- www.google.com"
    
    2. navigate:
        - simulate the list of clicks, starting from the last site visited, netflix, and return the site reached. 
        - A "b" stands for backwards. For instance, if you were on netflix, and "b" is encountered, you should move to instagram
        - An "f" stands for forwards. For instance, if you were on instagram, and "f" is encountered, you should move to netflix

    Note: If a forward click is performed when you are on the last site or a backwards click is performed when you are on the first site, ignore that click. For instance, if you are on netflix and you read an “f”, you should remain at netflix
'''


def navigate(sites, clicks):
    # TO IMPLEMENT
    pass
            
def printSites(sites):
    # TO IMPLEMENT
    pass

def main():  
    if len(argv) < 0:
        print("incorrect usage: python browser2.py <txt-file>")
        exit()
        
    sites = LinkedList()
    clicks = []

    # READ IN LINKED LIST
    with open("sites.txt", "r") as file:
        for row in file:
            sites.insert(row.rstrip('\n'))

    # READ IN CLICKS
    with open(argv[1], "r") as file:
        for row in file:
            clicks.append(row.rstrip("\n"))
            
    # PRINT THE LIST
    printSites(sites)

    # NAVIGATE THROUGH THE LIST
    reached = navigate(sites, clicks)
    print("reached: {}".format(reached.value))

if __name__ == '__main__': 
    main()