# Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters(hours and rate)
def computepay(hours, rate):
    pay = float(hours) * rate
    return pay

try :
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    regular_pay = (hours) * (rate)

    if hours > 40 :
        overtime_hours = hours - 40
        
        overtime_pay = ((0.5 * rate) * overtime_hours) + regular_pay
        print('Pay: ', overtime_pay)
    else  :
        print('Pay: ', regular_pay)

except :
        print('Error, please enter a numeric input')
