def f(n):
    if n % 5 == 0:
        return 'делится на 5'
    else:
        return 'не иделится на 5'
print(f(int(input('Введите число'))))