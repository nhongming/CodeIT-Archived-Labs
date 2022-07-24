from linked_list import LinkedList

def printResult(prev, current, next):
    if current == None:
        print("site not found")
        return
    
    if prev != None:
        print("previous site: {}".format(prev.value))
    else:
        print("previous site: nil")
    print("current site: {}".format(current.value))
    if next != None:
        print("next site: {}".format(next.value))
    else:
        print("next site: nil")

def searchLinkedList(siteToSearch, sites):
    cur = sites.head
    
    # if input is head
    if cur.value == siteToSearch:
        printResult(None, cur, cur.next)
        return
    
    prev = None
    current = None
    next = None
    
    # traverse linked list with prev, current and next
    while cur.next != None:
        if siteToSearch == cur.next.value:
            prev = cur
            current = cur.next
            
            # handle if current is last site
            if cur.next == None: next = None
            else: next = cur.next.next
            
            break
        cur = cur.next
    
    printResult(prev, current, next)

def printSites(sites):

    # TO IMPLEMENT
    print("last", end="")
    cur = sites.head
    while (cur != None):
        print(" <- {}".format(cur.value), end="")
        cur = cur.next
    print()
    return

# MAIN   
def main():
    sites = LinkedList()

    # READ IN LINKED LIST
    with open("sites.txt", "r") as file:
        for row in file:
            newSite = row.rstrip('\n')
            sites.insert(newSite)
        
    # PRINT THE LIST
    printSites(sites)

    # ASK FOR SITE TO SEARCH
    siteToSearch = input("search: ")
    siteToSearch = siteToSearch.lower()
    siteToSearch = "www." + siteToSearch + ".com"

    # SEARCH LINKED LIST
    searchLinkedList(siteToSearch, sites)

if __name__ == '__main__':
    main()


def printSites(sites):
    # TO IMPLEMENT
    pass

def searchLinkedList(siteToSearch, sites):
    # TO IMPLEMENT
    pass