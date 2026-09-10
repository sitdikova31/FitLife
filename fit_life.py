
# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30  # 30 - стандартная рекомендация
# для поддержания водного баланса
MILLILITER_IN_LITER = 1000  # (1 л = 1000 мл)


# функции
def calculate_bmi(user_weight, user_height):
    """Рассчитываем идекс массы тела"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)  # Округляем результат до одного знака после запятой


# Подсчет воды: вес * 30 мл
def calculate_water_needed(user_weight):
    """Рассчитываем норму воды"""
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / MILLILITER_IN_LITER  # Переводим в литры
    return water_l


# 1. Знакомство
# TODO: Спроси у пользователя имя/
#  и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную
# user_age (не забудь преобразовать в число)

print('Здравствуйте!')  # Приветствие
user_name = input('Как Вас зовут?')  # Узнаем имя
user_age = int(input('Сколько Вам лет?'))  # Узнаем возраст
print('Приятно познакомиться,', user_name)  # Выводим имя


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75)
# и сохрани в user_height (тип float)
user_weight = float(input('Какой Ваш вес? (В кг)'))  # Узнаем вес
user_height = float(input('Какой Ваш рост? (В метрах)'))  # Узнаем рост
print('Ваш вес (В кг)', user_weight)  # Выводим вес
print('Ваш рост (В метрах)', user_height)  # Выводим рост


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = calculate_bmi(user_weight, user_height)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_l = calculate_water_needed(user_weight)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие,
# например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
# Вывод
print(f'Отчет для пользователя: {user_name} ({user_age} лет)\n'
      f'Твой индекс массы тела: {bmi}\n'
      f'Рекомендуемая норма воды: {water_l} л. в день')

print('Расчет окончен. Будьте здоровы!')
