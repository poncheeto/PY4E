# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
regular_pay = int(hours) * float(rate)

if int(hours) > 40 :
    overtime_hours = int(hours) - 40
    print(overtime_hours)
    overtime_pay = (1.5 * int(overtime_hours)) + regular_pay
    print('Pay: ', overtime_pay)
else  :
    print('Pay: ', regular_pay)