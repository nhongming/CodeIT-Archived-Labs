from heap import MinHeap

class TreeNode:
    def __init__(self, char, frequency, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

'''
    calculateFrequencies:
        - This function takes in the data string and returns a dictionary which 
        contains each character in the string as keys and it's frequency as the value
'''
def calculateFrequencies(data):
    # TO IMPLEMENT
    characters = {}

    for element in data:
        if element not in characters:
            characters[element] = 1
        
        else:
            characters[element] += 1
    
    return characters

'''
    createHuffmanTree:
        - This function takes in char frequencies and inserts each character as a TreeNode 
        into a MinPQ sorted according to character frequency
        - Then, while the PQ has more than one item:
            -> Extract the 2 min nodes and create a new tree node where its 
            left is the node with smallest frequency and right is the node with second smallest frequency
            -> Insert the new node back into the priority queue
        - Once the tree has been build, this function should return the root node of the tree
'''
def createHuffmanTree(charFrequencies):
    pq = MinHeap(len(charFrequencies))

    for char in charFrequencies:
        frequency = charFrequencies[char]
        newNode = TreeNode(char, frequency, None, None)
        pq.insert(newNode, frequency)
    
    while pq.size > 1:
        left = pq.getMin()
        right = pq.getMin()
        newNode = TreeNode('*', left.value + right.value, left.key, right.key)
        pq.insert(newNode, newNode.frequency)
    
    root = pq.getMin().key
    return root


'''
    calculateCodes:
        - This function takes in the root node from the Huffman tree
        - It should traverse the tree, and determine the code for each character in the string:
            -> A left path is considered '0'
            -> A right path is considered '1'
            -> Traverse a tree until you find a leaf node, and that character's code will be its path. 
            -> For instance, to get to C, we first go right, then left. Thus, C's code will be '10'
        - This function should should return a dictionary with each character as keys and it's code as the value
'''
def calculateCodes(huffmanRoot):
    codes = {}
    calculateCodesRecurse(codes, huffmanRoot, "")
    return codes
def calculateCodesRecurse(codes, node, val):
    if node.left:
        calculateCodesRecurse(codes, node.left, val + '0')
    if node.right:
        calculateCodesRecurse(codes, node.right, val + '1')
    if not node.right and not node.left:
        codes[node.char] = val


'''
    encodeString(data, codes):
        - This function takes in the original string (data) and the dictionary of codes for each char
        - It should return the string with each character replaced with its corresponding code
        - E.g. If we have:
            -> codes = {'A': '0', 'C': '10', 'B': '11'}
            -> message = "AAABBC"
            Our encoded string will be: "000111110"
'''   
def encodeString(data, codes):
    encodedString = ""
    for c in data:
        encodedString += codes[c]
    return encodedString
    
def HuffmanEncoding(data):
    
    # 1. Determine frequencies of characters
    charFrequencies = calculateFrequencies(data)

    # 2. Build Huffman tree
    huffmanRoot = createHuffmanTree(charFrequencies)

    # 3. Traverse Huffman tree to determine code for each char
    codes = calculateCodes(huffmanRoot)
    print("codes:", codes)

    # 4. Build encoded string using codes 
    encodedOutput = encodeString(data, codes)

    return encodedOutput, huffmanRoot

def main():
    
    data = input('input a string to encode via huffman: ')
    encoded_output, huffmanRoot = HuffmanEncoding(data)

    print('encoded data:', encoded_output)
    print('space usage before compression:', len(data) * 8)
    print('space usage after compression:', len(encoded_output))

if __name__ == '__main__':
    main()