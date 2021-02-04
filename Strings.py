fruit = 'banana'


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
def count(word, letter):
    count = 0;
    for char in word:
        if char == letter:
            count += 1
    print(count)

count('banana', 'a')