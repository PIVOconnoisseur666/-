
import copy

person = ['Энакин Скайуокер',
		  41,
		  ['Татуин', 'Набу', 'Джеонозис', 'Корусант', 'Мустафар', 'Звезда Смерти'],
		  {'световой меч': 'синий', 'ранг': 'лорд ситхов'}
		  ]


def task_1(person):
	print(f'Персона: {person[0].split()[1]}, {person[0].split()[0]}')

def task_2(person):
	print(person[1])

def task_3(person):
	print(', '.join(person[2]))

def task_4(person):
	print(len(person[2]))

def task_5(person):
	print('Звезда Смерти' in person[2])

def task_6(person):
	print(person[3]['световой меч'])

def task_7(person):
	new_person = copy.deepcopy(person)
	new_person[1] = 42
	task_2(new_person)

def task_8(person):
	new_person = copy.deepcopy(person)
	if 'Эндор' not in new_person[2]:
		new_person[2].append('Эндор')
	task_3(new_person)

def task_9(person):
	rang = person[3].get('ранг','джедай')
	if rang == 'лорд ситхов':
		print("Энакин - лорд ситхов")
	else:
		print('Энакин - джедай')

def task_10(person):
	if len(person[2]) > 4:
		print("Энакин побывал во многих местах")
	else:
		print("Энакин не так много путешествовал")
while True:
	user_input = input('Введите команду: ')
	if user_input.lower() == 'выход':
		break
	elif user_input == '1': task_1(person)
	elif user_input == '2': task_2(person)
	elif user_input == '3': task_3(person)
	elif user_input == '4': task_4(person)
	elif user_input == '5': task_5(person)
	elif user_input == '6': task_6(person)
	elif user_input == '7': task_7(person)
	elif user_input == '8': task_8(person)
	elif user_input == '9': task_9(person)
	elif user_input == '10': task_10(person)
	else:
		print('Несуществующая команда')
# 1. Выведите фамилию и имя Энакина в формате "Персона: {Фамилия}, {Имя}".
# 2. Выведите возраст Энакина.
# 3. Напечатайте все места, связанные с крупными событиями вселенной Star Wars, в которых участвовал Энакин, через запятую.
# 4. Найдите количество таких мест и выведите это количество.
# 5. Если среди мест службы Энакина есть 'Звезда Смерти', то он служит Империи. Выведите True или False.
# 6. Напечатайте цвет светового меча Энакина.
# 7. Измените возраст Энакина на 42 и обновите список. Выведите новый возраст.
# 8. Добавьте новое место в список важных мест - 'Эндор'. Выведите обновленный список. Примечание: если "Эндор" уже содержится в списке важных мест, повторно его добавлять не нужно.
# 9. Проверьте, содержит ли список характеристик Энакина ранг 'лорд ситхов'. Если да, выведите "Энакин - лорд ситхов", иначе - "Энакин - джедай".
# 10. Если у Энакина в списке мест более 4 мест, выведите "Энакин побывал во многих местах". Если 4 или меньше - "Энакин не так много путешествовал".
