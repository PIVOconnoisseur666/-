flag = 0
brok = ['отмена', 'выход']
while flag == 0:
    print(' | ID  | ProductName | Цена | \n |-----|-------------|------|\n | 001 | Батончик    | 70   |'
          '\n | 002 | Вода        | 45   |\n | 003 | Газировка   | 64   |\n | 004 | Булочка     | 33   |\n')
    flag = 0
    user_input = input('#Выберите товар:')

    user_input.lower

    if user_input == 'ОТМЕНА':
        flag = 1
    else:
        try:
            user_input = int(user_input)
            if 0 < user_input < 5:
                shop = [70, 45, 64, 33]
                user_input -= 1

                cash = [10, 50, 100, 500]
                price = shop[user_input]
                money = 0
                while True:
                    user_input_2 = input(f'#Внесите {shop[user_input]} тугриков:')
                    if user_input_2 == 'ОТМЕНА':
                        flag = 1
                        break
                    try:
                        user_input_2 = int(user_input_2)
                        money += user_input_2
                        if user_input_2 not in cash:
                            print('\n*** Внесена фальшивая купюра ***\n')
                        else:
                            if money >= price:
                                print(f'#Ваша сдача: {money - price}')
                                break
                            else:
                                if flag == 0:
                                    print('\n*** Недостаточно средств ***\n')
                    except ValueError as user_input_2:
                        print('\n*** Введено не числовое значение ***\n')
                flag = 1  # Убрать, если хотим, чтобы просле успешного завершения программы она повторялась
            else:
                print('\n*** Товара с таким ID не существует ***\n')
        except ValueError as user_input:
            print('\n*** Введено не числовое значение ***\n')