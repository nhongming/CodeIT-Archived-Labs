import pathlib
import signal
import sys
import requests
import json

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from dfa import buildDFA


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
def runDFA(substring):
    return buildDFA(substring)

def studentSolution():
    tests = [
        '', 'ANA', 'AABB', 'ABABC', 'HELLO, WORLD', 'FINITE & automata', 'aaaabbbbaaaacccc', 'teststring123'
    ]

    results = {}
    
    for i in range(len(tests)):
        
        try:
            res = runDFA(tests[i])
        except TimedOutExc:
            print("Timeout error on test {}, running buildDFA('{}')".format(str(i + 1), tests[i]))
            return False
        except Exception as e:
            print("Runtime error on test {}, running buildDFA('{}')".format(str(i + 1), tests[i]))
            print("Error: {}".format(str(e)))
            return False
        results[str(i + 1)] = res

    return results


        
def main():
    student_solutions = studentSolution()
    if not student_solutions:
        return
    
    try:
        # rootURI = "http://127.0.0.1:5000"
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