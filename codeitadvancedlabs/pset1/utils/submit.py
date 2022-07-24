import pathlib
import sys
from tkinter import E
import requests
from datetime import datetime, timedelta

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from test import getStudentSolutions

def getReplName():
	first = scriptDir.find("PSET")
	second = scriptDir.find("/utils")
	replName = scriptDir[first + 7:second]
	return replName

def submit():
    repl_username = getReplName()
    try:
        student_solutions = getStudentSolutions()
        if not student_solutions:
            return
        data = {
			"student_answers": student_solutions,
			"repl_username": repl_username
		}
        rootURI = "https://codeit-autograder.herokuapp.com"
        res = requests.post(rootURI + "/advanced/pset1/submit", json=data)
        if res.status_code != 200:
            print("Failed to submit assignment to server. Try again.")
            return
        res = res.json()
        print("Successfully submitted work. Grade: {}/100\nResults uploaded to report.txt".format(res["grade"]))
        
        textReport = res['textReport']
        today = datetime.today()
        today += timedelta(hours=8)
        with open('report.txt', 'w') as file:
            file.write("{}\n".format(today.strftime("%d %b %Y %H:%M")))
            for line in textReport:
                file.writelines(line)
    except Exception as e:
        print(e)
        return

if __name__ == "__main__":
	submit()