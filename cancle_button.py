from PyQt5 import QtWidgets
import sys
import logging

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

line1_edit = QtWidgets.QLineEdit()
line2_edit = QtWidgets.QLineEdit()

run_btn=QtWidgets.QPushButton("Run")

def main():

    w.close()

run_btn.clicked.connect(main)

# layout = QtWidgets.QVBoxLayout()
# layout.addWidget(line1_edit)
# layout.addWidget(run_btn)
# layout.addWidget(run_btn)

button = QtWidgets.QPushButton()
button.setStyleSheet('QPushButton {background-color: gray; color: black;}')
button.setText('little button')

button.show()

# w.setLayout(layout)
# w.show()
sys.exit(app.exec_())