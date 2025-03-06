'''
Создайте список чисел.Используйте лямбда-функцию,
чтобы отфильтровать только четные числа из списка и сохранить их в новый список. 
Затем выведите новый список на экран.
'''

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num2 = list(filter(lambda x: x % 2 == 0, num))
# print('четные числа:', num2)


'''
Напишите программу, которая просит пользователя ввести целое число.
Затем программа должна определить, является ли число четным или нечетным,
и вывести соответствующее сообщение. Если число делится на 3 без остатка,
программа должна также вывести сообщение о том, что оно кратно 3. 
Программа должна продолжать запрашивать число до тех пор, пока пользователь не введет "0" для завершения.
'''

# while True:
#     num = int(input('введите число (0 для выхода): '))
#     if num == 0:
#         break
#     if num % 2 == 0:
#         print('число четное')
#     else:
#         print('число нечетное')
#     if num % 3 == 0:
#         print('число также кратно 3.')


'''
Напишите программу, которая принимает на вход текст и выводит 
на экран количество уникальных слов в тексте.
'''

# text = input('введите текст: ')
# words = text.lower().split()
# x_words = set(words)
# print('количество уникальных слов:', len(x_words))



# while True:
#     num = int(input('введите число:'))
#     if num<0:
#         print(f'{num} отрецательное число')
#     elif num>0:
#         print(f'{num} положительное число')
#     elif num==0:
#         print(f'{num} это ноль') 
#     else:
#         print(f'{num} это не число, введите число')
while True:
    import tkinter as tk
    from tkinter import messagebox
    from datetime import datetime, timedelta

    # Глобальные переменные
    attempt_count = 0
    last_attempt_time = None

    def brute_force():
        global attempt_count, last_attempt_time
        password = entry.get()  # Получаем введенный пользователем пароль
        
        # Проверяем, что пароль состоит из 4 цифр
        if len(password) != 4 or not password.isdigit():
            messagebox.showerror("Ошибка", "Пароль должен состоять из 4 цифр!")
            return
        
        # Проверяем, прошло ли 30 секунд с последней попытки
        if last_attempt_time and datetime.now() - last_attempt_time < timedelta(seconds=30):
            remaining_time = int((timedelta(seconds=30) - (datetime.now() - last_attempt_time)).total_seconds())
            messagebox.showwarning("Блокировка", f"Подождите {remaining_time} секунд перед следующей попыткой.")
            return
        
        # Перебор всех возможных комбинаций
        for i in range(10000):  # 0000 - 9999
            attempt = f"{i:04}"  # Форматируем число в 4-значный вид
            if attempt == password:
                messagebox.showinfo("Пароль найден!", f"Пароль: {attempt}")
                attempt_count = 0  # Сбрасываем счетчик попыток
                return  # Останавливаем перебор
        
        # Увеличиваем счетчик попыток
        attempt_count += 1
        last_attempt_time = datetime.now()  # Запоминаем время последней попытки
        
        if attempt_count < 3:
            messagebox.showinfo("Попытка", f"Попытка №{attempt_count}. Пароль не найден.")
        else:
            messagebox.showwarning("Попытка", f"Попытка №{attempt_count}. Пароль не найден. Подождите 30 секунд.")
            button.config(state=tk.DISABLED)  # Блокируем кнопку
            root.after(30000, unlock_button)  # Разблокируем через 30 секунд

    def unlock_button():
        global attempt_count
        attempt_count = 0  # Сбрасываем счетчик попыток
        button.config(state=tk.NORMAL)  # Разблокируем кнопку
        messagebox.showinfo("Разблокировка", "Кнопка разблокирована. Попробуйте снова.")

    # Создание GUI
    root = tk.Tk()
    root.title("Brute Force Password")

    tk.Label(root, text="Введите 4-значный пароль:").pack(pady=5)
    entry = tk.Entry(root, show="*", justify="center", font=("Arial", 14))
    entry.pack(pady=5)

    button = tk.Button(root, text="Подобрать пароль", command=brute_force)
    button.pack(pady=10)

    root.mainloop()