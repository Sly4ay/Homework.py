# # a = 'Hello'
# # b = 'World'
#
# # print(a + ' ' + b, 1234 , True,sep='***', end='**\n')
#
# # print('afafa\nfafa')   #\n перенос строки
#
# # print('that\'s')          # \ символ эскейпа ( \\ ) эскейп символа эскейпа
#
#
# salary = 2000
# name = 'John'
# age = '25'
# txt = '{0}s salary is {1}. He is {2} years old'  # можно ставить индексы в скобках
# print(txt.format(name, salary, age))
#
#
#
# product = 'computer'
# price = 1000
# txt2 = 'This {product}, cost {price:.2f}'
#
# print(txt2.format(product=product, price=price))
#
# x = 1134.1414
# y = 123.132
# print('The value of x is %4.f' % x)
#
#
# print(f'Hi my name is {price}. Price is {product.upper()}')


x = -10
if x > 0:
    print('X is a positive number')
elif x < 0:
    print('X is a negative number')
else:
    print('X is a zero')

print('Goodbye')

idcode = '39605230195'

if len(idcode) == 11:
    print('Id is valid')
else:
    if len(idcode) > 11:
        print('Code is too long')
    else:
        print('Code is too short')



y = 10

if y > 0:
    print('Y is greater than 0')
elif y > 5:
    print('Y is greater than 5')
elif y > 9:
    print('Y is greater than 9')