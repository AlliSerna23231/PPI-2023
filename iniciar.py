import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QIcon
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QApplication


class Inicar(QMainWindow):

    def __init__(self, anterior=None):
        super(Inicar, self).__init__(anterior)
        self.ventanaAnterior = anterior
        self.setWindowTitle("Data Comunity -- Inicio Sesión") #Poner una imagen de usuario y quitar el titulo
        self.setWindowIcon(QIcon("imagenes/datacomunnity.jpg"))
        self.setStyleSheet("background-color: white;")
        self.ancho = 600
        self.alto = 600
        self.resize(self.ancho, self.alto)

        self.pantalla = (self.frameGeometry())
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.interna = QWidget()
        self.interna.setContentsMargins(50, 50, 50, 50)

        self.setCentralWidget(self.interna)
        self.vertical = QVBoxLayout()

        self.cuadricula = QGridLayout()
        self.interna.setLayout(self.cuadricula)

        self.inicio_label = QLabel("Inicio Sesión")
        self.inicio_label.setAlignment(Qt.AlignCenter)
        self.inicio_label.setStyleSheet("color: black; font-size: 25px; font-family: Poppins; font-weight: bold;")
        self.cuadricula.addWidget(self.inicio_label, 0, 0, 1, 3)

        self.usuario_label = QtWidgets.QLabel('Usuario')
        self.usuario_label.setAlignment(Qt.AlignCenter)
        self.usuario_label.setStyleSheet("color: black; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.usuario_label, 1, 0, 1, 1)

        self.fullname_edit = QtWidgets.QLineEdit(self)
        self.fullname_edit.setAlignment(Qt.AlignCenter)
        self.fullname_edit.setStyleSheet(
            "color: black; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid black; ")
        self.cuadricula.addWidget(self.fullname_edit, 1, 1)

        self.documento_label = QtWidgets.QLabel('Documento')
        self.documento_label.setAlignment(Qt.AlignCenter)
        self.documento_label.setStyleSheet("color: black; font-size: 20px; font-family: Poppins;")
        self.cuadricula.addWidget(self.documento_label, 2, 0, 1, 1)

        self.email_edit = QtWidgets.QLineEdit(self)
        self.email_edit.setAlignment(Qt.AlignCenter)
        self.email_edit.setStyleSheet(
            "color: black; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid black; ")
        self.cuadricula.addWidget(self.email_edit, 2, 1)

        self.password2_label = QtWidgets.QLabel('Contraseña')
        self.password2_label.setAlignment(Qt.AlignCenter)
        self.password2_label.setStyleSheet("color: black; font-size: 20px; font-family: Poppins; ")
        self.cuadricula.addWidget(self.password2_label, 3, 0)

        self.password2_edit = QtWidgets.QLineEdit(self)
        self.password2_edit.setAlignment(Qt.AlignCenter)
        self.password2_edit.setStyleSheet(
            "color: black; font-size: 18px; font-family: Poppins; padding: 5px; border-radius:10px; "
            "border: 1px solid black; ")
        self.cuadricula.addWidget(self.password2_edit, 3, 1)
        self.password2_edit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.iniciar_button = QtWidgets.QPushButton('Iniciar')
        self.iniciar_button.setStyleSheet("background-color: #00E420;"
                                            "color: #1E1E1E;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")
        self.iniciar_button.clicked.connect(self.iniciar)
        self.cuadricula.addWidget(self.iniciar_button, 4, 0, 2, 4)

        self.botonVolver = QPushButton("Regresar")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: #215636;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonVolver.clicked.connect(self.volver)
        self.cuadricula.addWidget(self.botonVolver, 5, 0)

    def iniciar(self):
        pass

    def volver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # crear un onjeto de tipo Ventana1 con el nombre de ventana1
    iniciar = Inicar()
    # hacer que objeto ventana 1 se vea
    iniciar.show()

    sys.exit(app.exec_())