n=input('Введите число')
x=int(n)

if n == 0:
    print('Введен ноль')
elif isinstance(x, int) != True:
    print('Введена строка')

def f():

    return x/300

print(f())
