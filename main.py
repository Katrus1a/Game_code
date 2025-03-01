import random


# Функція для генерації унікального коду з 4 цифр (без повторень)
def generate_code():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))


# Функція для перевірки коду та підрахунку збігів
def check_code(secret_code, guess):
    # Підрахунок збігів цифр
    digits_in_code = sum(1 for digit in set(guess) if digit in secret_code)

    # Підрахунок цифр на своїх місцях
    correct_positions = sum(1 for i in range(4) if guess[i] == secret_code[i])

    return digits_in_code, correct_positions


# Функція для ходу бота (рандомно генерує код з можливими повторами цифр)
def bot_guess():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))


# Основна функція гри
def play_game():
    print("Починаємо гру!")

    # Гравець загадує свій код
    while True:
        player_secret_code = input("Загадайте свій секретний код (4 унікальні цифри): ")
        if len(player_secret_code) == 4 and player_secret_code.isdigit() and len(set(player_secret_code)) == 4:
            break
        else:
            print("Помилка: введіть 4 унікальні цифри!")

    # Бот генерує свій код (не показуємо його гравцеві)
    bot_secret_code = generate_code()

    # Ігровий цикл
    while True:
        # Хід гравця
        player_guess = input("Ваш хід! Введіть свій варіант коду (цифри можуть повторюватися): ")
        if len(player_guess) != 4 or not player_guess.isdigit():
            print("Помилка: введіть 4-значний код, що складається лише з цифр.")
            continue

        # Перевірка ходу гравця
        digits_in_code, correct_positions = check_code(bot_secret_code, player_guess)
        print(f"Цифр у коді: {digits_in_code}, на своєму місці: {correct_positions}")
        if correct_positions == 4:
            print("🎉 Ви виграли! Ви вгадали код бота.")
            break

        # Хід бота
        bot_guess_code = bot_guess()
        digits_in_code, correct_positions = check_code(player_secret_code, bot_guess_code)
        print(f"Хід бота: {bot_guess_code} -> Цифр у коді: {digits_in_code}, на своєму місці: {correct_positions}")
        if correct_positions == 4:
            print("🤖 Бот виграв! Бот вгадав ваш код.")
            break


# Запуск гри
play_game()
