import pathlib
from re import I
import signal
import sys
import requests
import json

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from centrality import shortestPaths, betweennessCentrality

import csv

    
class TimedOutExc(Exception):
    pass

def deadline(timeout, *args):
    def decorate(f):
        def handler(signum, frame):
            raise TimedOutExc()

        def new_f(*args):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(timeout)
            return f(*args)
            signal.alarm(0)

        new_f.__name__ = f.__name__
        return new_f
    return decorate

@deadline(5)
def runShortestPaths(name, adjList):
    return shortestPaths(name, adjList)

@deadline(5)
def runBetweennessCentrality(adjList):
    return betweennessCentrality(adjList)

def studentSolution():
    files = ['network5.csv', 'network6.csv',
    'network7.csv', 'network8.csv', 'network19.csv']

    results = {}
    adjLists = {}

    for fileName in files:
        adjLists[fileName] = {}
        with open("networks/" + fileName) as csv_file:
            myReader = csv.reader(csv_file)
            for row in myReader:
                u, v = row[0], row[1]
                if u not in adjLists[fileName]:
                    adjLists[fileName][u] = []
                if v not in adjLists[fileName]:
                    adjLists[fileName][v] = []
                adjLists[fileName][u].append(v)
                
    tests = {
        1: ('Ann', adjLists["network5.csv"], "network5.csv"),
        3: ('Draco', adjLists["network6.csv"], "network6.csv"),
        5: ('Shawn', adjLists["network7.csv"], "network7.csv"),
        7: ('Jake', adjLists["network8.csv"], "network8.csv"),
        9: ('Noah', adjLists["network19.csv"], "network19.csv")
    }
    
    
    for i in range(1, 11, 2):
        test1 = i
        test2 = i + 1
        name, adjList, filename = tests[i]
        try:
            results[str(test1)] = runShortestPaths(name, adjList)
            
        except TimedOutExc:
            print("Runtime error on test {}, file: {}, function: shortestPaths('{}', adjList)".format(
                test1, filename, name
            ))
            return False
        except Exception as e:
            print("Timeout error on test {}, file: {}, function: shortestPaths({}, adjList)".format(
                test1, filename, name
            ))
            print("Error: {}".format(str(e)))
            return False
            
        try:
            results[str(test2)] = runBetweennessCentrality(adjList)
            
        except TimedOutExc:
            print("Timeout error on test {}, file: {}, function: betweennessCentrality".format(
                test2, filename
            ))
            return False
        except Exception as e:
            print("Runtime error on test {}, file: {}, function: betweennessCentrality".format(
                test2, filename
            ))
            print("Error: {}".format(str(e)))
            return False

    return results

def main():
    student_solutions = studentSolution()
    if not student_solutions:
        return
    
    rootURI = "http://127.0.0.1:5000"
    rootURI = "https://codeit-autograder.herokuapp.com"
    res = requests.post(rootURI + "/advanced/pset3/centrality", json=student_solutions)
    res = res.json()

    report = res['report']
    for i in report:
        print(i)

if __name__ == "__main__":
    main()