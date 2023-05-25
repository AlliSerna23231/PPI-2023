import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton, QVBoxLayout, QDialog, QDialogButtonBox, QComboBox, QDateEdit
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QDate
import re


class VentanaRegistro(QMainWindow):
    def __init__(self, anterior=None):
        super(VentanaRegistro, self).__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Registrar Estudiante")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/datacomunnity.jpg"))

        self.ancho = 600
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
        self.nombre = QLineEdit()
        self.nombre.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre*", self.nombre)

        # Hacemos el campo para ingresar el apellido
        self.apellido = QLineEdit()
        self.apellido.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Apellido*", self.apellido)

        # Hacemos el campo para agregar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar la fecha de nacimiento:
        self.fnacimiento = QDateEdit()
        self.fnacimiento.setMaximumDate(QDate.currentDate())  # Limitar fecha máxima a la fecha actual
        self.fnacimiento.setCalendarPopup(True)  # Mostrar un calendario emergente para seleccionar fecha
        self.fnacimiento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Fecha de nacimiento*", self.fnacimiento)

        # Hacemos el campo para ingresar la genero:
        self.Genero = QComboBox()
        self.Genero.addItems(["", "Masculino", "Femenino", "Otros"])
        self.Genero.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Género", self.Genero)

        # Hacemos el campo para ingresar la grado:
        self.grado = QComboBox()
        self.grado.addItems(["", "2°1", "2°2", "2°3"])
        self.grado.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Grado*", self.grado)

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
                self.nombre.text() == ''
                or self.apellido.text() == ''
                or self.documento.text() == ''
                or self.fnacimiento.text() == ''

        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()
        else:
            # Obtenemos la fecha ingresada en el QDateEdit
            fecha = self.fnacimiento.date()

            # Creamos objetos QDate para las fechas mínima y máxima permitidas
            fecha_minima = QDate(1945, 1, 1)
            fecha_maxima = QDate.currentDate()

            # Validamos que la fecha ingresada esté dentro del rango permitido
            if fecha < fecha_minima or fecha > fecha_maxima:
                self.datosCorrectos = False

                self.mensaje.setText("La fecha de nacimiento debe estar entre el año 1945 y el año actual")

                # Limpiamos el campo de fecha de nacimiento
                self.fnacimiento.setDate(QDate.currentDate())

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
            Genero_valido = ["Masculino", "Femenino", "Otros"]
            if self.Genero.currentText() not in Genero_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione un género válido")
                self.ventanaDialogo.exec_()

            grado_valido = ["2°1", "2°2", "2°3"]
            if self.grado.currentText() not in grado_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione un grado válido")
                self.ventanaDialogo.exec_()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/estudiantes.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombre.text() + ";"
                + self.apellido.text() + ";"
                + self.documento.text() + ";"
                + self.fnacimiento.text() + ";"
                + self.Genero.currentText() + ";"  # Agregar género seleccionado
                + self.grado.currentText() + "\n"  # Agregar grado seleccionado
                , encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/estudiantes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()

    def accion_botonModificar(self):
        pass

    def accion_botonLimpiar(self):

        self.nombre.setText('')
        self.apellido.setText('')
        self.documento.setText('')

    def accion_botonAcudiente(self):
        self.hide()
        self.acudiente = VentanaRegistro(self)
        self.acudiente.show()

    def accion_botonRegresar(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    acudiente = VentanaRegistro()
    acudiente.show()
    sys.exit(app.exec_())
