def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        # Формула БД для мужчин
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        # Формула БД для женщин
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr


def calculate_caloric_needs(bmr, activity_level):
    activity_multiplier = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }

    return bmr * activity_multiplier.get(activity_level, 1.2)


def main():
    print("Добро пожаловать в калькулятор калорий!")

    # Сбор данных от пользователя
    weight = float(input("Введите ваш вес (в кг): "))
    height = float(input("Введите ваш рост (в см): "))
    age = int(input("Введите ваш возраст (в годах): "))
    gender = input("Введите ваш пол (male/female): ").strip()
    activity_level = input(
        "Введите уровень физической активности (sedentary, lightly active, moderately active, very active, extra active): ").strip()

    # Расчет БОД
    bmr = calculate_bmr(weight, height, age, gender)
    print(f"Ваш базальный уровень метаболизма (БОД): {bmr:.2f} калорий в день")

    # Расчет калорий в зависимости от уровня активности
    caloric_needs = calculate_caloric_needs(bmr, activity_level)
    print(f"Ваши суточные потребности в калориях для поддержания веса: {caloric_needs:.2f} калорий в день")

    # Опционально, можно добавить расчет для похудения или набора веса
    weight_loss_goal = caloric_needs - 500  # Для потери примерно 0.5 кг в неделю
    weight_gain_goal = caloric_needs + 500  # Для набора примерно 0.5 кг в неделю
    print(f"Для похудения (0.5 кг в неделю) вам нужно потреблять около: {weight_loss_goal:.2f} калорий в день")
    print(f"Для набора веса (0.5 кг в неделю) вам нужно потреблять около: {weight_gain_goal:.2f} калорий в день")


if __name__ == "__main__":
    main()