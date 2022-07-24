from linked_list import LinkedList
from sys import argv

def navigate(sites, clicks):
    stack = LinkedList()
    currentSite = sites.head
    
    for click in clicks:
        if click == "b" and sites.size != 0:
            stack.insert(currentSite.value)
            sites.delete()
            currentSite = sites.head
        elif click == "f" and stack.size != 0:
            tmp = stack.head
            stack.delete()
            sites.insert(tmp.value)
            currentSite = sites.head
        else:
            continue
    
    if currentSite == None:
        return stack.head

    return currentSite
            
def printSites(sites):
    
    # TO IMPLEMENT
    print("last", end="")
    cur = sites.head
    while (cur != None):
        print(" <- {}".format(cur.value), end="")
        cur = cur.next
    print()
    return


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