students = [["Samuel", 80, 75, 90], ["David", 55, 60, 50], ["Mary", 35, 40, 30], ["John", 65, 70, 68]]
grade = ""

for student in students:
    average = (student[1] + student[2] + student[3]) / 3
    appr_avg = round(average, 2)
    if average >= 70:
        grade = "A"
    elif average >= 60 and average <= 69:
        grade = "B"
    elif average >= 50 and average <= 59:
        grade = "C"
    elif average >= 40 and average <= 49:
        grade = "D"
    else:
        grade = "F"

    out = print (f"{student[0]} --> Average: {appr_avg} --> Grade: {grade}")

print (out)