# Prompt for user input
N = float(input("Please Input Number of Students: "))

#initiate no of students to 1
studno = 1

# empty weights list
weights = []
while studno <= N:
    student_input = float(input("Please Enter student "+str(studno)+"'s weight: "))
    wconvert = student_input * 0.45359237
    weights.insert(studno, wconvert)
    studno += 1
print("Weights:",weights)