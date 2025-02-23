# Напишите программу, которая принимает на вход строку (название переменной) и выполняет следующие преобразования в попытке её исправить:
# 1) **(0.2 балла)** символы `-` заменяются на `_`+
# 2) **(0.2 балла)** если переменная написана в формате CamelCase, каждое слово должно быть разделено нижним подчеркиванием и приведено к нижнему регистру (-> `camel_case`).
# В частности, переменные типа `ABC` -> `a_b_c`
# 3) **(0.2 балла)** любые пробелы во вводе переменной заменяются на `_`, после чего избыточное количество символов `_` заменяется на один.
# Пробелы по бокам должны обрезаться и не быть заменены на `_`. Пример: "this is my name" -> "this_is_my_name"+
# 4) **(0.2 балла)** если переменная начинается с цифр, они должны быть удалены; пример: `1myname` -> `myname` (но `myname1` -> `myname1`)+
# 5) **(0.2 балла)** если после всех преобразований имя переменной содержит что-то кроме цифр ([0-9]),
# букв английского алфавита ([A-z]) и нижнего подчеркивания "\_", выводится "Введено некорректное имя переменной". Иначе выводится исправленное имя переменной с учетом всех преобразований
#


a = 'CCCCcamelCase1_-this   _ is my-_ name'
word = 'CCCCamelCase'

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
allowed = upper + lower + nums + '_'

user_input = input('Введите слово: ')
user_input = user_input.lower()
for number in range(1,2):
    number = str(number)
    if user_input[0] == number:
        user_input = user_input[1:]
        print(user_input)

# print(allowed)

print(user_input)
while '-' in user_input or '__' in user_input or ' ' in user_input:
    if '-' in user_input:
        user_input = user_input.replace('-', '_')
    if ' ' in user_input:
        user_input = user_input.replace(' ', '_')
    if '__' in user_input:
        user_input = user_input.replace('__', '_')

print(user_input)


for i in range(len(user_input)):
    # for n in allowed:
    #     if user_input[i] != n:
    #         print('Введено некорректное имя переменной')

    sign = '_' + user_input[i]
    if user_input[i] in upper:
       user_input = user_input.replace((user_input)[i], sign)
       user_input = user_input.lower()
       break
if user_input[0] == '_':
    user_input = user_input.replace('_', '', 1)
    print(user_input)

