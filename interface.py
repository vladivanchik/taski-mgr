import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QDialogButtonBox, QDialog, QTextBrowser, QTextEdit, QCommandLinkButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main import save_users
from main import users
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

def adding_mode():   
    print("Програма створює нову функцію...")
    
    dialog = QDialog()
    dialog.resize(248,229)
    dialog.setWindowTitle("Adding Mode")
    dialog_icon = QIcon("Icon.png")
    dialog.setWindowIcon(dialog_icon)
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint) # Ховає кнопку підказок у вікні dialog
    print("Програма створює нове вікно і його параметри...")
        
    add_user_text = QTextBrowser(dialog)
    add_user_text.setText("Введіть сюди ім'я/прізвище людини, яку ви хочете сюди додати.")
    add_user_text.setGeometry(20,0,211,51)
    add_user_text.show()
    print("Програма створює текстове поле з інформацією та його параметри...")
    
    add_user_in_list = QTextEdit(dialog)
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
        username = add_user_in_list.toPlainText() # змінна в якій буде передана інформація з add_user_in_list...
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
            print("Програма змінює назву діалогового вікна на \"Error\"...")
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
def del_user():  
    dialog = QDialog()
    dialog.resize(248,229)
    dialog.setWindowTitle("Delete Mode")
    dialog_icon = QIcon("Icon.png")
    dialog.setWindowIcon(dialog_icon)
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint) # Ховає кнопку підказок у вікні dialog
    print("Програма створює нове вікно і його параметри...")
    
    sign = QTextBrowser(dialog)
    sign.setText("Виберіть якого користувача ви хочете видалити.")
    sign.setGeometry(20,0,211,51)
    sign.show()
    print("Програма створює новий напис sing, та задає параметри для нього...")
    
    combobox_to_del = QComboBox(dialog)
    combobox_to_del.setGeometry(35,70,180,40)
    combobox_to_del.show()
    for user in users:
        combobox_to_del.addItem(user)
        print("Програма додає елементи зі списку...")
    print("Програма створює новий об'єкт та створює параметри для нього...")
    
    but_to_del = QPushButton("Видалити користувача", dialog)
    but_to_del.setGeometry(50,130,151,23)
    but_to_del.show()
    print("Програма створює нову кнопку, та задає параметри для неї...")
    
    def but_press():
        selected_index = combobox_to_del.currentIndex() # Змінна яка зберігає значення індексу combobox
        if selected_index != -1: # Перевіряємо що combobox не дорівнює -1(нічого немає у списку)
            combobox_to_del.hide()
            but_to_del.hide()
            print("Програма ховає об'єкти")
            text_from_combobox= combobox_to_del.currentText() # Отримуємо текст з combobox_to_del
            
            dialog.setWindowTitle("Warning!")
            dialog_icon = QIcon("Warning.png")
            dialog.setWindowIcon(dialog_icon)
            print("Програма змінює параметри вікна...")
            
            sign.setText("Ви точно хочете видалити користувача? " + text_from_combobox + ". Цю дію неможливо скасувати! ")
            sign.setGeometry(20,40,211,51)
            print("Програма змінює параметри об'єкта...")
            
            button_box = QDialogButtonBox(dialog)
            button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            button_box.setGeometry(50,130,151,23)
            button_box.show()
            print("Програма створює нову кнопку, та задає параметри для неї...")
            
            def ok_canl_press(button):
                if button == button_box.button(QDialogButtonBox.Ok):
                    users.remove(text_from_combobox)
                    save_users(users)
                    print("Програма видаляє, та збережує нові дані...")
                    
                    index = combobox.findText(text_from_combobox)
                    if index != 1:
                        combobox.removeItem(index)
                    print("Програма оновлює інформацію в combobox")
                    combobox_to_del.clear()
                    for user in users:
                        combobox_to_del.addItem(user)
                    print("Програма оновлює інформацію про combobox_to_del...")
        
                    button_box.hide()
                    print("Програма ховає кнопку...")
                    combobox_to_del.show()
                    but_to_del.show()
                    print("Програма показує об'єкти...")
                    
                    sign.setText("Виберіть якого користувача ви хочете видалити.")
                    sign.setGeometry(20,0,211,51)
                    print("Програма змінює параметри вікна...")
                    
                    dialog.setWindowTitle("Delete Mode")
                    dialog_icon = QIcon("Icon.png")
                    dialog.setWindowIcon(dialog_icon)
                    print("Програма змінює параметри вікна...")
                    
                elif button == button_box.button(QDialogButtonBox.Cancel):
                    dialog.close()
                    print("Програма закриває вікно...")
            button_box.clicked.connect(ok_canl_press)
                
                        
        else:
            combobox_to_del.hide()
            dialog.setWindowTitle("Error!")
            dialog_icon = QIcon("Error.png")
            dialog.setWindowIcon(dialog_icon)
            print("Програма змінює параметри вікна")
            
            sign.setText("Помилка! Ніяких користувачів не знайдено, спробуйте спочатку додати їх.")
            sign.setGeometry(20,40,211,51)
            print("Програма змінює параметри об'єкта...")
            
            but_to_del.setText("Ок")
            print("Програма змінює параметри кнопки...")
            
            def but_press():
                dialog.close()
                print("Програма закриває dialog")
            but_to_del.clicked.connect(but_press)
            
            
    but_to_del.clicked.connect(but_press)
    dialog.exec_()
def func_of_adding_car():
    dialog = QDialog()
    dialog.resize(248,229)
    dialog.setWindowTitle("Adding Mode")
    dialog_icon = QIcon("Icon.png")
    dialog.setWindowIcon(dialog_icon)
    dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
    print("Програма створює нове вікно та задає параметри для нього...")
    
    message_text = QTextBrowser(dialog)
    message_text.setText("Нижче виберіть людину з поданого списку, для якої ви хочете додати автівку...")
    message_text.setGeometry(20,0,211,51)
    print("Програма створює нову функцію, та задає параметри для неї...")
    
    
    combo_user = QComboBox(dialog)
    for user in users:
        combo_user.addItem(user) # Програма буде додавати кожного користувача зі списка, по черзі
    combo_user.setGeometry(35,70,180,40)
    combo_user.show()
    print("Програма створює новий combobox, та задає параметри для нього...")
    
    push_button = QPushButton("Вибрати", dialog)
    push_button.setGeometry(50,130,151,23)
    push_button.show()
    print("Програма створює нову кнопку, та параметри для неї...")
    
    def if_but_press():
        index = combo_user.currentIndex() # Вибудовуємо індекс з combo_user
        current_text = combo_user.currentText() # Вибудовуємо даний текст з combo_user
        if index != -1:
            combo_user.hide()
            push_button.hide()
            print("Програма ховає непотрібні об'єкти...")
            
            dialog.setWindowTitle("Warning!")
            app_icon = QIcon("Warning.png")
            dialog.setWindowIcon(app_icon)
            print("Програма змінює параметри вікна...")
            
            message_text.setText("Ви впевнені що хочете додати автівку? Вона застосується до користувача " + current_text)
            message_text.setGeometry(35,55,180,53)
            print("Програма змінює параметри об'єкта...")
            
            button_box = QDialogButtonBox(dialog)
            button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            button_box.setGeometry(50,130,151,23)
            button_box.show()
            print("Програма створює новий об'єкт та задає параметри для нього...")
            def but_press(button):
                if button == button_box.button(QDialogButtonBox.Ok):
                    pass    
                elif button == button_box.button(QDialogButtonBox.Cancel):
                    pass
            button_box.clicked.connect(but_press)
        else:
            combo_user.hide()
            
            dialog.setWindowTitle("Error!")
            app_icon = QIcon("Error.png")
            dialog.setWindowIcon(app_icon)
            
            message_text.setText("Помилка! Ви не вибрали жодного користувача зі списку, спробуйте заново.")
            message_text.setGeometry(35,55,180,53)
            print("Програма змінює параметри для об'єкту...")
            
            push_button.setText("Ок")
            
            def close():
                dialog.close()
                print("Програма закриває вікно...")
            push_button.clicked.connect(close)
            
    push_button.clicked.connect(if_but_press)
    
    dialog.exec_()
    
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

adding_car = QCommandLinkButton("Додати нову автівку", window)
adding_car.setGeometry(5,55,340,41)
adding_car.show()
adding_car.clicked.connect(func_of_adding_car)
print("Програма створює кнопку і задає нові параметри...")

    
combobox.show()
add_user.show()
delete_user.show()
window.show()
sys.exit(app.exec_())