#------ Task 1.1------#
str_1 = '45851'
print('Answer_1.1:', str_1.isdigit())

#------ Task 1.2------#
str_2 = 'df  rgty 154 ht'
print('Answer_1.2:', str_2.count(' '))

#------ Task 1.3------#
str_3 = 'Jght. KJkr. 123.'
print('Answer_1.3:', str_3.count('.'))

#------ Task 1.4------#
str_4 = 'Homework'
str_4 = str_4.center(100, ' ')   # если добавлять пробелы то можно просто str_4 = str_4.center(100) без указания символа
print('Answer_1.4:', str_4)
print('  Length of str_4 = ', len(str_4))

#------ Task 1.5------#
str_5 = 'ergjjjhjsnfgiu irjgkv toijrt ok'
print('Answer_1.5:', str_5.title())

#------ Task 1.6------#
str_6 = 'Trying'
print('Answer_1.6:', str_6.endswith('ing'))

#------ Task 1.7------#
str_7 = 'pijervlqwrfjjaorg aa afo tky'
print('Answer_1.7:', str_7.find('a'))

#------ Task 1.8------#
str_8 = 'okfg ;trh er jjh wjwerj'
print('Answer_1.8:', str_8.split(' '))  # если разбивать по пробелу то можно просто str_8.split() без указания символа разделителя

#------ Task 1.9------#
str_9 = '  lkwg gtre Fryj 15963 Okjd     '
print('Answer_1.9:', (str_9.lstrip()).rstrip())

print ('******************************************************')

#------ Task 2.1------#
a = 367
b = 127
print('Answer_2.1:', (a**2 + b**2)**0.5)

#------ Task 2.2------#
a = 73
print('Answer_2.2:', a//10)

#------ Task 2.3------#
a = 951
print('Answer_2.3:', a//100 + a//10%10 + a%10)

#------ Task 2.4------#
a = 96
print('Answer_2.4:', (a+2) - a%2)

#------ Task 2.5------#
a = 156.93
print('Answer_2.5:', a - int(a))

#------ Task 2.6------#
a = 75.831
print('Answer_2.6:', int(a*10%10))

print ('******************************************************')
list_1 = ['rgd', 'Kjr15', 'PksD4f', 'world', 'koierg']

#------ Task 3.1------#
print('Answer_3.1:', list_1[-3])

#------ Task 3.2------#
print('Answer_3.2:', list_1[1][0])

#------ Task 3.3------#
print('Answer_3.3:', list_1[-1][-1])

#------ Task 3.4------#
list_1.append('Wjfgot')
print('Answer_3.4:', list_1)

#------ Task 3.5------#
list_1.insert((len(list_1)//2), '__New Item__')
print('Answer_3.5:', list_1)

#------ Task 3.6------#
del list_1[0]
print('Answer_3.6:', list_1)

#------ Task 3.7------#
list_1.remove('world')
print('Answer_3.7:', list_1)

print ('******************************************************')
dict_1 = {'title': 'Meal #1', 'price': 153.6, 'ingredients': ['meat', 'salt', 'pepper']}

#------ Task 4.1------#
dict_1['description'] = 'Ribeye Steak'
print('Answer_4.1:', dict_1)

#------ Task 4.2------#
dict_1['price'] += 100
print('Answer_4.2:', dict_1)

#------ Task 4.3------#
dict_1['ingredients'].append('oil')
print('Answer_4.3:', dict_1)

#------ Task 4.4------#
print('Answer_4.4:', 'amount of ingredients =', len(dict_1['ingredients']))

#------ Task 4.5------#
del dict_1['description']   # возможно использовать метод .pop(), тогда строка будет такой dict_1.pop('description')
print('Answer_4.5:', dict_1)