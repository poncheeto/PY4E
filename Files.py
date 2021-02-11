# fhand = open('mbox.txt')
# print(fhand)

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count += 1
# print('Line Count:', count)

# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
    