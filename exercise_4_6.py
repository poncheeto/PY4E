# Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters(hours and rate)
def computepay(hours, rate):
    pay = hours * rate
    return pay

hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
regular_pay = computepay(hours, rate)

if hours > 40 :
    overtime_hours = hours - 40
    overtime_pay = computepay(overtime_hours, (rate * 0.5)) + regular_pay
    print('Pay: ', overtime_pay)
else  :
    print('Pay: ', regular_pay)
