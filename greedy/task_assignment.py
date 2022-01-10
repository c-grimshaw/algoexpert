def taskAssignment(k, tasks):
	# Get task indices
	taskIndices = {}
	for idx, task in enumerate(tasks):
		if task not in taskIndices:
			taskIndices[task] = []
		taskIndices[task] += [idx]
	
	# Sort tasks
	tasks.sort()
	
	# Select max and min task from tasks
	assignedTasks = []
	leftIdx, rightIdx = 0, len(tasks) -1
	while leftIdx <= rightIdx:
		assignedTasks.append([taskIndices[tasks[leftIdx]].pop(), taskIndices[tasks[rightIdx]]].pop())
		leftIdx += 1
		rightIdx -= 1

	return assignedTasks

taskAssignment(3, [1, 3, 5, 3, 1, 4])