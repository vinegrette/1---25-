def f(n):
    if n%4==0 and n%100!=0 and n%400!=0:
        return print('Год',n,'- високосный')
    else:
       return print('Этот год не високосный')

x=int(input('Введите год'))
print(f(x))
