def f(x):
    if x%4==0 and x%100!=0 and x%400!=0:
        return print('Год',x,'- високосный')
    else:
       return print('Этот год не високосный')

x=int(input('Введите год'))
print(f(x))
