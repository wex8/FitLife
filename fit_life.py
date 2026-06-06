WATER_PER_KG = 30 / 1000
SLASH = "*" * 40


def calculate_bmi(weight: float, height: float) -> float:
    """Вычисляет Индекс Массы Тела (BMI) по формуле: вес (кг) / рост (м)^2."""
    return round(weight / height**2, 2)


def calculate_water_intake(weight: float) -> float:
    """Вычисляет рекомендуемое количество воды в литрах на основе веса."""
    return round(weight * WATER_PER_KG, 1)


def get_user_name() -> str:
    """Получает имя пользователя, проверяя, что оно не пустое."""
    while True:
        user_name = input("Пожалуйста, введите ваше имя: ").title()
        if user_name:
            return user_name
        print("Имя не может быть пустым. Попробуйте снова.")


def get_user_age() -> int:
    """Получает возраст пользователя, проверяя, что он положительный."""
    while True:
        try:
            user_age = int(input("Введите ваш возраст (в годах): "))
            if user_age <= 0:
                print("Возраст должен быть положительным числом.")
                continue
            return user_age
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def get_user_weight() -> float:
    """Получает вес пользователя, проверяя, что он положительный."""
    while True:
        try:
            user_weight = float(
                input("Пожалуйста, введите ваш вес (в кг): ").replace(",", ".")
            )
            if user_weight <= 0:
                print("Вес должен быть положительным числом.")
                continue
            return user_weight
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


def get_user_height() -> float:
    """Получает рост пользователя, проверяя, что он положительный."""
    while True:
        try:
            user_height = float(
                input("Пожалуйста, введите ваш рост (в м): ").replace(",", ".")
            )
            if user_height <= 0:
                print("Рост должен быть положительным числом.")
                continue
            return user_height
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


if __name__ == "__main__":
    print("Добро пожаловать в FitLife - ваш персональный помощник!")

    user_name = get_user_name()
    user_age = get_user_age()
    user_weight = get_user_weight()
    user_height = get_user_height()

    bmi = calculate_bmi(user_weight, user_height)
    water_needed = calculate_water_intake(user_weight)

    print(
        f"Добрый день, {user_name}!\n\n"
        f"{SLASH}\n"
        f"Отчет для пользователя: {user_name} ({user_age} г.)\n"
        f"Ваш Индекс Массы Тела: {bmi}.\n"
        f"Рекомендуемая для Вас норма воды: {water_needed} л. в день.\n"
        f"{SLASH}\n"
        f"Расчет окончен. Будьте здоровы!",
    )
