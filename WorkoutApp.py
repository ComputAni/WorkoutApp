import plotly



def main():
	exerciseSet = set()
	targetDir = '/Users/ani/Dev/foo.txt'
	exerciseList = ["Deadlift","Bench", "Squat"]
	workoutDict = dict()
	for i in xrange(len(exerciseList)):
		workoutDict[exerciseList[i]] = []

	print workoutDict

	myF = open(targetDir,'r')

	for line in myF:
		splitLine = line.split()
		if (splitLine == []):
			print "Invalid workout! %s\n", workoutName
		workoutName = (splitLine[0])
		workoutName = workoutName[:len(workoutName)-1]
		print workoutName
		numExercises = len(splitLine)

		if (workoutName in workoutDict):
			#Grab all sets in workout except for workout name itself
			for i in xrange(numExercises,1,-1):
				workoutDict[workoutName].append(splitLine[i-1])
		else:
			print "Invalid workout! %s\n", workoutName


	print workoutDict

main()