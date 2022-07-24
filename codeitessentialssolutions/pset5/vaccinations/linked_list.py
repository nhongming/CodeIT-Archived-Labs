class ListNode():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def printList(self):
        cur = self.head
        tracker = 1
        while cur != None:
            print("{}. {} | {}".format(tracker, cur.name, cur.age))
            cur = cur.next
            tracker += 1
        return

    def insertByPriority(self, newName, newAge):
        # TO IMPLEMENT
        if self.size == 0 or newAge > self.head.age:
            newNode = ListNode(newName, newAge)
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return

        cur = self.head
        while cur.next != None and cur.next.age > newAge:
            cur = cur.next

        newNode = ListNode(newName, newAge)
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1
        return
        pass
