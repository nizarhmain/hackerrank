

# grades between 0 and 100

# if grade < 40 => fail

# difference between next multiple of 5 and the grade < 3, round grade up to that multiple

# if grade < 38, no rounding happnes => fail

# 




def gradingStudents(grades):

	final = []

	for i in range(len(grades)):

		next_multiple = 0
	
		# keep increment until we found the multiple
		grade = grades[i]
		grade_counter = grades[i]
		
		while next_multiple == 0:
			grade_counter += 1
			if grade_counter % 5 == 0:
				next_multiple = grade_counter
			
		# fail them or pass them
		if next_multiple - grade < 3 and grade >= 38:
			grade = next_multiple
		
		final.append(grade)		
	
	return final



grades = [73, 67, 38, 33]

result = gradingStudents(grades)
print(result)










