import random
kn=0
ko=0
while kn<3:
    n1=random.randint(1,10)
    n2=random.randint(1,10)

    r=int(input('{n1} + {n2} = '.format(n1=n1,n2=n2)))
    if r==n1+n2:
        print('Правильно!')
        ko+=1
    else:
        print('Ответ неверный')
        kn+=1

print('Игра окончена. Правильных ответов - ',ko)