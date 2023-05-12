import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QDialog, QDialogButtonBox
import re



class VentanaAcudiente(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        self.ventanaAnterior = anterior

        self.setWindowTitle("Registrar Acudiente")

        self.ancho = 800
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedSize(self.ancho, self.alto)

        # cargar la imagen del icono
        icono = QIcon('imagenes/datacomunnity.jpg')

        # establecer el icono de la ventana
        self.setWindowIcon(icono)

        self.vertical = QVBoxLayout()
        self.setLayout(self.vertical)

        # cargar la fuente en la aplicación
        QFontDatabase.addApplicationFont("fonts/Billy Ohio.otf")

        self.letra1 = QFont()
        self.letra1.setFamily("Billy Ohio")
        self.letra1.setPointSize(12)

        self.letrero1 = QLabel()
        self.letrero1.setText("Formulario del Acudiente")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 5px;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # Agregar widgets para ingresar información del Acudiente
        self.nombreacudiente1 = QLineEdit()
        self.apellidoacudiente1 = QLineEdit()
        self.nidentificacion1 = QLineEdit()
        self.contacto1 = QLineEdit()
        self.direccion1 = QLineEdit()
        self.id = QLineEdit()
        self.Genero1 = QComboBox()
        self.Genero1.addItems(["", "Masculino", "Femenino", "Otros"])
        self.relacion1 = QComboBox()
        self.relacion1.addItems(["", "Padre", "Madre", "Acudiente"])

        # establecemos el tamaño de los campos
        campo_fijo = 575
        altura_fija = 25
        self.nombreacudiente1.setFixedSize(campo_fijo, altura_fija)
        self.apellidoacudiente1.setFixedSize(campo_fijo, altura_fija)
        self.nidentificacion1.setFixedSize(campo_fijo, altura_fija)
        self.contacto1.setFixedSize(campo_fijo, altura_fija)
        # self.fnacimiento.setMaximumDate(QDate.currentDate())  # Limitar fecha máxima a la fecha actual
        # self.fnacimiento.setCalendarPopup(True)  # Mostrar un calendario emergente para seleccionar fecha
        self.direccion1.setFixedSize(campo_fijo, altura_fija)
        self.Genero1.setFixedSize(campo_fijo, altura_fija)
        self.relacion1.setFixedSize(campo_fijo, altura_fija)

        self.vertical.addWidget(QLabel("Nombre del Acudiente :"))
        self.vertical.addWidget(self.nombreacudiente1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Apellido del Acudiente :"))
        self.vertical.addWidget(self.apellidoacudiente1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Documento del Acudiente :"))
        self.vertical.addWidget(self.nidentificacion1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Contacto del Acudiente :"))
        self.vertical.addWidget(self.contacto1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Dirección de casa:"))
        self.vertical.addWidget(self.direccion1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Género del Acudiente:"))
        self.vertical.addWidget(self.Genero1)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("Relación:"))
        self.vertical.addWidget(self.relacion1)
        self.vertical.addStretch()

        # Agregar botones para guardar y modificar
        self.botonGuardar = QPushButton("Guardar")
        self.botonGuardar.setFixedWidth(150)
        self.botonGuardar.setStyleSheet("background-color: #2AD241; color: #1E1E1E; padding: 5px;")
        self.botonGuardar.clicked.connect(self.accion_botonGuardar)
        self.vertical.addWidget(self.botonGuardar)

        # Agregar botones para que limpie los campos
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(150)
        self.botonLimpiar.setStyleSheet("background-color: #FF4500; color: #1E1E1E; padding: 5px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)
        self.vertical.addWidget(self.botonLimpiar)

        self.botonRegresar = QPushButton("Regresar")
        self.botonRegresar.setFixedWidth(150)
        self.botonRegresar.setStyleSheet("background-color: #AAAAAA; color: #1E1E1E; padding: 5px;")
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accion_botonRegresar)
        self.vertical.addStretch()

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
                self.nombreacudiente1.text() == ''
                or self.apellidoacudiente1.text() == ''
                or self.nidentificacion1.text() == ''
                or self.contacto1.text() == ''
                or self.direccion1.text() == ''
                # or self.fnacimiento.text() == ''

        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe llenar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()
        # validar si el documento si es numerico
        if (
                not self.nidentificacion1.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El documento debe ser númerico."
                                 "\nNo debe ingresar letras "
                                 "ni caracterés especiales.")

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()

            # limpiamos el campo del documento:
            self.nidentificacion1.setText('')

        else:
            # Validar si se ha seleccionado un elemento válido de la lista de opciones
            Genero1_valido = ["Masculino", "Femenino", "Otros"]
            if self.Genero1.currentText() not in Genero1_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione un género válido")
                self.ventanaDialogo.exec_()

            relacion1_valido = ["Padre", "Madre", "Acudiente"]
            if self.relacion1.currentText() not in relacion1_valido:
                self.datosCorrectos = False
                self.mensaje.setText("Seleccione una opción válido")
                self.ventanaDialogo.exec_()

            # Validar el número de celular
            contacto1_valido = re.match(r'^[367]\d{9}$', self.contacto1.text())  # Verifica que el número tenga 10 dígitos y comience con 3, 6 o 7
            if not contacto1_valido:
                self.datosCorrectos = False
                self.mensaje.setText("El número de celular es inválido")
                self.contacto1.setText('')  # borra el número de celular inválido ingresado
                self.ventanaDialogo.exec_()

        # Si los datos están correctos:
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/acudientes.txt', 'ab')

            # traer el texto de los QLineEdit() y los agrega concatenandolos.
            # para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombreacudiente1.text() + ";"
                + self.apellidoacudiente1.text() + ";"
                + self.nidentificacion1.text() + ";"
                # + self.fnacimiento.text() + ";"
                + self.contacto1.text() + ";"
                + self.direccion1.text() + ";"
                + self.Genero1.currentText() + ";"  # Agregar género seleccionado
                + self.relacion1.currentText() + "\n"  # Agregar grado seleccionado
                , encoding='UTF-8'))
            self.file.close()

            self.file = open('datos/acudientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()
    def accion_botonLimpiar(self):

        self.nombreacudiente1.setText('')
        self.apellidoacudiente1.setText('')
        self.nidentificacion1.setText('')
        self.contacto1.setText('')
        self.direccion1.setText('')

    def accion_botonRegresar(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    acudiente = VentanaAcudiente()
    acudiente.show()
    sys.exit(app.exec_())