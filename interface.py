import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QDialogButtonBox, QDialog, QTextBrowser
from PyQt5.QtGui import QIcon
from main import save_users
from main import load_users
from main import users

app = QApplication(sys.argv)

window = QMainWindow()
window.setFixedSize(800, 600)
window.setWindowTitle("Taxi Manager")
app_icon = QIcon ("Icon.png")
window.setWindowIcon(app_icon)
window.resize(800, 600)
window.show()

def adding_mode():
    dialog = QDialog()
    dialog.resize(248,229)
    sign = QTextBrowser(dialog)
    sign.setText("Вы точно хотите добавить нового пользователя?")
    sign.show()
    sign.setGeometry(30,80,201,51)
    sign.resize(180,40)
    button_box = QDialogButtonBox(dialog)
    button_box.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    button_box.show()
    button_box.setGeometry(45,140,156,21)
    def Ok_canl(button):
        if button == button_box.button(QDialogButtonBox.Ok):
            print("Hello World!")
        elif button == button_box.button(QDialogButtonBox.Cancel):
            print("Hello World!")
    button_box.clicked.connect(Ok_canl)
    dialog.exec_()
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
