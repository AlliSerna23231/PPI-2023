import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, \
    QComboBox, QDialogButtonBox, QDialog, QDateEdit

from acudiente import VentanaAcudiente


class VentanaRegistro(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Registrar Estudiante")

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
        self.letrero1.setText("Formulario del Estudiante")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 5px;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # Agregar widgets para ingresar información del estudiante
        self.nombre = QLineEdit()
        self.apellido = QLineEdit()
        self.documento = QLineEdit()
        self.fnacimiento = QDateEdit()
        self.Genero = QComboBox()
        self.Genero.addItems(["", "Masculino", "Femenino", "Otros"])
        self.grado = QComboBox()
        self.grado.addItems(["", "2°1", "2°2", "2°3"])

        # establecemos el tamaño de los campos
        campo_fijo = 575
        altura_fija = 25
        self.nombre.setFixedSize(campo_fijo, altura_fija)
        self.apellido.setFixedSize(campo_fijo, altura_fija)
        self.documento.setFixedSize(campo_fijo, altura_fija)
        self.fnacimiento.setFixedSize(campo_fijo, altura_fija)
        self.fnacimiento.setMaximumDate(QDate.currentDate())  # Limitar fecha máxima a la fecha actual
        self.fnacimiento.setCalendarPopup(True)  # Mostrar un calendario emergente para seleccionar fecha
        self.Genero.setFixedSize(campo_fijo, altura_fija)
        self.grado.setFixedSize(campo_fijo, altura_fija)

        self.vertical.addWidget(QLabel("*Nombre:"))
        self.vertical.addWidget(self.nombre)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("*Apellido:"))
        self.vertical.addWidget(self.apellido)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("*Número de identificación:"))
        self.vertical.addWidget(self.documento)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("*Fecha de nacimiento:"))
        self.vertical.addWidget(self.fnacimiento)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("*Género:"))
        self.vertical.addWidget(self.Genero)
        self.vertical.addStretch()
        self.vertical.addWidget(QLabel("*Grado:"))
        self.vertical.addWidget(self.grado)
        self.vertical.addStretch()

        # Agregar botones para guardar y modificar
        self.botonGuardar = QPushButton("Guardar")
        self.botonGuardar.setFixedWidth(150)
        self.botonGuardar.setStyleSheet("background-color: #2AD241; color: #1E1E1E; padding: 5px;")
        self.botonGuardar.clicked.connect(self.accion_botonGuardar)
        self.vertical.addWidget(self.botonGuardar)

        self.botonModificar = QPushButton("Modificar")
        self.botonModificar.setFixedWidth(150)
        self.botonModificar.setStyleSheet("background-color: #2AD241; color: #1E1E1E; padding: 5px;")
        self.botonModificar.clicked.connect(self.accion_botonModificar)
        self.vertical.addWidget(self.botonModificar)

        # Agregar botones para que nos lleve al formulario del acudiente
        self.botonAcudiente = QPushButton("Acudiente")
        self.botonAcudiente.setFixedWidth(150)
        self.botonAcudiente.setStyleSheet("background-color: #00E420; color: #1E1E1E; padding: 5px;")
        self.botonAcudiente.clicked.connect(self.accion_botonAcudiente)
        self.vertical.addWidget(self.botonAcudiente)

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
        self.acudiente = VentanaAcudiente(self)
        self.acudiente.show()

    def accion_botonRegresar(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    registro = VentanaRegistro()
    registro.show()
    sys.exit(app.exec_())
