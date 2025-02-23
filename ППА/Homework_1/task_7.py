# ## Задача 7. Развернуть число (0.5 балла)
#
# Вам на вход подается произвольное целое число. "Разверните" его, не используя преобразование к строке (это единственное ограничение)
#
# **Пример 1:**
#
# ```
# Ввод: 12345890
# Вывод: 9854321
# ```
#
# **Пример 2:**
# ```
# Ввод: 10000
# Вывод: 0
# ```

def reverse_number(num):
    # Обрабатываем случай, когда число равно нулю
    if num == 0:
        return 0

    reversed_num = 0
    has_significant_digit = False  # Флаг, чтобы проверить наличие значащих цифр

    # Переворачиваем число
    while num > 0:
        digit = num % 10
        if digit != 0:
            has_significant_digit = True  # Найдена значащая цифра
        reversed_num = reversed_num * 10 + digit
        num //= 10

    # Если не было найдено значащих цифр, возвращаем 0
    return reversed_num if has_significant_digit else 0

num = int(input("Введите целое число: "))
print("Развернутое число:", reverse_number(num))