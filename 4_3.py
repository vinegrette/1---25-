d=int(input('дата'))
m=int(input('месяц'))
g=int(input('год'))

def f():
    if d*m==g:
        return True
    else:
        return False

print(f())