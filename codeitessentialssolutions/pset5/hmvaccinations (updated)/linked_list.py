class ListNode():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0 
        # self.queue = []
    
    def printList(self):
        cur = self.head
        tracker = 1
        while cur != None:
            print("{}. {} | {}".format(tracker, cur.name, cur.age))
            cur = cur.next
            tracker += 1
        return
    def insertByPriority(self, name, age):
        # TO IMPLEMENT

        # condition check for checking priority by descending age order
        # queue is empty or not
        if self.head == None:
            self.head = ListNode(name,age)
        else:

            # special condition check to see that 
            # first node priority value
            if self.head.age < age:

                # creating a new node
                newNode = ListNode(name, age)

                # updating the new node next value
                newNode.next = self.head

                #assigning it to self.front
                self.head = newNode

            else:
                # traversing through queue until it
                # finds the next larger priority node
                temp = self.head

                while temp.next:
                    # If same priority node found then current
                    # node will come after previous node
                    if age >= temp.next.age:
                        break

                    temp = temp.next
                
                newNode = ListNode(name,age)
                newNode.next = temp.next
                temp.next = newNode
        return