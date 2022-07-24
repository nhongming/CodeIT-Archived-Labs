'''
    Browser (Easy)

    Your Task

    1. printSites:
        - printSites takes in the linked list sites
        - Implement the printSites function such that it prints the linked list of sites like so:
        "last <- www.netflix.com <- www.instagram.com <- www.spotify.com <- www.twitter.com <- www.facebook.com <- www.google.com"
    
    2. searchLinkedList:
        - searchLinkedList takes in the linked list sites, and siteToSearch, the url of the site inputted by the user (e.g. "www.facebook.com")
        - Note: the user only needs to input the name of the site ("facebook"). We have concatenated the "www." and ".com" before passing it into the searchLinkedList function
        - This function should search the linked list and print in the format below:
            "
                previous site: <site before siteToSearch>
                current site: <siteToSearch>
                next site: <site after siteToSearch>
            "

    Note: 
        - If the site visited is the first site (i.e. google), your previous site will be nil
        - If the site visited is the last site (i.e. netflix), your next site will be nil
        - If the site visited is not found, print “site not found”
'''

from linked_list import LinkedList


def printSites(sites):
    # TO IMPLEMENT
    currentNode = sites.head
    to_print = ""
    while currentNode is not None:
        to_print = to_print + currentNode.value + " <- "
        currentNode = currentNode.next
    print(to_print.rstrip(' <- '))

def searchLinkedList(siteToSearch, sites):
    # TO IMPLEMENT
    if not sites.search(siteToSearch):
        print('site not found')
    else:        
        found = False
        current = sites.head
        previous = None
        next = None
        index_count = 0
        while current != None and not found:
            if current.value == siteToSearch:
                if current.value == sites.getNodeAt(0).value:
                    previous = current.next.value
                    next =  'nil'
                elif current.value == sites.getNodeAt(sites.size - 1).value:
                    previous = 'nil' 
                    next = sites.getNodeAt(sites.size - 2).value
                else:
                    previous = current.next.value
                    next = sites.getNodeAt(index_count-1).value

                found = True

            index_count += 1
            current = current.next

        print(f"previous site: {previous}", end="\n")
        print(f"current site: {siteToSearch}", end="\n")
        print(f"next site: {next}")

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