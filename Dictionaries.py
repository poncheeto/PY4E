# # Exercise 1 
# fhand = open('words.txt', 'r')

# lines = []
# word_dict = dict()

# for line in fhand:
#     lines.append(line)
#     for line in lines:
#         line_words = line.split()
#         for word in line_words:
#             word_dict[word] = word

# fhand.close()
# print('skills' in word_dict)
# print('data' in word_dict)
# print('possum' in word_dict)

word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)