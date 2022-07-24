import pathlib
import sys
import requests
import json

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from huffman import TreeNode, calculateFrequencies, createHuffmanTree, calculateCodes, encodeString

def flattenTree(treeShape, chars, node):
    assert isinstance(node, TreeNode), "Error: Huffman Tree contains nodes that aren't of type TreeNode, instead got {}".format(type(node))
    if not node.right and not node.left:
        # leaf node
        treeShape.append(0)
        chars.append(node.char)
    
    else:
        treeShape.append(1)
        # treeShape.append(node.symbol)
    if node.left: 
        flattenTree(treeShape, chars, node.left)
    if node.right:
        flattenTree(treeShape, chars, node.right)

def createSetOfResults(results, number, string):
    results[str(number)] = None
    results[str(number + 1)] = None
    results[str(number + 2)] = None
    results[str(number + 3)] = None

    try: 
        charFrequencies = calculateFrequencies(string)
        results[str(number)] = charFrequencies
    except:
        return

    try:
        root = createHuffmanTree(charFrequencies)
        assert isinstance(root, TreeNode), "Error: Huffman tree root (return) should be of type TreeNode, instead got {}".format(type(root))
        treeShape = []
        chars = []
        flattenTree(treeShape, chars, root)
        result2 = {
            "treeShape": treeShape,
            "chars": chars
        }
        results[str(number + 1)] = result2
    except Exception as e: 
        results[str(number + 1)] = str(e)
        return

    try: 
        result3 = calculateCodes(root)   
        results[str(number + 2)] = result3
    except: 
        return

    try:
        result4 = encodeString(string, result3)
        results[str(number + 3)] = result4
    except:
        return

    return


def getStudentResults():
    string1 = "AAAA BBB CCCCC DD"
    string2 = "HHHELLLLOOWWWWWWOOOOOOORRRRRRRRRLLLLLLLLLLDDDDDDDDDDD"
    string3 = "AAAABBBBBCCCCCCDDDDDDDEEEEEEEE"

    results = {}
    createSetOfResults(results, 1, string1)
    createSetOfResults(results, 5, string2)
    createSetOfResults(results, 9, string3)

    return results

def main():
    results = getStudentResults()

    res = requests.post("https://codeit-autograder.herokuapp.com/advanced/pset2/huffman", json=results)
    # res = requests.post("http://127.0.0.1:5000/advanced/pset2/huffman", json=results)
    res = res.json()

    report = res['report']
    for i in report:
        print(i)


if __name__ == "__main__":
    main()