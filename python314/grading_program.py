"""Module providing a function printing high"""

student_scores = {
    "Harry": 81,
    "Ron": 87,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grade = {}


# for key in student_scores:
#     if student_scores[key] > 90:
#         grade = "Outstanding"
#         student_grade[key] = grade
#     elif student_scores[key] > 80:
#         grade = "Exceeds Expectation"
#         student_grade[key] = grade
#     elif student_scores[key] > 70:
#         grade = "Pass"
#         student_grade[key] = grade
#     elif student_scores[key] > 60:
#         grade = "Fail"
#         student_grade[key] = grade

# OR

# for key in student_scores:
#     if student_scores[key] > 90:
#         student_grade[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         student_grade[key] = "Exceeds Expectation"
#     elif student_scores[key] > 70:
#         student_grade[key] = "Pass"
#     elif student_scores[key] > 60:
#         student_grade[key] = "Fail"


# OR

for key in student_scores:
    score = student_scores[key]
    if score > 90:
        student_grade[key] = "Outstanding"
    elif score > 80:
        student_grade[key] = "Exceeds Expectation"
    elif score > 70:
        student_grade[key] = "Pass"
    elif score > 60:
        student_grade[key] = "Fail"

print(student_grade)
