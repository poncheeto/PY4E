# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

try :
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    regular_pay = (hours) * (rate)

    if hours > 40 :
        overtime_hours = hours - 40
        print(overtime_hours)
        
        overtime_pay = (0.5 * overtime_hours) + regular_pay
        print('Pay: ', overtime_pay)
    else  :
        print('Pay: ', regular_pay)

except :
        print('Error, please enter a numeric input')
