import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QDialogButtonBox, QDialog, QTextBrowser, QTextEdit, QCommandLinkButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import Qt
from main import save_users
from main import users
import keyboard
print("Програма створює модулі...")

app = QApplication(sys.argv)

print("Програма ініціалізується...")

window = QMainWindow()
window.setFixedSize(800, 600)
window.setWindowTitle("Taxi Manager")
app_icon = QIcon ("Icon.png")
window.setWindowIcon(app_icon)
window.resize(800, 600)
window.show()

print("Програма створює параметри вікна...")
class NoEnterTextEdit(QTextEdit):
    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            return  # Просто ігноруємо подію під час натискання Enter
        super().keyPressEvent(event)
print("Програма створює нове правило для об'єкта Text Edit")

def adding_mode():
    
    sign = QTextBrowser(window)
    sign.setText("Ви точно хочете додати нового користувача?")
    sign.show()
    sign.setGeometry(295,200,156,31)
    sign.resize(180,40)
    print("Програма створює напис та його параметри...")
    
    button_box = QDialogButtonBox(window)
    button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.show()
    button_box.setGeometry(310,250,156,31)
    print("Програма створює кнопку дій та її параметри...")
    
    def Ok_canl(button):
        print("Програма створює нову функцію...")
        
        if button == button_box.button(QDialogButtonBox.Ok):
            def push_ent_for_add(e):
                push_add.click()
            keyboard.on_press_key("enter", push_ent_for_add)
            print("Програма створює обробник подій по клавіатурі...")
            
            sign.hide()
            print("Напис ховається...")
            button_box.hide()
            print("Напис ховається...")
            dialog = QDialog()
            dialog.resize(248,229)
            dialog.setWindowTitle("Adding Mode")
            dialog_icon = QIcon("Icon.png")
            dialog.setWindowIcon(dialog_icon)
            dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            print("Програма створює нове вікно і його параметри...")
            
            add_user_text = QTextBrowser(dialog)
            add_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви хочете сюди додати.")
            add_user_text.setGeometry(20,0,211,51)
            add_user_text.show()
            print("Програма створює текстове поле з інформацією та його параметри...")
            
        
            add_user_in_list = NoEnterTextEdit(dialog)
            add_user_in_list.setGeometry(70,70,111,31)
            add_user_in_list.show()
            print("Програма створює поле для введення і його параметри...")
            push_add = QPushButton("Додати у список", dialog)
            push_add.setGeometry(50,130,151,23)
            push_add.show()
            print("Програма створює кнопку підтвердження і його параметри...")
            def if_but_press():
                special_characters = ['№', '"', '!', '%', '@', '#', '$', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '`', '~']
                print("Програма створює список зі спеціальними значеннями...")
                username = add_user_in_list.toPlainText()
                print("Програма створює нову змінну в якій буде передана інформація з add_user_in_list...")
                if username == "":
                    print("Помилка! У QTextEdit, немає ніякої інформації...")
                    dialog.setWindowTitle("Error!")
                    print("Програма змінює назви діалогового вікна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Програма застосовує нову іконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_text.setText("Помилка! Ви не ввели жодних даних, спробуйте знову")
                    print("Програма змінює параметри для об'єкта add_user_text...")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Програма застосовує нове розташування функції add_user_text")
                    
                    ok_to_close = QPushButton("ОK", dialog)
                    print("Програма створює нову кнопку...")
                    ok_to_close.setGeometry(70,130,111,31)
                    print("Програма застосовує розташування кнопки...")
                    ok_to_close.show()
                    push_add.hide()
                    print("Програма ховає об'єкт push_add...")
                    add_user_in_list.hide()
                    print("Програма ховає об'єкт add_user_in_list...")
                    def dia_close():
                        print("Створюється нова функція")
                        
                        dialog.close()                        
                        print("Діалогове вікно закривається...")
                        
                    ok_to_close.clicked.connect(dia_close)
                    print("Функція по закриттю кнопки активується...")
                elif any(char in special_characters for char in username):
                    print("Дані, які ввів користувач, містять неприпустимі значення...")
                    
                    dialog.setWindowTitle("Error!")
                    print("Програма змінює назви діалогового вікна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Програма застосовує нову іконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_in_list.hide()
                    push_add.hide()
                    print("Програма ховає кнопки...")
                    
                    add_user_text.setText("Ви ввели неприпустимі значення! Користувач не може бути доданий, спробуйте знову")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Програма змінює параметри add_user_text...")
                    
                    ok_to_res = QPushButton("OK", dialog)
                    ok_to_res.setGeometry(70,130,111,31)
                    ok_to_res.show()
                    print("Програма створює нову кнопку і застосовує нові параметри до неї...")
                    
                    def res():
                        dialog.setWindowTitle("Adding Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog.setWindowIcon(dialog_icon)
                        print("Програма змінює параметри вікна dialog")
                        
                        add_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви хочете сюди додати.")
                        add_user_text.setGeometry(20,0,211,51)
                        print("Програма застосовує нові значення в add_user_text...")
                        
                        ok_to_res.hide()
                        print("Програма ховає кнопку...")
                        
                        add_user_in_list.show()
                        add_user_in_list.clear()
                        print("Програма відновлює add_user_in_list...")
                        push_add.show()
                        print("Програма показує push_add...")
                    ok_to_res.clicked.connect(res)
                    
                elif username in users:
                    print("Такий користувач уже є в списку!")
                    
                    dialog.setWindowTitle("Error!")
                    print("Программа изменяет названия диалогового окна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    dialog.setWindowIcon(dialog_icon)
                    print("Програма застосовує нову іконку...")
                    
                    add_user_in_list.hide()
                    push_add.close()
                    print("Програма ховає кнопки...")
                    
                    
                    add_user_text.setText("Це ім'я вже є в списку! Спробуйте заново.")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Програма змінює параметри об'єкта add_user_text...")
                    
                    ok_to_res2 = QPushButton("OK", dialog)
                    ok_to_res2.setGeometry(70,130,111,31)
                    ok_to_res2.show()
                    print("Програма створює і застосовує нові значення для кнопки....")
                    def res2():
                        dialog.setWindowTitle("Adding Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog.setWindowIcon(dialog_icon)
                        print("Програма змінює параметри вікна dialog")
                        
                        add_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви хочете сюди додати.")
                        add_user_text.setGeometry(20,0,211,51)
                        print("Програма застосовує нові значення в add_user_text...")
                        
                        ok_to_res2.hide()
                        print("Програма ховає кнопку...")
                        
                        add_user_in_list.show()
                        add_user_in_list.clear()
                        print("Програма відновлює add_user_in_list...")
                        push_add.show()
                        print("Програма показує push_add...")
                        
                    ok_to_res2.clicked.connect(res2)
                    
                else:
                    dialog.setWindowTitle("Warning")
                    print("Програма змінює назви діалогового вікна на \"Warning\"...")
                    dialog_icon = QIcon("Warning.png")
                    dialog.setWindowIcon(dialog_icon)
                    print("Програма застосовує нову іконку...")
                    
                    add_user_in_list.hide()
                    push_add.close()
                    print("Програма ховає кнопки...")
                    
                    
                    add_user_text.setText("Ви точно хочете додати користувача " + username + "?")
                    add_user_text.setGeometry(20,50,211,51)
                    
                    ok_to_res2 = QPushButton("Так", dialog)
                    ok_to_res2.setGeometry(70,130,111,31)
                    ok_to_res2.show()
                    print("Програма створює і застосовує нові значення для кнопки....")
                    
                    def res2():
                        combobox.clear()
                        users.append(username)
                        print("Програма створює і застосовує нові значення для кнопки....")
                        save_users(users)
                        print("Програма зберігає список...")
                        add_user_in_list.clear()
                        print("Програма очищає вміст об'єкта QTextEdit...")
                        for user in users:
                            combobox.addItem(user)
                            print("Програма оновлює інформацію про списки...")
                        
                        dialog.setWindowTitle("Adding Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog.setWindowIcon(dialog_icon)
                        print("Програма змінює параметри вікна dialog")
                        
                        add_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви хочете сюди додати.")
                        add_user_text.setGeometry(20,0,211,51)
                        print("Програма застосовує нові значення в add_user_text...")
                        
                        ok_to_res2.hide()
                        print("Програма ховає кнопку...")
                        
                        add_user_in_list.show()
                        add_user_in_list.clear()
                        print("Програма відновлює add_user_in_list...")
                        push_add.show()
                        print("Програма показує push_add...")
                        
                    ok_to_res2.clicked.connect(res2)
            push_add.clicked.connect(if_but_press)
            dialog.exec_()
            
        elif button == button_box.button(QDialogButtonBox.Cancel):
            sign.close()
            print("Напис закривається...")
            button_box.close()
            print("Кнопка закривається...")
    button_box.clicked.connect(Ok_canl)
def del_user():  
    del_sign = QTextBrowser(window)
    del_sign.setText("Ви точно хочете видалити користувача зі списку?")
    del_sign.setGeometry(295,200,156,31)
    del_sign.resize(180,40)
    del_sign.show()
    print("Створюється новий напис, також параметри до нього...")
    
    del_but = QDialogButtonBox(window)
    del_but.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    del_but.show()
    del_but.setGeometry(310,250,156,31)
    del_but.show()
    print("Програма створює інтерактивні кнопки, а також їхні параметри...")
    def ok_but(button):
        if button == del_but.button(QDialogButtonBox.Ok):
            def push_ent_for_del(e):
                del_button.click()
            keyboard.on_press_key("enter", push_ent_for_del)
            del_sign.hide()
            print("Програма ховає напис...")
            del_but.hide()
            print("Програма ховає напис...")
            
            dialog2 = QDialog()
            dialog2.resize(248,229)
            dialog2.setWindowTitle("Delete Mode")
            dialog_icon = QIcon("Icon.png")
            dialog2.setWindowIcon(dialog_icon)
            dialog2.setWindowFlags(dialog2.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            dialog2.show()
            print("Програма створює нове вікно і його параметри...")
            
            del_user_text = QTextBrowser(dialog2)
            del_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви видалити зі списку.")
            del_user_text.setGeometry(20,0,211,51)
            del_user_text.show()
            print("Програма створює текстове поле з інформацією та його параметри...")
            
            del_user_list = NoEnterTextEdit(dialog2)
            del_user_list.setGeometry(70,70,111,31)
            del_user_list.show()
            print("Програма створює поле для введення і його параметри...")
            del_button = QPushButton("Удалить из списка", dialog2)
            del_button.setGeometry(50,130,151,23)
            del_button.show()
            print("Програма створює кнопку підтвердження і його параметри...")
            
            def if_but_press_to_del():
                del_username = del_user_list.toPlainText()
                if del_username in users:
                    dialog2.setWindowTitle("Warning")
                    print("Програма змінює назву діалогового вікна на \"Warning\"...")
                    dialog_icon = QIcon("Warning.png")
                    dialog2.setWindowIcon(dialog_icon)
                    print("Програма змінює параметри вікна...")
                
                    del_user_text.setText("Ви точно хочете видалити користувача " + del_username + "? Цю дію неможливо скасувати!")
                    del_user_text.setGeometry(20,50,211,51)
                    print("Програма застосовує нові параметри для del_user_text")
                    
                    del_button.hide()
                    del_user_list.hide()
                    print("Програма ховає кнопки...")
                    
                    ok_to_res = QPushButton("ОК", dialog2)
                    ok_to_res.setGeometry(70,130,111,31)
                    ok_to_res.show()
                    print("Програма створює і застосовує нові значення для кнопки...")
                    
                    def if_but_press():
                        users.remove(del_username)
                        print("Програма видаляє вміст списку...")
                        save_users(users)
                        print("Програма зберігає список...")
                        del_user_list.clear()
                        print("Програма очищає вміст об'єкта QTextEdit...")
                        # Отримуємо індекс елемента в combobox за його значенням (ім'я користувача)
                        index = combobox.findText(del_username)
                        if index != -1:
                            combobox.removeItem(index)
                        print("Програма оновлює інформацію про списки...")
                        
                        dialog2.setWindowTitle("Delete Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog2.setWindowIcon(dialog_icon)
                        print("Програма повертає параметри вікна...")
                        
                        ok_to_res.hide()
                        del_button.show()
                        del_user_list.show()
                        del_user_list.clear()
                        print("Програма змінює параметри кнопок...")
                        
                        del_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви видалити зі списку.")
                        del_user_text.setGeometry(20,0,211,51)
                    ok_to_res.clicked.connect(if_but_press)
                    
                
                elif del_username != "" and del_username not in users:
                    print("Цього користувача не існує")
                    dialog2.setWindowTitle("Error")
                    print("Програма застосовує нову назву для об'єкта dialog2")
                    dialog_icon2 = QIcon("Error.png")
                    print("Програма застосовує нову іконку для об'єкта dialog2")
                    dialog2.setWindowIcon(dialog_icon2)
                    
                    del_user_text.setText("Помилка! Даного користувача немає в списку, спробуйте заново.")
                    del_user_text.setGeometry(20,50,211,51)
                    print("Програма застосовує нові параметри в del_user_text")
                    
                    del_button.hide()
                    del_user_list.hide()
                    print("Програма ховає кнопки...")
                    
                    ok_to_res = QPushButton("ОК", dialog2)
                    ok_to_res.setGeometry(70,130,111,31)
                    ok_to_res.show()
                    print("Програма створює і застосовує нові значення для кнопки...")
                    
                    def if_but_press():
                        dialog2.setWindowTitle("Delete Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog2.setWindowIcon(dialog_icon)
                        print("Програма повертає параметри вікна...")
                        
                        ok_to_res.hide()
                        del_button.show()
                        del_user_list.show()
                        del_user_list.clear()
                        print("Програма змінює параметри кнопок...")
                        
                        del_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви видалити зі списку.")
                        del_user_text.setGeometry(20,0,211,51)
                    ok_to_res.clicked.connect(if_but_press)
                    
                else:
                    print("Ви не ввели будь-які значення")
                    dialog2.setWindowTitle("Error")
                    print("Програма застосовує нову назву для об'єкта dialog2")
                    dialog_icon2 = QIcon("Error.png")
                    print("Програма застосовує нову іконку для об'єкта dialog2")
                    dialog2.setWindowIcon(dialog_icon2)
                    
                    del_button.hide()
                    del_user_list.hide()
                    print("Програма ховає кнопки...")
                    
                    del_user_text.setText("Помилка! Ви не ввели жодних значень, спробуйте знову!")
                    del_user_text.setGeometry(20,50,211,51)
                    
                    ok_to_close = QPushButton("OK", dialog2)
                    print("Програма створює нову кнопку...")
                    ok_to_close.setGeometry(70,130,111,31)
                    ok_to_close.show()
                    print("Програма застосовує нові параметри для кнопки ok_to_close")
                    
                    def close():
                        print("Програма створює нову функцію...")
                        
                        dialog2.close()
                        print("Програма закриває діалогове вікно...")
                    ok_to_close.clicked.connect(close)
                    print("Ви ввели неправильне значення, видалення не відбудеться...")
            del_button.clicked.connect(if_but_press_to_del)
            dialog2.exec_()
        elif button == del_but.button(QDialogButtonBox.Cancel):
            del_sign.close()
            print("Програма закриває напис...")
            del_but.close()
            print("Програма закриває кнопки...")
        
    del_but.clicked.connect(ok_but)

def func_calculate_of_profit():
    def push_ent_for_add(e):
        ent_button.click()
    keyboard.on_press_key("enter", push_ent_for_add)
    print("Програма створює функцію по взаємодії з клавіатурою")
    dialog3 = QDialog()
    dialog3.resize(248,229)
    dialog3.setWindowTitle("Calculating Mode")
    dialog_icon = QIcon("Icon.png")
    dialog3.setWindowIcon(dialog_icon)
    dialog3.setWindowFlags(dialog3.windowFlags() & ~Qt.WindowContextHelpButtonHint)
    print("Програма створює нове вікно і його параметри...")
    
    calculate_of_profit_text = QTextBrowser(dialog3)
    calculate_of_profit_text.setText("Введіть нижче ім'я та прізвище людини, для якої ви хочете разрахувати прибуток.")
    calculate_of_profit_text.setGeometry(20,0,211,51)
    calculate_of_profit_text.show()
    print("Програма створює текстове поле з інформацією та його параметри...")
    
    calculate_of_profit_list = NoEnterTextEdit(dialog3)
    calculate_of_profit_list.setGeometry(70,70,111,31)
    calculate_of_profit_list.show()
    print("Програма створює поле для введення і його параметри...")
    
    ent_button = QPushButton("Розрахувати прибуток для водія", dialog3)
    ent_button.setGeometry(30,130,190,23)
    ent_button.show()
    print("Програма створює нову кнопку та властивосіт для неї...")
    
    def func_net_income():
        username = calculate_of_profit_list.toPlainText()
        if username in users:
            calculate_of_profit_text.setText("Нижче введіть чистий дохід водія " + username)
            calculate_of_profit_list.clear()
            ent_button.close()
            print("Програма змінила налаштування для деяких кнопок...")
            
            button = QPushButton("Ввести значення" ,dialog3)
            button.setGeometry(40,130,170,23)
            button.show()
            print("Програма створює нову кнопку, а також параметри для неї...")
            def func_spent_fuel():
                net_income = calculate_of_profit_list.toPlainText()
                if net_income.isdigit():
                    calculate_of_profit_text.setText("Нижче введіть скільки водій витратив на пальне...")
                    calculate_of_profit_list.clear()
                    button.close()
                    print("Програма змінює параметри для кнопок...")
                    
                    button2 = QPushButton("Ввести значення", dialog3)
                    button2.setGeometry(40,130,170,23)
                    button2.show()
                    print("Програма створює нову кнопку та параметри для неї...")
                    
                else:
                    dialog3.setWindowTitle("Error")
                    dialog_icon = QIcon("Error.png")
                    dialog3.setWindowIcon(dialog_icon)
                    print("Програма змінює параметри вікна...")
            
                    calculate_of_profit_text.setText("Помилка! налючюються неприпустіми значення, спробуйте заново(вводіть значення тільки з цифрами)")
                    calculate_of_profit_text.setGeometry(20,40,211,51)
                    calculate_of_profit_list.hide()
                    print("Програма змінює значення в кнопках...")
                    
                    ok_to_close = QPushButton("Ок", dialog3)
                    ok_to_close.setGeometry(40,130,170,23)
                    ok_to_close.show()
                    print("Програма створює нову кнопку, та параметри для неї...")
                    
                    def if_but_press():
                        dialog3.close()
                        print("Програма закриває вікно та всі об'єкти...")
                    ok_to_close.clicked.connect(if_but_press)
            button.clicked.connect(func_spent_fuel)
            
        else:
            dialog3.setWindowTitle("Error")
            dialog_icon = QIcon("Error.png")
            dialog3.setWindowIcon(dialog_icon)
            print("Програма змінює параметри вікна...")
            
            calculate_of_profit_text.setText("Даного користувача немає у списку, спробуйте знову")
            calculate_of_profit_text.setGeometry(20,40,211,51)
            ent_button.close()
            calculate_of_profit_list.hide()
            print("Програма змінює параметри кнопок...")
            
            ok_to_close = QPushButton("Ок", dialog3)
            ok_to_close.setGeometry(40,130,170,23)
            ok_to_close.show()
            print("Програма створює нову кнопку, та задає параметри для неї...")
            
            def if_but_press():
                dialog3.setWindowTitle("Calculating Mode")
                dialog_icon = QIcon("Icon.png")
                dialog3.setWindowIcon(dialog_icon)
                print("Програма змінює параметри вікна...")
                
                calculate_of_profit_text.setText("Введіть нижче ім'я та прізвище людини, для якої ви хочете разрахувати прибуток.")
                calculate_of_profit_text.setGeometry(20,0,211,51)
                print("Програма змінює параметри для об'єкта calculate_of_profit_text...")
                
                calculate_of_profit_list.clear()
                calculate_of_profit_list.show()
                print("Програма змінює параметри для вікна calculate_of_profit_list...")
                
                ent_button.show()
                ok_to_close.close()
                print("Програма змінює параметри для об'єктів")
                
            ok_to_close.clicked.connect(if_but_press)
    
    ent_button.clicked.connect(func_net_income)
    dialog3.exec_()
    
combobox = QComboBox(window)  # Створюємо порожній QComboBox з батьком window
print("combobox створюється...")
combobox.setGeometry(10, 1, 351, 51)
print("Встановлюються параметри для combobox...")

for user in users:
    combobox.addItem(user)  # Додаємо елементи зі списку users у combobox
    print("Програма додає елементи зі списку...")

add_user = QPushButton("Додати нового користувача", window) # Створюємо кнопку, яка дає змогу додати нового користувача
add_user.setGeometry(370, 0, 191, 51)
add_user.clicked.connect(adding_mode)
print("Програма створює кнопку і задає нові параметри...")
    
delete_user = QPushButton("Видалити користувача", window)
delete_user.setGeometry(570, 0, 191, 51)
delete_user.clicked.connect(del_user)
print("Програма створює кнопку і задає нові параметри...")

calculate_of_profit = QCommandLinkButton("Розрахувати прибуток водія", window)
calculate_of_profit.setGeometry(5,55,340,41)
calculate_of_profit.show()
calculate_of_profit.clicked.connect(func_calculate_of_profit)
print("Програма створює кнопку і задає нові параметри...")

    
combobox.show()
add_user.show()
delete_user.show()
window.show()
sys.exit(app.exec_())
