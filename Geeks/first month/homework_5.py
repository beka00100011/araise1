'''
1) Создайте вручную список из 15 элементов (название городов, музыки, машины). 
Сделайте срез от 2-го индекса до 7-го
'''
# list = ['Tokyo', 'Kyota', 'Paris', 'Dubai', 'London', 'Osh', 'Bishkek', 'Porsche', 
# 'Lamborghini', 'Ferrari', 'Maserati', 'BMW', 'Mercedes', 'Rolls Royce', 'Tesla']
# print(list[2:7])

'''
2) Создайте вручную список из чисел и выведите их в обратном порядке
'''
# list2 = [1,2,3,4,5,6,7,8,9,0]
# list2.reverse()
# print(list2)
# print(list2[::-1]) # Второй способ
'''
3) Найдите наименьший элемент в списке из задания 2
'''
# list2 = [1,2,3,4,5,6,7,8,9,0]
# print(min(list2))

'''
4) Удалите все элементы из списка, созданного в задании 2
'''
# list2 = [1,2,3,4,5,6,7,8,9,0]
# list2.clear()
# print(list2)

'''
5) Найдите сумму элементов списка из задания 2
'''
# list2 = [1,2,3,4,5,6,7,8,9,0]
# print(sum(list2))

'''
6) Найдите среднее арифметическое элементов списка из задания 2
'''
# list2 = [1,2,3,4,5,6,7,8,9,0]
# list2_sum = sum(list2)
# list2_len = len(list2)
# print(list2_sum/list2_len)

'''
7) Создайте плейлист из 10 любимых песен, поменяйте 4-й с 8-м и выведите на экран весь плейлист
'''
# play_list = ['We dont talk anymore', 'I Wanna Be Yours', 'Nentori','О ней', 'До ступора',
# 'Нежно', 'Пульс', 'Баллада', 'Джаванна', 'Больше дела меньше слов', ]
# play_list[4], play_list[8] = play_list[8], play_list[4]
# print(play_list)

'''
8) Выясните сколько раз цифра 110 встречается в списке:
'''
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
# 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
# 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 
# 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
# 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,
# 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
# 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 
# 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 
# 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 
# 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 
# 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 
# 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255,
# 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 
# 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295,
# 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125,
# 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
# 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 
# 265,266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 
# 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110].count(110)
# print(numbers)

'''
ДОП ЗАДАНИЕ:

1) Даны два списка, удалите все элементы первого списка из второго, то есть дубликаты.
'''
# a = [1, 3, 4, 5] 
# b = [4, 5, 6, 7]
# b = list(set(b)-set(a))
# print(b) 

'''
2) Создайте 2 строки "Aidana" и "Adilet".
Вам нужно в результате получить смешанную строку из двух имён, буква за буквой.
Результат: "AAiddialneat"
'''
# name1="Aidana"
# name2="Adilet"
# name3 = "".join(sum(zip(name1,name2),()))
# print(name3)
 
'''
3) Вам даётся текст:
Посчитайте количество букв s и t .
Найдите все слова, которые начинаются с корня advert (регистр не должен учитываться)
и превратите их все в верхний регистр
'''

text='''
Advertising companies say advertising is necessary and important.
It informs people about new products. Advertising hoardings in the street make our environment colourful.
And adverts on TV are often funny. Sometimes they are mini-dramas and
we wait for the next programme in the mini-drama. Advertising can educate, too. 
Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier,
be fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad for children.
Adverts make children ‘pester’ their parents buy things for them. 
Advertisers know we love our children and want to give them everything. 
So they use children’s ‘pester power’ to sell their products. Finally, consumers say,
if there is advertising there must be rules. Some adverts advertise unhealthy 
things like cigarettes and make people waste their money.
'''

# count1 = text.count('s')
# count2 = text.count('t')
# print(count1,count2)
# print(text.lower().count('advert'))
# print(text.lower().replace("advert","ADVERT"))
