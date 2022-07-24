from datetime import datetime, timedelta
import pathlib
import sys
import requests

scriptDir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(scriptDir[:len(scriptDir) - 6])
sys.dont_write_bytecode = True

from test import studentSolution

def getReplName():
	first = scriptDir.find("PSET")
	second = scriptDir.find("/utils")
	replName = scriptDir[first + 7:second]
	return replName

def submit():
    repl_username = getReplName()

    try:
        student_solutions = studentSolution()
        data = {
			"student_answers": student_solutions,
			"repl_username": repl_username
		}
        rootURI = "http://127.0.0.1:5000"
        rootURI = "https://codeit-autograder.herokuapp.com"
        res = requests.post(rootURI + "/advanced/pset4/submit", json=data)
        if res.status_code != 200:
            print("Failed to submit assignment to server. Try again.")
            return
        res = res.json()
        print('''Successfully submitted work. Grade: {}/100.\nResults uploaded to report.txt'''.format(res["grade"]))
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