import pickle
# Функція для збереження даних в файлі
def save_users(user):
    with open('users.pickle', 'wb') as file:
        print("Програма записує дані в таблицю...")
        pickle.dump(user, file)
# Функція для завантаження даних із файлу
def load_users():
    try:
        with open('users.pickle', 'rb') as file:
            print("Програма намагається відкрити таблицю...")
            users = pickle.load(file)
    except FileNotFoundError:
        print("Програма створить нову таблицю...")
        users = []
    
    return users
# Завантаження даних із файлу
users = load_users()