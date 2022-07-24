'''
    Recursion (Easy): Palindrome

    Your Tasks:
    Create a recursive function called isPalindromic which:
        1. Takes in a string as an argument
        2. Returns a boolean of True if the string is palindromic, and False if not
        3. Your function should make use of recursion
        4. You may assume that your string contains no white spaces
'''

def isPalindromic(string):
    #consider base case where string is a letter itself
    if len(string) <= 1:
        return True 
    else:
        if string[0] == string[-1]: #check of symmetrical letters located at each respective sides
            corr_string = string[1:-1] # check for inner string layers
            return isPalindromic(corr_string) # repeat the same procedure
        else:
            return False
'''
    main has been implemented for you to test out your function
'''
def main():
    string = input('check palindrome: ')
    print(isPalindromic(string))
    return

if __name__ == '__main__':
    main()
