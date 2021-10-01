print('------ Task 1------')
str_1 = input('Enter some text: ')
print(str_1[2], '\n', str_1[-2], '\n',
      str_1[0:5], '\n', str_1[0:-2], '\n',
      str_1[::2], '\n', str_1[1::2], '\n',
      str_1[::-1], '\n', str_1[::-2], '\n',
      str_1[-2::-2], '\n', str_1[-2:0:-1], '\n',
      len(str_1), sep='')

print('------ Task 2------')
str_2 = input('Enter some text: ')
if len(str_2) % 2 == 0:
      str_21 = str_2[(len(str_2)//2):] + str_2[0:(len(str_2)//2)]
else:
      str_21 = str_2[(len(str_2)//2)+1:] + str_2[0:(len(str_2)//2)+1]
print(str_21)

print('------ Task 3------')
YY = int(input('Enter year: '))
if YY % 4 == 0 or YY % 400 == 0 and YY % 100 != 0:
      print('YES')
else:
      print('NO')

print('------ Task 4------')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a + b > c and b + c > a and a + c > b:
      print('YES')
else:
      print('NO')

print('------ Task 5------')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a >= b:
      a,b = b,a
if a >= c:
      a,c = c,a
if b >= c:
      b,c = c,b
print(a, b, c)

print('------ Task 6------')
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
if a == b and b == c:
    print('3')
elif a == b or a == c or b == c:
    print('2')
else:
    print('0')

print('------ Task 7.1------')
x = 0
while x <= 10:
    print(x, end=' ')
    x += 1

print('\n------ Task 7.2------')
x = 20
while x > 0:
    print(x, end=' ')
    x -= 1

print('\n------ Task 7.3------')
x = int(input('Enter number: '))
i = 0
while x % 2 == 0:
    print(str(x))
    x //= 2
    i += 1
print('Number of iterations: ', i)


print('------ Task 8.1-----')
list_1 = ['rgd', 'Kjr15', 'PksD4f', 'world', 'koierg']
while len(list_1) > 0:
    print(list_1)
    list_1.pop(0)

print('------ Task 8.2-----')
str_3 = 'abcdefghijklmnopqrstuvwxyz'
while len(str_3) > 0:
    print(str_3)
    str_3 = str_3[1:]

print('------ Task 8.3-----')
list_1 = [54, 159, 12, 962, 3, 9]
print('Initial list: ', list_1)
while len(list_1) > 0:
    print('remove min element:', min(list_1), '-> ', end='')
    list_1.remove(min(list_1))
    print(list_1)

print('------ Task 9.1-----')
def is_year_leap(yy):
    if yy % 4 == 0 or yy % 400 == 0 and yy % 100 != 0:
        return True
    else:
        return False

year = int(input('Enter year: '))
print(is_year_leap(year))

print('------ Task 9.2-----')
def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False

a1 = int(input('Enter first number: '))
b1 = int(input('Enter second number: '))
c1 = int(input('Enter third number: '))
print(triangle(a1, b1, c1))

print('------ Task 10.1-----')
str_4 = 'We are not what we should be! ' \
        'We are not what we need to be. ' \
        'But at least we are not what we used to be'
print('Initial line: ', str_4)
tmp = str_4.split()
print('Number of words: ', len(str_4.split()))

print('------ Task 10.2-----')
for x in tmp:
    tmp_index = tmp.index(x)
    x = x.strip('.')
    x = x.strip(',')
    x = x.strip('!')
    tmp[tmp_index] = x
print(tmp)

print('------ Task 10.3-----')
print(sorted(tmp, key=str.lower))

print('------ Task 10.4-----')
dict_1 = {}
for x in range(len(tmp)):
    tmp[x] = tmp[x].lower()
    if tmp[x] not in dict_1:
        dict_1[tmp[x]] = tmp.count(tmp[x])
print(dict_1)