#Для диапозона чисел от 0 до 100 включительно.
#Если число делится на 3 без остатка - написать число и Fizz
#Если число делится на 5 без остатка - написать число и Buzz
#Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz

for num in range(0, 101):
    if num % 5 == 0 and num % 3 == 0:
        print(num, 'fizzbuzz')
    elif num % 3 == 0:
        print(num, 'fizz')
    elif num % 5 == 0:
        print(num, 'buzz')
