'1) Вам даётся текст:Посчитайте количество букв s и t .'

# text='''Advertising companies say advertising is necessary and important. 
# It informs people about new products. Advertising hoardings in the street make our environment colourful. 
# And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next 
# programme in the mini-drama. Advertising can educate, too. 
# Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look 
# prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. 
# Adverts make children ‘pester’ their parents buy things for them. 
# Advertisers know we love our children and want to give them everything.
# So they use children’s ‘pester power’ to sell their products. 
# Finally, consumers say, if there is advertising there must be rules. 
# Some adverts advertise unhealthy things like cigarettes and make people waste their money.'''
# s=text.count('s')
# t=text.count('t')
# print(f'В тексте {s} букв s, и {t} букв t')


'''
2) Дана строка: " hello, world! ".
Удалите пробелы в начале и в конце строки.
Преобразуйте все буквы строки в верхний регистр.
Замените запятую на восклицательный знак.
Посчитайте количество символов 'o' в строке.
'''
# stroka=' hello, world! '
# one=stroka='hello, world'
# two=stroka.upper()
# three=stroka='hello! world!'
# four=stroka.count('o')
# print(f'{one}\n{two}\n{three}\n{four}')


'''
3) Преобразование типов данных.
Преобразуйте строку "100" в целое число и выведите его тип.
Преобразуйте число 3.14 в строку и выведите его тип.
Преобразуйте логическое значение True в строку и выведите его тип.
'''
# num1='100'
# num1=int(num1)
# type(num1)
# print(num1,type(num1))
# num2=3.14
# num2=str(num2)
# print(num2,type(num2))
# bool=True
# bool=str(bool)
# print(bool,type(bool))


'''
Доп задание:
Напишите программу которая запрашивает 2 целые числа .
Выведите результат арифметических действий между двумя переменными с помощью f строки.
''' 
# n1=int(input('Введите первое число: '))
# n2=int(input('Введите второе число: '))
# print(f'{n1}+{n2}={n1+n2}')
# print(f'{n1}-{n2}={n1-n2}')
# print(f'{n1}*{n2}={n1*n2}')
# print(f'{n1}/{n2}={n1/n2}')
# print(f'{n1}**{n2}={n1**n2}')
# print(f'{n1}//{n2}={n1//n2}')
