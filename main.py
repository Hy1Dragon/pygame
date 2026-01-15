from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import random
def SANIS():
    a = ['(@_@)','54','456','745','47','45734','9']
    asgor.setText(random.choice(a))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Underverse')
main_win.resize(400,200)
main_win.show()
asgor=QLabel('(@_@):')

list={'task': 'Купить молоко', 'done': False}
papirus = QPushButton('Pypsik')
v_line = QVBoxLayout()

v_line.addWidget(asgor,alignment = Qt.AlignCenter)

v_line.addWidget(papirus,alignment = Qt.AlignCenter)

main_win.setLayout(v_line)

papirus.clicked.connect(SANIS)

app.exec_()

