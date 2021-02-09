# numlist = list()

# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
    
# average = sum(numlist) / len(numlist)
# print('Average: ', average)

# # Exercise 6.1
# def chop(t):
#     t = t[1:(len(t) - 1)]

# print(chop([1, 2, 3, 4]))

# def middle(t):
#     return t[1:(len(t) - 1)]

# print(middle([1, 2, 3, 4,]))

t = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = int(inp)
    t.append(value)
    max_value = max(t)
    min_value = min(t)

print('Maximum:', max_value)
print('Minimum:', min_value)
