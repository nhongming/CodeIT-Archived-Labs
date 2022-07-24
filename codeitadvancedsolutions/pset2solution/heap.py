# HELPER FUNCTIONS
def parent(index):
    return index // 2


def left(index):
    return index * 2


def right(index):
    return index * 2 + 1


def swap(array, positions, index1, index2):
    key1 = array[index1].key
    key2 = array[index2].key
    positions[key1], positions[key2] = positions[key2], positions[key1]
    array[index1], array[index2] = array[index2], array[index1]


class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (maxsize + 1)
        self.positions = {}

    def greater(self, index1, index2):
        if self.heap[index1].value < self.heap[index2].value:
            return True
        else:
            return False

    def swim(self, index):

        while (index != 1 and self.greater(index, parent(index))):
            swap(self.heap, self.positions, index, parent(index))
            index = parent(index)

        return

    def insert(self, newKey, newValue):
        if self.size >= self.maxsize:
            print('size limit reached')
            return

        # HANDLE EXISTING KEY, NEW VALUE
        if newKey in self.positions:

            currentIndex = self.positions[newKey]
            self.heap[currentIndex].value = newValue

            if self.greater(currentIndex, parent(currentIndex)):
                self.swim(currentIndex)
            else:
                self.sink(currentIndex)

            return

        self.size += 1
        self.heap[self.size] = HeapItem(newKey, newValue)
        self.positions[newKey] = self.size

        self.swim(self.size)

    def sink(self, index):
        while (2 * index <= self.size):

            # initialize j to be left child
            j = left(index)

            # compare left and right
            if (j < self.size and self.greater(right(index), j)):
                j = right(index)

            if self.greater(index, j):
                break

            else:
                swap(self.heap, self.positions, j, index)
                index = j

        return

    def getMin(self):
        # SAVE MAX ITEM FOR REMOVAL
        maxItem = self.heap[1]

        # SWAP MAX ITEM
        swap(self.heap, self.positions, 1, self.size)

        # REMOVE ITEM
        self.heap[self.size] = None
        self.size -= 1

        # SINK FIRST ITEM
        self.sink(1)
        return maxItem
