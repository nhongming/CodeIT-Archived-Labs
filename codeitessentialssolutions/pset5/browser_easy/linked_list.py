class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def getNodeAt(self, index):
        if (index < 0 or index > self.size):
            print("invalid index")
            return None
        
        cur = self.head
        while (index != 0):
            cur = cur.next
            index -= 1
        return cur

    def insert(self, item):
        newNode = ListNode(item)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        return
            
    
    def delete(self):
        self.head = self.head.next
        self.size -= 1