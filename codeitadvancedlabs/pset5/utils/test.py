import pathlib
import sys
import requests
import json

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from dfa import buildDFA

def studentSolution():
    tests = [
        '', 'ANA', 'AABB', 'ABABC', 'HELLO, WORLD', 'FINITE & automata', 'aaaabbbbaaaacccc', 'teststring123'
    ]

    results = {}
    for i in range(len(tests)):
        res = buildDFA(tests[i])
        results[str(i + 1)] = res

    return results


        
def main():
    student_solutions = studentSolution()
    
    try:
        rootURI = "http://127.0.0.1:5000"
        rootURI = "https://codeit-autograder.herokuapp.com"
        res = requests.post(rootURI + "/advanced/pset5/dfa", json=student_solutions)
        res = res.json()
        report = res['report']
        for i in report:
            print(i)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()