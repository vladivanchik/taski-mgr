import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QDialogButtonBox, QDialog, QTextBrowser, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from main import save_users
from main import users
import keyboard
print("Программа создаёт модули...")

app = QApplication(sys.argv)

print("Программа инициализируется...")

window = QMainWindow()
window.setFixedSize(800, 600)
window.setWindowTitle("Taxi Manager")
app_icon = QIcon ("Icon.png")
window.setWindowIcon(app_icon)
window.resize(800, 600)
window.show()

print("Программа создаёт параметры окна...")
class NoEnterTextEdit(QTextEdit):
    def keyPressEvent(self, event):
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            return  # Просто игнорируем событие при нажатии Enter
        super().keyPressEvent(event)
print("Программа создаёт новую")

def adding_mode():
    
    sign = QTextBrowser(window)
    sign.setText("Вы точно хотите добавить нового пользователя?")
    sign.show()
    sign.setGeometry(295,200,156,31)
    sign.resize(180,40)
    print("Программа создаёт надпись и её параметры ...")
    
    button_box = QDialogButtonBox(window)
    button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.show()
    button_box.setGeometry(310,250,156,31)
    print("Программа создаёт кнопку действий и её параметры...")
    
    def Ok_canl(button):
        print("Программа создаёт новую функцию...")
        
        if button == button_box.button(QDialogButtonBox.Ok):
            def push_ent_for_add(e):
                push_add.click()
            keyboard.on_press_key("enter", push_ent_for_add)
            print("Программа создаёт обработчика событий по клавиатуре...")
            
            sign.hide()
            print("Надпись прячется...")
            button_box.hide()
            print("Надпись прячется...")
            dialog = QDialog()
            dialog.resize(248,229)
            dialog.setWindowTitle("Adding Mode")
            dialog_icon = QIcon("Icon.png")
            dialog.setWindowIcon(dialog_icon)
            dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            print("Программа создаёт новоё окно и его параметры...")
            
            add_user_text = QTextBrowser(dialog)
            add_user_text.setText("Введите сюда имя/фамилию человека которого вы хотите сюда добавить.")
            add_user_text.setGeometry(20,0,211,51)
            add_user_text.show()
            print("Программа создаёт текстовое поле с информацией и его параметры...")
            
        
            add_user_in_list = NoEnterTextEdit(dialog)
            add_user_in_list.setGeometry(70,70,111,31)
            add_user_in_list.show()
            print("Программа создаёт поле для ввода и его параметры...")
            push_add = QPushButton("Добавить в список", dialog)
            push_add.setGeometry(50,130,151,23)
            push_add.show()
            print("Программа создаёт кнопку подтверждения и его параметры...")
            def if_but_press():
                special_characters = ['№', '"', '!', '%', '@', '#', '$', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '`', '~']
                print("Программа создаёт список со специальными значениями...")
                username = add_user_in_list.toPlainText()
                print("Программа создаёт новую переменную в которой будет передана информация из add_user_in_list...")
                if username == "":
                    print("Ошибка! В QTextEdit, нету никакой информации...")
                    dialog.setWindowTitle("Error!")
                    print("Программа изменяет названия диалогового окна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Программа применяет новую иконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_text.setText("Ошибка! Вы не ввели никаких данных, попробуйте снова")
                    print("Программа изменяет параметры для объекта add_user_text...")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Программа применяет новое расположение функции add_user_text")
                    
                    ok_to_close = QPushButton("ОK", dialog)
                    print("Программа создаёт новую кнопку...")
                    ok_to_close.setGeometry(70,130,111,31)
                    print("Программа применяет расположение кнопки...")
                    ok_to_close.show()
                    push_add.hide()
                    print("Программа прячет объект push_add...")
                    add_user_in_list.hide()
                    print("Программа прячет объект add_user_in_list...")
                    def dia_close():
                        print("Создаётся новая функция...")
                        
                        dialog.close()                        
                        print("Диалоговое окно закрывается...")
                        
                    ok_to_close.clicked.connect(dia_close)
                    print("Функция по закрытию кнопки активируется...")
                elif any(char in special_characters for char in username):
                    print("Данные которые ввёл пользователь содержат недопустимые значения...")
                    
                    dialog.setWindowTitle("Error!")
                    print("Программа изменяет названия диалогового окна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Программа применяет новую иконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_in_list.hide()
                    push_add.hide()
                    print("Программа прячет кнопки...")
                    
                    add_user_text.setText("Вы ввели недопустимые значения! Пользователь не может быть добавлен, попробуйте снова")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Программа изменяет параметры add_user_text...")
                    
                    ok_to_res = QPushButton("OK", dialog)
                    ok_to_res.setGeometry(70,130,111,31)
                    ok_to_res.show()
                    print("Программа создаёт новую кнопку и применяет новые параметры к ней...")
                    
                    def res():
                        dialog.setWindowTitle("Adding Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog.setWindowIcon(dialog_icon)
                        print("Программа изменяет параметры окна dialog")
                        
                        add_user_text.setText("Введите сюда имя/фамилию человека которого вы хотите сюда добавить.")
                        add_user_text.setGeometry(20,0,211,51)
                        print("Программа применяет новые значения в add_user_text...")
                        
                        ok_to_res.hide()
                        print("Программа прячет кнопку...")
                        
                        add_user_in_list.show()
                        add_user_in_list.clear()
                        print("Программа восстанавливает add_user_in_list...")
                        push_add.show()
                        print("Программа показывает push_add...")
                    ok_to_res.clicked.connect(res)
                    
                elif username in users:
                    print("Такой пользователь уже есть в списке!")
                    def for_res2(e):
                        ok_to_res2.click()
                    keyboard.on_press_key("enter", for_res2)
                    print("Программа создаёт поддержку клавиатуры для данной функции...")
                    
                    add_user_in_list.hide()
                    push_add.close()
                    print("Программа прячет кнопки...")
                    
                    dialog.setWindowTitle("Error!")
                    print("Программа изменяет названия диалогового окна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Программа применяет новую иконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_text.setText("Данное имя уже есть в списке! Попробуйте заново.")
                    add_user_text.setGeometry(20,50,211,51)
                    print("Программа изменяет параметры объекта add_user_text...")
                    
                    ok_to_res2 = QPushButton("OK", dialog)
                    ok_to_res2.setGeometry(70,130,111,31)
                    ok_to_res2.show()
                    print("Программа создаёт и применяет новые значения для кнопки....")
                    def res2():
                        dialog.setWindowTitle("Adding Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog.setWindowIcon(dialog_icon)
                        print("Программа изменяет параметры окна dialog")
                        
                        add_user_text.setText("Введите сюда имя/фамилию человека которого вы хотите сюда добавить.")
                        add_user_text.setGeometry(20,0,211,51)
                        print("Программа применяет новые значения в add_user_text...")
                        
                        ok_to_res2.close()
                        print("Программа закрывает кнопку...")
                        
                        add_user_in_list.show()
                        add_user_in_list.clear()
                        print("Программа восстанавливает add_user_in_list...")
                        push_add.show()
                        print("Программа показывает push_add...")
                        
                        
                    ok_to_res2.clicked.connect(res2)
                    
                else:
                    combobox.clear()
                    users.append(username)
                    print("Программа добавляет в список новую информацию...")
                    save_users(users)
                    print("Программа сохраняет список...")
                    add_user_in_list.clear()
                    print("Программа очищает содержимое объекта QTextEdit...")
                    for user in users:
                        combobox.addItem(user)
                        print("Программа обновляет информацию об списках...")
            push_add.clicked.connect(if_but_press)
            dialog.exec_()
            
        elif button == button_box.button(QDialogButtonBox.Cancel):
            sign.close()
            print("Надпись закрывается...")
            button_box.close()
            print("Кнопка закрывается...")
    button_box.clicked.connect(Ok_canl)
def del_user():     
    del_sign = QTextBrowser(window)
    del_sign.setText("Вы точно хотите удалить пользователя из списка?")
    del_sign.setGeometry(295,200,156,31)
    del_sign.resize(180,40)
    del_sign.show()
    print("Создаётся новая надпись, также параметры к ней...")
    
    del_but = QDialogButtonBox(window)
    del_but.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    del_but.show()
    del_but.setGeometry(310,250,156,31)
    del_but.show()
    print("Программа создаёт интерактивные кнопки, а также их параметры...")
    def ok_but(button):
        if button == del_but.button(QDialogButtonBox.Ok):
            del_sign.hide()
            print("Программа прячет надпись...")
            del_but.hide()
            print("Программа прячет кнопки...")
            
            dialog2 = QDialog()
            dialog2.resize(248,229)
            dialog2.setWindowTitle("Delete Mode")
            dialog_icon = QIcon("Icon.png")
            dialog2.setWindowIcon(dialog_icon)
            dialog2.setWindowFlags(dialog2.windowFlags() & ~Qt.WindowContextHelpButtonHint)
            dialog2.show()
            print("Программа создаёт новоё окно и его параметры...")
            
            del_user_text = QTextBrowser(dialog2)
            del_user_text.setText("Введите сюда имя/фамилию человека которого вы удалить из списка.")
            del_user_text.setGeometry(20,0,211,51)
            del_user_text.show()
            print("Программа создаёт текстовое поле с информацией и его параметры...")
            
            del_user_list = QTextEdit(dialog2)
            del_user_list.setGeometry(70,70,111,31)
            del_user_list.show()
            print("Программа создаёт поле для ввода и его параметры...")
            del_button = QPushButton("Удалить из списка", dialog2)
            del_button.setGeometry(50,130,151,23)
            del_button.show()
            print("Программа создаёт кнопку подтверждения и его параметры...")
            
            def if_but_press_to_del():
                del_username = del_user_list.toPlainText()
                if del_username in users:
                    users.remove(del_username)
                    print("Программа удаляет содержимое списка...")
                    save_users(users)
                    print("Программа сохраняет список...")
                    del_user_list.clear()
                    print("Программа очищает содержимое объекта QTextEdit...")
                    # Получаем индекс элемента в combobox по его значению (имени пользователя)
                    index = combobox.findText(del_username)
                    if index != -1:
                        combobox.removeItem(index)
                    print("Программа обновляет информацию об списках...")
                elif del_username != "" and del_username not in users:
                    print("Данного пользователя не существует")
                    dialog2.setWindowTitle("Error")
                    print("Программа применяет новое названия для объекта dialog2")
                    dialog_icon2 = QIcon("Error.png")
                    print("Программа применяет новую иконку для объекта dialog2")
                    dialog2.setWindowIcon(dialog_icon2)
                    
                    del_user_text.setText("Ошибка! Даного пользоателя нету в списке, попробуйте заново.")
                    del_user_text.setGeometry(20,50,211,51)
                    print("Программа применяет новые параметры в del_user_text")
                    
                    del_button.hide()
                    del_user_list.hide()
                    print("Программа прячет кнопки...")
                    
                    ok_to_res = QPushButton("ОК", dialog2)
                    ok_to_res.setGeometry(70,130,111,31)
                    ok_to_res.show()
                    print("Программа создаёт и применяет новые значения для кнопки...")
                    
                    def if_but_press():
                        dialog2.setWindowTitle("Delete Mode")
                        dialog_icon = QIcon("Icon.png")
                        dialog2.setWindowIcon(dialog_icon)
                        print("Программа возвращает параметры окна...")
                        
                        ok_to_res.hide()
                        del_button.show()
                        del_user_list.show()
                        del_user_list.clear()
                        print("Программа изменяет параметры кнопок...")
                        
                        del_user_text.setText("Введите сюда имя/фамилию человека которого вы удалить из списка.")
                        del_user_text.setGeometry(20,0,211,51)
                    ok_to_res.clicked.connect(if_but_press)
                    
                else:
                    print("Вы не ввели какие либо значения ")
                    dialog2.setWindowTitle("Error")
                    print("Программа применяет новое названия для объекта dialog2")
                    dialog_icon2 = QIcon("Error.png")
                    print("Программа применяет новую иконку для объекта dialog2")
                    dialog2.setWindowIcon(dialog_icon2)
                    
                    del_button.hide()
                    del_user_list.hide()
                    print("Программа прячет кнопки...")
                    
                    del_user_text.setText("Ошибка! Вы не ввели каких-либо значений, попробуйте снова!")
                    del_user_text.setGeometry(20,50,211,51)
                    
                    ok_to_close = QPushButton("OK", dialog2)
                    print("Программа создаёт новую кнопку...")
                    ok_to_close.setGeometry(70,130,111,31)
                    ok_to_close.show()
                    print("Программа применяет новые параметры для кнопки ok_to_close")
                    
                    def close():
                        print("Программа создаёт новую функцию...")
                        
                        dialog2.close()
                        print("Программа закрывает диалоговое окно...")
                    ok_to_close.clicked.connect(close)
                    print("Вы ввели неправильное значения, удаления не произойдёт...")
            del_button.clicked.connect(if_but_press_to_del)
            dialog2.exec_()
        elif button == del_but.button(QDialogButtonBox.Cancel):
            del_sign.close()
            print("Программа закрывает надпись...")
            del_but.close()
            print("Программа закрывает кнопки...")
        
    del_but.clicked.connect(ok_but)

    
combobox = QComboBox(window)  # Создаем пустой QComboBox с родителем window
print("combobox создаётся...")
combobox.setGeometry(10, 1, 351, 51)
print("Устанавливаются параметры для combobox...")



for user in users:
    combobox.addItem(user)  # Добавляем элементы из списка users в combobox
    print("Программа добавляет элементы из списка...")

add_user = QPushButton("Добавить нового пользователя", window) #Создаём кнопку которая позволяет добавить нового пользователя
add_user.setGeometry(370, 0, 191, 51)
add_user.clicked.connect(adding_mode)
print("Кнопка создаётся и задаются параметры...")
    
delete_user = QPushButton("Удалить пользователя", window)
delete_user.setGeometry(570, 0, 211, 51)
delete_user.clicked.connect(del_user)
print("Кнопка создаётся и задаются параметры...")
    
combobox.show()
add_user.show()
delete_user.show()
window.show()
sys.exit(app.exec_())
