min = None
max = None

while True:
    str_value = input('Enter a number: ')
    if str_value == 'done':
        break
    try:
        int_value = int(str_value)
    except:
        print('Invalid input')
        continue

    if min is None or int_value < min:
        min = int_value
    elif max is None or int_value > max:
        max = int_value

print(min, max)