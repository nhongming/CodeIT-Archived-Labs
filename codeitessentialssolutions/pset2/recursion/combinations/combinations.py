from sys import argv

def combinationsHelper(results, res, names, i):

    # Base case when i has reached the end
    if i == len(names):
        results.append(res)
        return

    # Call function for which names[i] was not added
    combinationsHelper(results, res.copy(), names, i + 1)

    # Append and call function for which names[i] is added
    res.append(names[i])
    combinationsHelper(results, res, names, i + 1)
    
    return results

def combinations(names):
    return combinationsHelper([], [], names, 0)

'''
    main has been implemented for you to test out your function
'''
def main():
    if len(argv) != 2:
        print("Incorrect usage, pass in a text file")
        return
    names = []
    
    with open(argv[1], 'r') as txt_file:
        for row in txt_file:
            row = row.rstrip('\n')
            names.append(row)

    print(combinations(names))

if __name__ == '__main__':
    main()



