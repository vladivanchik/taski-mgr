import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QDialogButtonBox, QDialog, QTextBrowser, QTextEdit
from PyQt5.QtGui import QIcon
from main import save_users
from main import load_users
from main import users
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

def adding_mode():
    sign = QTextBrowser(window)
    sign.setText("Вы точно хотите добавить нового пользователя?")
    sign.show()
    sign.setGeometry(30,80,201,51)
    sign.resize(180,40)
    print("Программа создаёт надпись и её параметры ...")
    
    button_box = QDialogButtonBox(window)
    button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.show()
    button_box.setGeometry(45,140,156,21)
    print("Программа создаёт кнопку действий и её параметры...")
    
    def Ok_canl(button):
        print("Программа создаёт новую функцию...")
        
        if button == button_box.button(QDialogButtonBox.Ok):
            dialog = QDialog()
            dialog.resize(248,229)
            dialog.setWindowTitle("Adding Mode")
            dialog_icon = QIcon("Icon.png")
            dialog.setWindowIcon(dialog_icon)
            print("Программа создаёт новоё окно и его параметры...")
                
            add_user_text = QTextBrowser(dialog)
            add_user_text.setText("Введите сюда имя/фамилию человека которого вы хотите сюда добавить.")
            add_user_text.setGeometry(20,0,211,51)
            add_user_text.show()
            print("Программа создаёт текстовое поле с информацией и его параметры...")
            
            add_user_in_list = QTextEdit(dialog)
            add_user_in_list.setGeometry(70,70,111,31)
            add_user_in_list.show()
            print("Программа создаёт поле для ввода и его параметры...")
            push_add = QPushButton("Добавить в список", dialog)
            push_add.setGeometry(50,130,151,23)
            push_add.show()
            print("Программа создаёт кнопку подтверждения и его параметры...")
            def if_but_press():
                username = add_user_in_list.toPlainText()
                print("Программа создаёт новую переменную в которой будет передана информация из add_user_in_list...")
                if username != "":
                    users.append(username)
                    print("Программа добавляет в список новую информацию...")
                    save_users(users)
                    print("Программа сохраняет список...")
                    add_user_in_list.clear()
                    print("Программа очищает содержимое объекта QTextEdit...")
                    for user in users:
                        combobox.addItem(user)
                        print("Программа обновляет информацию об списках...")
                
                else:
                    print("Ошибка! В QTextEdit, нету никакой информации...")
                    dialog.setWindowTitle("Error!")
                    print("Программа изменяет названия диалогового окна на \"Error\"...")
                    dialog_icon = QIcon("Error.png")
                    print("Программа применяет новую иконку...")
                    dialog.setWindowIcon(dialog_icon)
                    
                    add_user_text.setText("Ошибка! Вы не ввели никаких данных, попробуйте снова")
                    print("Программа изменяет параметры для объекта add_user_text...")
                    
                    ok_to_close = QPushButton("Ок", dialog)
                    print("Программа создаёт новую кнопку...")
                    ok_to_close.setGeometry(70,55,111,31)
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
                        
                        sign.close()
                        print("Надпись закрывается...")
                        
                        button_box.close()
                        print("Кнопки закрываются...")
                        
                    ok_to_close.clicked.connect(dia_close)
            push_add.clicked.connect(if_but_press)
            dialog.exec_()
                
        elif button == button_box.button(QDialogButtonBox.Cancel):
            sign.close()
            button_box.close()
    button_box.clicked.connect(Ok_canl)
    
combobox = QComboBox(window)  # Создаем пустой QComboBox с родителем window
combobox.setGeometry(10, 1, 351, 51)

for user in users:
    combobox.addItem(user)  # Добавляем элементы из списка users в combobox

add_user = QPushButton("Добавить нового пользователя", window) #Создаём кнопку которая позволяет добавить нового пользователя
add_user.setGeometry(370, 0, 191, 51)
add_user.clicked.connect(adding_mode)
    
    
del_user = QPushButton("Удалить пользователя", window)
del_user.setGeometry(570, 0, 211, 51)

combobox.show()
add_user.show()
del_user.show()
window.show()
sys.exit(app.exec_())
