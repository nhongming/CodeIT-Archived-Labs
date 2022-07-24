
import pathlib
import sys
import requests
import json

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from exchangeRates import exchangeRates
from arbitrage import arbitrage
from time import time

def studentSolution():
    results = {}
    for i, exchangeRate in enumerate(exchangeRates):
        if i == 7:
            start = time()
            res = arbitrage(exchangeRate)
            end = time()

            try:
                res.sort()
                results[str(i + 1)] = res
                results["9"] = end - start
            except:
                results[str(i + 1)] = None
            res = arbitrage(exchangeRate)
        
        else:
            res = arbitrage(exchangeRate)
            try:
                res.sort()
                results[str(i + 1)] = res
            except:
                results[str(i + 1)] = None

    return results


def main():
    student_solutions = studentSolution()

    
    
    rootURI = "http://127.0.0.1:5000"
    rootURI = "https://codeit-autograder.herokuapp.com"
    res = requests.post(rootURI + "/advanced/pset4/arbitrage", json=student_solutions)
    res = res.json()

    # print(res)
    report = res['report']
    for i in report:
        print(i)


if __name__ == "__main__":
    main()
