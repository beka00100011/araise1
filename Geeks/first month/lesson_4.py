y=int(input('Введите свой возраст: '))
if 7<=y<12:
    print('Добро пожаловать в наш парк!😁')
elif 2<=y<6:
    print('Вам нужен опекун!👀')
elif y>12:
    print('К сожалению вам вход запришен!🤨')
else:
    print('Ошибка❌')
    
n1=float(input('Введите первое число: '))
d=str(input('Выберите действие(+,-,*,/,**,//): '))
n2=float(input('Введите второе число: '))
if d=='+':
    print(f'{n1}+{n2}={n1+n2}')
elif d=='-':
    print(f'{n1}-{n2}={n1-n2}')
elif d=='*':
    print(f'{n1}*{n2}={n1*n2}')
elif d=='/':
    print(f'{n1}/{n2}={n1/n2}')
elif d=='**':
    print(f'{n1}*{n2}={n1*n2}')
elif d=='//':
    print(f'{n1}//{n2}={n1//n2}')
else:
    print('Ошибка❌')

