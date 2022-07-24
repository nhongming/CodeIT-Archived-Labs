import signal
from time import time
import pathlib
import sys
import csv
import requests

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from stocks import doubles, triples

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

def load():
    filePath = "prices/"
    files = ['prices10.csv', 'prices20.csv',
             'prices100.csv', 'prices200.csv', 'prices500.csv']

    stocks = {}

    for file in files:
        path = filePath + file
        companies = []
        prices = []
        with open(path, 'r') as csv_file:
            myReader = csv.reader(csv_file)
            lineCount = 0
            for row in myReader:
                if lineCount == 0:
                    lineCount += 1
                    continue

                companies.append(row[0])
                prices.append(int(row[1]))

        stocks[file] = {
            "companies": companies,
            "prices": prices
        }

    return stocks

@deadline(6)
def runDoubles(companies, prices, budget):
    return doubles(companies, prices, budget)

@deadline(6)
def runTriples(companies, prices, budget):
    return triples(companies, prices, budget)

def getStudentSolutions():
    stocks = load()
    results = {}
    
    tests = [
        ('prices10.csv', 20),
        ('prices20.csv', 40),
        ('prices100.csv', 200),
        ('prices200.csv', 400),
        ('prices500.csv', 1000),
    ]
    
    count = 1
    for test in tests:

        test1 = count
        test2 = count + 6
        count += 1
        
        try:
            if test1 == 5:
                results[str(test1 + 1)] = None
            start = time()
            doubleRes = runDoubles(stocks[test[0]]["companies"],
                       stocks[test[0]]["prices"], test[1])
            results[str(test1)] = doubleRes
            end = time()
            if test1 == 5:
                results[str(test1 + 1)] = end - start
                
        except TimedOutExc:
            print("Timeout error on test {}, running function doubles, file: {}, budget: {}".format(
                test1, test[0], test[1]
            ))
            print("Are you sure your program is running in O(N) time?")
            return False
        except Exception as e:
            print("Runtime error on test {}".format(test1))
            print("Error: {}".format(str(e)))
            return False
        
        
        try:
            if test2 == 11:
                results[str(test2 + 1)] = None
            start = time()
            results[str(test2)] = runTriples(stocks[test[0]]["companies"],
                       stocks[test[0]]["prices"], test[1])
            end = time()
            if test2 == 11:
                results[str(test2 + 1)] = end - start
            
        except TimedOutExc:
            print("Timeout error on test {}, running function doubles, file: {}, budget: {}".format(
                test2, test[0], test[1]
            ))
            print("Are you sure your program is running in O(N^2) time?")
            return False
        except Exception as e:
            print("Runtime error on test {}".format(test2))
            print("Error: {}".format(str(e)))
            return False

    return results


def main():
    try:
        
        student_solutions = getStudentSolutions()
        if not student_solutions:
            return
        
        rootURI = "https://codeit-autograder.herokuapp.com"
        
        res = requests.post(rootURI + "/advanced/pset1/stocks", json=student_solutions)
        res = res.json()
        
        report = res['report']
        for i in report:
            print(i)
    except:
        print("failed to reach server")
    

if __name__ == "__main__":
    main()
