WATER_PER_KG = 30 / 1000

# 1. Знакомство
user_name = input("Добрый день! Подскажите, как Вас зовут? ").title()
user_age = int(input("Отлично! Теперь мне нужно узнать Ваш возраст: "))

# 2. Сбор данных
user_weight = float(input("Укажите Ваш вес (в кг): "))
user_height = float(input("Укажите Ваш рост (в метрах, например 1.75): "))

# 3. Логика расчетов
bmi = round(user_weight / user_height**2, 2)
water_needed = round(user_weight * WATER_PER_KG, 1)

# 4. Вывод красивого результата
print(
    f"Добрый день, {user_name}!\n\n"
    f"{'*' * 40}\n"
    f"Отчет для пользователя: {user_name} ({user_age} г.)\n"
    f"Ваш Индекс Массы Тела: {bmi}.\n"
    f"Рекомендуемая для Вас норма воды: {water_needed} л. в день.\n"
    f"{'*' * 40}\n"
    f"Расчет окончен. Будьте здоровы!"
)
