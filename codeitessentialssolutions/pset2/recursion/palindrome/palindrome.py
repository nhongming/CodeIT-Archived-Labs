'''
    Recursion (Easy): Palindrome

    Your Tasks:
    Create a recursive function called isPalindromic which:
        1. Takes in a string as an argument
        2. Returns a boolean of True if the string is palindromic, and False if not
        3. Your function should make use of recursion
        4. You may assume that your string contains no white spaces
'''

def isPalindromicRecurse(string, lo, hi):
    if lo >= hi:
        return True
    
    elif string[lo] == string[hi]:
        return isPalindromicRecurse(string, lo + 1, hi - 1)

    else:
        return False

def isPalindromic(string):
    return isPalindromicRecurse(string, 0, len(string) - 1)

'''
    main has been implemented for you to test out your function
'''
def main():
    string = input('check palindrome: ')
    print(isPalindromic(string))
    return

if __name__ == '__main__':
    main()

