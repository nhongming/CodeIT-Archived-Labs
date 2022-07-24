'''
    Recursion (Hard): Combinations

    Your Tasks:
    Create a recursive function called isPalindromic which:
    Implement the combinations function
    It should take in a list of names, and output a 2D list containing every possible combination made from that list of names
    It should make use of recursion
Example: combinations(['A', 'B', 'C']) -> [[], ['C'], ['B'], ['B', 'C'], ['A'], ['A', 'C'], ['A', 'B'], ['A', 'B', 'C']]
'''

def combinations(names):
    # WRITE YOUR CODE HERE
    #consider the base case where the array is empty
    if not names:
        return [[]]
    else:
        combo = combinations(names[:-1])
        return combo + [c + [names[-1]] for c in combo]

    
from sys import argv
def main():
    if len(argv) != 2:
        print("Pass in a text file")
        return

    names = []
    with open(argv[1], 'r') as txt_file:
        for row in txt_file:
            row = row.rstrip('\n')
            names.append(row)

    print(combinations(names))


if __name__ == '__main__':
    main()