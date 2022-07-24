
import os
import sys
import pathlib
scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True
from tictactoe_hard import main

class Colors:
    GREEN = "\033[92m"
    RED = '\033[91m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test(boardSize, testNumber, expectedResult):

    # RUN PROGRAM
    sys.argv[1] = boardSize

    try:
        testFileName = 'tests/t' + str(testNumber) + '.txt'
        sys.stdin = open(testFileName, 'r')
        sys.stdout = open('tests/output.txt', 'w')
        main()

        sys.stdout.close()
        sys.stdout = sys.__stdout__

        c = sys.stdin.readline()
        if c != 'end':
            print(Colors.RED + 'TEST {} FAILED: '.format(testNumber), end='')
            return

    except Exception as e:
        sys.stdin.close()
        sys.stdout.close()
        sys.stdout = sys.__stdout__
        print(Colors.RED + 'TEST {} FAILED: '.format(testNumber), end='')
        print(e)
        return

    sys.stdin.close()

    # GET LAST LINE OF OUTPUT
    try:
        f = open('tests/output.txt', 'rb')
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        result = f.readline().decode()
        result = result.rstrip('\n')

        # COMPARE RESULT
        if result.find(expectedResult) != -1:
            print(Colors.GREEN + 'TEST {} PASSED:'.format(testNumber), end=' ')
        else:
            print(Colors.RED + 'TEST {} FAILED:'.format(testNumber), end=' ')
    except:
        print(Colors.RED + 'TEST {} FAILED: '.format(testNumber), end='')

if __name__ == '__main__':

    # INITIALIZE CLA
    sys.argv.append('3')

    # TEST CASE 1: 3x3 BOARD, HORIZONTAL
    test(boardSize=3, testNumber=1, expectedResult='winner')
    print('3x3 BOARD, HORIZONTAL')

    # TEST CASE 2: 3x3 BOARD, HORIZONTAL
    test(boardSize=3, testNumber=2, expectedResult='winner')
    print('3x3 BOARD, VERTICAL')

    # TEST CASE 3: 3x3 BOARD, HORIZONTAL
    test(boardSize=3, testNumber=3, expectedResult='winner')
    print('3x3 BOARD, DIAGONAL')

    # TEST CASE 4: 3x3 BOARD, NO WINNER
    test(boardSize=3, testNumber=4, expectedResult='no winner')
    print('3x3 BOARD, NO WINNER')

    # TEST CASE 5: 4x4 BOARD, NO WINNER
    test(boardSize=4, testNumber=5, expectedResult='winner')
    print('4x4 BOARD, HORIZONTAL')

    # TEST CASE 5: 4x4 BOARD, NO WINNER
    test(boardSize=4, testNumber=6, expectedResult='winner')
    print('4x4 BOARD, VERTICAL')
