import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox
from main import save_users
from main import load_users
from main import users

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(800, 600)
window.setWindowTitle("Taksi Manager")
window.show()

combobox = QComboBox(window)  # Создаем пустой QComboBox с родителем window
combobox.setGeometry(10, 1, 351, 51)

for user in users:
    combobox.addItem(user)  # Добавляем элементы из списка users в combobox

add_user = QPushButton("Добавить нового пользователя", window) #Создаём кнопку которая позволяет добавить нового пользователя
add_user.setGeometry(370, 0, 191, 51)

del_user = QPushButton("Удалить пользователя", window)
del_user.setGeometry(570, 0, 211, 51)

combobox.show()
add_user.show()
del_user.show()
window.show()
sys.exit(app.exec_())
