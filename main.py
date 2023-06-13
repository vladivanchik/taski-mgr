#Импортирую модули time(для функции sleep), pickle(для базы данных).
import time, pickle
def save_users(user):
    with open('users.pickle', 'wb') as file:
        pickle.dump(user, file)
def load_users():
    try:
        with open('users.pickle', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        users = []
    
    return users

users = load_users()

sel_num = input("Выберите водителя из списка: " + str(users) + "\nЧтобы перейти в режим добавления нового пользователя напишите \"Добавить нового пользователя\"(можно и с маленькой буквы) ")
time.sleep(0.5)

def add_new_user():
    if sel_num.lower() == "добавить нового пользователя":
        print("Сейчас вы перешли в режим добавления нового пользователя...")
        time.sleep(1)
        back = input("Чтобы отменить это действия просто нажмите \"Enter\" \nЕсли вы всё-таки хотите добавить нового пользователя введите \"Добавить\"(можна с маленькой буквы) ")
        
        if back == "":
            print("Сейчас программа завершит свою работу...")
            time.sleep(1)
            exit()
            
        elif back.lower() == "добавить":
            new_value = input("Введите ИФ пользователя которого хотите добавить: ")
            save = input("Сохранить результат? ")
            
            if save.lower() == "да":
                users.append(new_value)
                save_users(users)
                print("Ваш список пользователей сейчас такой" + str(users))
                print("Программа перезапуститься с уже новыми данными...")
                time.sleep(1)
                exit()
                
            elif save.lower == "нет":
                print("Вы выбрали вариант не сохранять данные изменения, программа завершает свою работу без сохранения данных...")
                exit()
                
            else:
                print("Вы ввели неправильные значения, программа завершит свою работу...")
                exit()
                
        return back, new_value, save
add_new_user()
if sel_num in users:
    print("Сейчас вы смотрите информацию по водителю: " + sel_num)
    time.sleep(0.5)

else:
    print("Такого водителя не существует, попробуйте заново")
    exit()
    
dohod = int(input("Чистый доход водителя в кроннах: "))
bonus = int(input("Введите колиство бонусов(будут поделены на 50%): "))
orenda = int(input("Введите затраты на аренду: "))
time.sleep(0.5)

print("Также будут вычтены 700 кронн за гараж")

time.sleep(1)

def present():
    result = dohod - (bonus * 0.5)
    amount = result - (orenda - 700)
    print("Чистый доход работника составляет " + str(amount))
    return result, amount
present()