# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    if score >= 0.9 :
        grade = 'A'
    elif score >= 0.8 :
        grade = 'B'
    elif score >= 0.7 :
        grade = 'C'
    elif score >= 0.6 :
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
    return grade

print(computegrade(.70))