'''
NOTE 1: The number of unique characters is given in a constant variable. Do make use of this to initialise your 2D list!
'''

NO_OF_CHARS = 256

'''
NOTE 2: To convert a character to it's ASCII number, you can use the ord() function in python, and to convert from it, you can use the chr() function
'''
# ord('A') # convert char to ascii number: 65
# chr(65)  # convert ascii number to char: 'A'

'''
    - This function takes in a substring and builds the appropriate finite automata for the KMP string matching algorithm
    - It should return the DFA as a 2D list, with 256 rows (number of ASCII characters) and M (length of substring) + 1 columns, which is the number of states
    - All values in the last column (final state) should be 0
    - All values in rows of chars not in the substring should be 0
'''

def buildDFA(substring): # build DFA for KMP
    # TO IMPLEMENT 
    M = len(substring)  # length of pattern
    dfa = [[0 for x in range(M + 1)] for y in range(NO_OF_CHARS)]   # dfa[R][M]
    if len(substring) != 0: # if pattern is not empty   
        dfa[ord(substring[0])][0] = 1   # set first state to 1
        x = 0   # index of pattern
        for state in range(1,M):    # for each state
            for j in range(NO_OF_CHARS):    # for each character
                dfa[j][state] = dfa[j][x] # Copy mismatch cases
            dfa[ord(substring[state])][state] = state+1 # Set match case
            x = dfa[ord(substring[state])][x]   # Update restart state
    return dfa

def KnuthMorrisPratt(text, substring):  # KMP algorithm
    dfa = buildDFA(substring)   # build DFA for KMP
    i = 0   # index of text
    j = 0   # index of substring
    M = len(substring)  # length of substring

    while (i < len(text)):  # while text is not empty
        charIndex = ord(text[i])    # get index of current character
        j = dfa[charIndex][j]   # get next state

        if j == M:  # if substring is found
            print("substring found at index {}".format(i - (M - 1)))    # print index of substring
            j = 0   # reset state
            i = i - M + 1   # reset index of text
        
        i += 1  # increment index of text

def main():
    substring = input('substring: ')
    text = input('text: ')
    KnuthMorrisPratt(text, substring)

if __name__ == '__main__':
    main()

""" Here is the explanation for the code above:
1. We first build the DFA for the substring.
2. We then use the DFA to find the index of the substring in the text.
3. We then print the index of the substring.
4. We then reset the index of the text to the index of the substring minus the length of the substring plus one.
5. We then increment the index of the text.
6. We then repeat the process until the text is empty. """

## JAVA to PYTHON IMPLEMENTATION ##

"""
The KMP algorithm finds the first occurrence of a pattern string in a text string.

This implementation uses a version of the Knuth-Morris-Pratt substring search algorithm.
The version takes time proportional to n + m R in the worst case, where n is the length of the text string,
m is the length of the pattern, and R is the alphabet size.
It uses extra space proportional to m R.

For additional documentation, see
https://algs4.cs.princeton.edu/53substring
"""

## PSEUDOCODE ##

class KMP:
    def __init__(self, pat):
        self.R = 256
        self.pat = pat
        self.dfa = [[0] * len(pat) for _ in range(self.R)]
        self.dfa[ord(pat[0])][0] = 1
        for x in range(self.R):
            for j in range(len(pat)):
                self.dfa[x][j] = self.dfa[x][self.dfa[x][j - 1]]
                if j > 0:
                    self.dfa[ord(pat[j])][j] = j + 1
        self.dfa[ord(pat[-1])][-1] = len(pat)
    def search(self, txt):
        m = len(self.pat)
        n = len(txt)
        i = 0
        j = 0
        while i < n:
            j = self.dfa[ord(txt[i])][j]
            if j == m:
                return i - m + 1
            i += 1
        return -1

class KMP:
    def __init__(self, pattern, R):
        self.R = R
        self.m = len(pattern)
        self.dfa = [[0 for j in range(self.m)] for i in range(self.R)]
        self.dfa[ord(pattern[0])][0] = 1
        for x in range(0, self.m):
            for c in range(self.R):
                self.dfa[c][x] = self.dfa[c][x-1]
            self.dfa[ord(pattern[x])][x] = x+1
        return

import sys  

class KMP:
    def __init__(self, pat):
        self.R = 256
        self.m = len(pat)
        self.dfa = [[0] * self.m for _ in range(self.R)]
        self.dfa[ord(pat[0])][0] = 1
        for x in range(0, self.m):
            for c in range(self.R):
                self.dfa[c][x] = self.dfa[c][x - 1]
            self.dfa[ord(pat[x])][x] = x + 1
        return

    def search(self, txt):
        n = len(txt)
        i, j = 0, 0
        for i in range(n):
            j = self.dfa[ord(txt[i])][j]
            if j == self.m:
                return i - self.m
        return n

    def main(self, args):
        pat = args[0]
        txt = args[1]
        pattern = pat.encode('utf-8')
        text = txt.encode('utf-8')
        kmp1 = KMP(pat)
        offset1 = kmp1.search(txt)
        kmp2 = KMP(pattern, 256)
        offset2 = kmp2.search(text)
        # print results
        print("text:    " + txt)
        print("pattern: ")
        for i in range(offset1):
            print(" ", end='')
        print(pat)
        print("pattern: ")
        for i in range(offset2):
            print(" ", end='')
        print(pat)
        return


if __name__ == '__main__':
    KMP.main(sys.argv[1:])

""" https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/ """

### Not 100% foolproof ### 
### Passed all test cases except test case 7 & 8 ###

# def getNextState(pat, M, state, x): 
#     '''
#     calculate the next state
#     '''
#     # If the character c is same as next character
#     # in pattern, then simply increment state    
#     if state < M and x == ord(pat[state]):  # if state is less than M and x is equal to the character in the pattern
#         return state + 1            
#     i=0 # else, start from the beginning of the pattern
#     # ns stores the result which is next state

#     # ns finally contains the longest prefix
#     # which is also suffix in "pat[0..state-1]c"

#     # Start from the largest possible value and
#     # stop when you find a prefix which is also suffix
#     for ns in range(state, 0,-1):
#         if x == ord(pat[ns-1]):
#             while(i<ns-1):  
#                 if pat[i]!=pat[state-ns+i+1]:
#                     break   
#                 i+=1    
#             if i == ns-1:   
#                 return ns   
#     return 0

# def buildDFA(substring):    # build DFA for KMP
#     # TO IMPLEMENT 
#     M = len(substring)
#     dfa = [[0 for x in range(M + 1)] for y in range(NO_OF_CHARS)]
#     for x in range(NO_OF_CHARS):
#         for state in range(M): 
#             dfa[x][state] = getNextState(substring, M, state, x)
#     return dfa