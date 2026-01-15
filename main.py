
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit
import random

def add_one():
    pass


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Underverse')

main_win.resize(400,200)
main_win.show()
asgor=QLabel('(@_@):')

button = QPushButton("удалить все")
button2 = QPushButton("удалить выбранную заметку")
button3 = QPushButton("переместить в сделано")
button4 = QPushButton("удалить выбранную заметку")
button5 = QPushButton("добавить")

papirus = QPushButton('добавить')
winner = QLabel('удалить все')
winner1 = QLabel('удалить выбранную заметкy')
winner2 = QLabel('переместить в сделано')
winner3 = QLabel('переместить в список дел')
winner4 = QLabel('удалить выбранную заметку')
winner5 = QLabel('удалить все')
winner.text()
sanis = QLineEdit()
v_line = QVBoxLayout()
h_line = QHBoxLayout()

main_win.setLayout(v_line)

h_line.addLayout(v_line)
v_line.addWidget(asgor,alignment = Qt.AlignCenter)
v_line.addWidget(asgor,alignment = Qt.AlignCenter)
v_line.addWidget(button,alignment = Qt.AlignCenter)
v_line.addWidget(button2,alignment = Qt.AlignCenter)
v_line.addWidget(button3,alignment = Qt.AlignCenter)
v_line.addWidget(button4,alignment = Qt.AlignCenter)
v_line.addWidget(button5,alignment = Qt.AlignCenter)

v_line.addWidget

main_win.setLayout(v_line)
button.clicked.connect(add_one)
button2.clicked.connect(add_one)
button3.clicked.connect(add_one)
button4.clicked.connect(add_one)
button5.clicked.connect(add_one)
sanis.text()
app.exec_()






