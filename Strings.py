# fruit = 'banana'

# # Exercise 1
# i = 0
# while i < len(fruit):
#     print(fruit[i])
#     i += 1

# for char in fruit:
#     print(char)

# # Exercise 2
# print(fruit[:])

# Exericse 3
# def count(word, letter):
#     count = 0;
#     for char in word:
#         if char == letter:
#             count += 1
#     print(count)

# count('banana', 'a')

# Exercise 4
# print(fruit.count('a'))

# Exercise 5
str = 'X-DSPAM-Confidence:0.8475'

posit1 = str.find(':')
print(posit1)

posit2 = str[posit1 + 1:]
print(posit2)

float_posit2 = float(posit2)
print(float_posit2)
print(type(float_posit2))