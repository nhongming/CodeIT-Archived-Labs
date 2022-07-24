import csv
from sys import argv
from linked_list import LinkedList


def main():
    # READ IN PATIENTS CSV FILE NAME
    if len(argv) < 2:
        print("Incorrect usage: python vaccinations.py <csv-filename>")
        exit()
    
    # INITIALIZE LINKED LIST 
    roster = LinkedList()

    # INSERT EACH PATIENT INTO ROSTER
    with open(argv[1], "r") as csv_file:
        reader = csv.reader(csv_file)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
                continue
            else:
                roster.insertByPriority(row[0], row[1])

    # PRINT ROSTER
    print("ROSTER:")
    roster.printList()

if __name__ == '__main__':
    main()