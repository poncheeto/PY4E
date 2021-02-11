# fhand = open('mbox.txt')
# print(fhand)

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)