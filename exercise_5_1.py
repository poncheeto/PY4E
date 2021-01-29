count = 0
total = 0

while True:
    str_value = input('Enter a number: ')
    if str_value == 'done':
        break
    try:
        int_value = int(str_value)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + int_value
    average = total / num
print(total, count, average)