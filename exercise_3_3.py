# Write a program to prompt for a score between 0.0 and1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
    # >= 0.9A >= 0.8B >= 0.7C >= 0.6D < 0.6F

grade = float(input('Enter your grade: '))

try :
    if grade >= 0.0 and grade<= 1.0 :
        if grade >= 0.9 :
            print('A')
        elif grade >= 0.8 :
            print('B')
        elif grade >= 0.7 :
            print('C')
        elif grade >= 0.6 :
            print('D')
        elif grade < 0.6:
            print('F')
    else :
        print('Bad score')
except :
        print('Bad score')
