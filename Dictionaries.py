# # # Exercise 1 
# fhand = open('words.txt')

# word_dict = dict()

# for line in fhand:
#     words = line.split()
#     for word in words:
#         word_dict[word] = word

# print('skills' in word_dict)
# print('data' in word_dict)
# print('possum' in word_dict)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] += 1
# print(d)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# print(d)

# Exercise 
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
days = dict()
for line in fhand:
    if line.startswith('From'):
        line = line.rstrip()
        print(line)
