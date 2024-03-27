lst=[1,2,3,4,5]
x=int(input('Введите число'))

if x in lst:
    print(lst)
    print('Ваше число: ',x)
    print('Вы угадали число!')
else:
    print(lst)
    print('Ваше число: ',x)
    print('Вы не угадали число')