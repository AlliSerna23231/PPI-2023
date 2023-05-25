import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QDialog, QDialogButtonBox, QMainWindow, QFormLayout, QHBoxLayout
import re


class Ventana_Docente(QMainWindow):
    def __init__(self, anterior=None):
        super(Ventana_Docente, self).__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Formulario de Registro-- Docente")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/datacomunnity.jpg"))

        self.ancho = 900
        self.alto = 600

        self.setFixedSize(self.ancho, self.alto)

        # ventana en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la ventana no se pueda cambiar de tamaño
        # se fija el ancho y alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        # definimos la imagen
        self.imagenFondo = QPixmap('imagenes/paisaje.jpg')

        # asignamos la imagen
        self.fondo.setPixmap(self.imagenFondo)

        # establecer el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # el tamaño de la imagen se adapta al tamaño de su contenedor
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # establecemos la ventana fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribuccion de los elementos en Layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # *****************Layout IZQUIERDO******************

        # creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Información del Usuario")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero1.setStyleSheet("color: #215636;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Les escribimos el e¿texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero2.setStyleSheet("color: #215636; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #215636;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemoc el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar la contraseña:
        self.password1 = QLineEdit()
        self.password1.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.password1)

        # Hacemos el campo para ingresar la contraseña2:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Contraseña*", self.password2)

        # Hacemos el campo para agregar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el botón para registrar los datos:
        self.botonGuardar = QPushButton("Registrar")
        self.botonGuardar.setFixedWidth(90)
        self.botonGuardar.setStyleSheet("background-color: #215636;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #215636;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Hacemos el botón para regresar:
        self.botonRegresar = QPushButton("Regresar")
        self.botonRegresar.setFixedWidth(90)
        self.botonRegresar.setStyleSheet("background-color: #215636;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonRegresar.clicked.connect(self.accion_botonRegresar)



        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonGuardar, self.botonLimpiar)
        self.ladoIzquierdo.addRow(self.botonRegresar)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # *****************Layout DERECHO******************

        # creamos el layout del lado izquierdo:
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Formulario")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Andalem Mono", 20))

        # Le ponemos el color del texto:
        self.letrero3.setStyleSheet("color: #215636;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Les escribimos el e¿texto
        self.letrero4.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero4.setStyleSheet("color: #215636; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #215636;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # --- 1

        # Hacemos el campo para ingresar la pregunta1:
        self.pin = QLineEdit()
        self.pin.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow("Pin",self.pin)

        # Hacemos el campo para ingresar la materia:
        self.materia = QComboBox()
        self.materia.addItems(["", "Matemáticas", "Español", "Educación Física", "Religión", "Ciencias Naturales", "Sociales", "Artística", "Inglés", "Ética", "Tecnología"])
        self.materia.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow("Materia", self.materia)

        # --- 2

        # Hacemos el campo para ingresar la pregunta2:
        self.genero = QComboBox()
        self.genero.addItems(["", "Masculino", "Femenino", "Otros"])
        self.genero.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow("Género", self.genero)


        # Hacemos el campo para ingresar la pregunta1:
        self.cargo = QComboBox()
        self.cargo.addItems(["", "Docente"])
        self.cargo.setFixedWidth(320)

        # Agregamos estos en el formulario:
        self.ladoDerecho.addRow("Cargo", self.cargo)

        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es horizontal:


        self.fondo.setLayout(self.horizontal)

        # -----------Construccion de la ventana emergente----------------

        # Creamos la ventana de diálogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Poner el icono:
        self.ventanaDialogo.setWindowIcon(QtGui.QIcon("imagenes/datacomunnity.jpg"))

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el boton de aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de Registro Estudiante")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilo al label mensaje:
        self.mensaje.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 10px;")

        # agregamos el label de mensajes
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones.
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana de dialogo:
        self.ventanaDialogo.setLayout(self.vertical)

    def accion_botonGuardar(self):
        # Creamos una variable para validar si los datos estan correctos
        self.datosCorrectos = True

        # Validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password1.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pin.text() == ''


        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # validamos que las contraseñas sean iguales
        if (
                self.password1.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # validar si el documento si es numerico
        if (
                not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El documento debe ser númerico."
                                 "\nNo debe ingresar letras "
                                 "ni caracterés especiales.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

            # limpiamos el campo del documento:
            self.documento.setText('')

        else:
            # Validar si se ha seleccionado un elemento válido de la lista de opciones
            genero_valido = ["Masculino", "Femenino", "Otros"]
            if self.genero.currentText() not in genero_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione un género válido")
                self.ventanaDialogo.exec_()

            cargo_valido = ["Docente"]
            if self.cargo.currentText() not in cargo_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione una cargo válido")
                self.ventanaDialogo.exec_()

            # Validar longitud del PIN
            if len(self.pin.text()) > 5:
                self.datosCorrectos = False
                self.mensaje.setText("El PIN no debe ser mayor a 5 dígitos")
                self.ventanaDialogo.exec_()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/docentes.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password1.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pin.text() + ";"
                + self.genero.currentText() + ";"
                + self.cargo.currentText() + "\n"  # Agregar grado seleccionado
                , encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/docentes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()


    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password1.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pin.setText('')

    def accion_botonRegresar(self):
        # ocultamos la ventana actual
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    docente = Ventana_Docente()
    docente.show()
    sys.exit(app.exec_())
