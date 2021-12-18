import sys, random

alphabet = 'А Б В Г Д Е\
Ё Ж З І Й К Л М\
Н О П Р С Т У Ў\
Ф Х Ц Ч Ш Ы Ь Э\
Ю Я'
alphabet = list(alphabet.split())
alphabet = alphabet[::2]

file = open('C:\Users\nikit\Desktop\HW7.txt', 'w')
for i in range(len(alphabet)):
    file.write(alphabet[i] + '.\n')

print(sys.getsizeof('C:\Users\nikit\Desktop\HW7.txt'), '- количество байт')

file.close()

file = open('C:\Users\nikit\Desktop\HW7.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line.replace('\n',''), end=' ')
print(f'\n{len(lines)} - количество символов')
file.close()

file = open('C:\Users\nikit\Desktop\HW7.txt', 'r')
num = [i for i in range(1,10)]
lines = file.readlines()
a = 0
b = []
print(len(lines))
while a <= 10:
    b.append(lines[random.choice(num)])
    a += 1
print(b)


file2 = open('C:\Users\nikit\Desktop\HW7(1).txt', 'wt')
for i in b:
    file2.write(i.replace('\n', '') + ' ')

file2.close()
file.close()