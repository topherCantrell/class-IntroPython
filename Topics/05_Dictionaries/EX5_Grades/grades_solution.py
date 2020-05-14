
my_grades = {
    'Jan' : 75,
    'Bob' : 88,
    'Jill' : 52,
    'Pat' : 99
}

def find_highest(data):
    high_grade = -1
    for student in data:
        if data[student] > high_grade:
            high_grade = data[student]
            high_student = student
    return student
    
highest = find_highest(my_grades)

print('Highest grade is '+str(my_grades[highest])+' made by '+highest+'.')