import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QLabel, QAction, QMessageBox, \
    QPushButton

from campovaldes import VentanaCampo
from datacomunnity import VentanaDataComunnity
from generador import GeneradorListas
from obsdocente import Observaciones_docente
from infoalumno import Info_alumno
from infopadre import Info_padre


class Interfaz(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # poner titulo
        self.setWindowTitle("Data Comunity -- Docente")
        self.setStyleSheet("background-color: #215636;")

        # propiedades de ancho y largo
        self.ancho = 1000
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # establecemos el fondo principal
        self.fondo = QLabel(self)

        self.imagenFondo = QPixmap('imagenes/img_2.png')

        self.fondo.setPixmap(self.imagenFondo)

        # centrar la imagen en la etiqueta
        self.fondo.setAlignment(Qt.AlignCenter)

        # cargar la imagen del icono
        icono = QIcon('imagenes/datacomunnity.jpg')

        # establecer el icono de la ventana
        self.setWindowIcon(icono)

        # Crear etiqueta para el pie de página
        footer = QLabel('© 2023 Data Comunity. Todos los derechos reservados.', self)
        footer.setFixedWidth(1000)
        footer.setFixedHeight(70)
        footer.setStyleSheet("background-color: #215636; color: #FEFFFF;")
        footer.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # Agregar el pie de página a la barra de estado
        self.statusBar().addWidget(footer)

        menu = self.menuBar()
        menu_clista = menu.addMenu("&Crear Lista")
        menu_obse = menu.addMenu("&Observaciones")
        menu_info = menu.addMenu("&Información")

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_clista_abrir = QAction(QIcon(), "&Generador de listas", self)
        menu_clista_abrir.setShortcut("Ctrl+e")  # atajo de tecladp
        menu_clista_abrir.setStatusTip("Generador de listas")  # mensaje en la barra de estado
        menu_clista_abrir.triggered.connect(self.menu_clista_estudiante)  # lanzador
        menu_clista.addAction(menu_clista_abrir)

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_obse_abrir = QAction(QIcon(), "&Observaciones", self)
        menu_obse_abrir.setShortcut("Ctrl+e")  # atajo de tecladp
        menu_obse_abrir.setStatusTip("Observaciones")  # mensaje en la barra de estado
        menu_obse_abrir.triggered.connect(self.menu_observa_estudiantes)  # lanzador
        menu_obse.addAction(menu_obse_abrir)

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_info_abrir = QAction(QIcon(), "&Información Acudiente", self)
        menu_info_abrir.setShortcut("Ctrl+e")  # atajo de tecladp
        menu_info_abrir.setStatusTip("Información Acudiente")  # mensaje en la barra de estado
        menu_info_abrir.triggered.connect(self.menu_info_acudiente)  # lanzador
        menu_info.addAction(menu_info_abrir)

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_info_abrir = QAction(QIcon(), "&Información Alumno", self)
        menu_info_abrir.setShortcut("Ctrl+e")  # atajo de tecladp
        menu_info_abrir.setStatusTip("Información Alumno")  # mensaje en la barra de estado
        menu_info_abrir.triggered.connect(self.menu_info_alumno)  # lanzador
        menu_info.addAction(menu_info_abrir)

        menu.setStyleSheet("color: #FEFFFF;")

        # boton de campo valdes
        boton = QPushButton(self)
        boton.setGeometry(self.ancho - 50, 40, 50, 50)
        boton_size = boton.size()
        # boton.setIconSize(boton_size)
        boton.setIcon(QIcon("imagenes/institucion.jpeg"))
        boton.clicked.connect(self.boton_clickeado)
        boton.setStyleSheet("border: 20px solid black;")

        # boton de data comunity
        botonData = QPushButton(self)
        botonData.setGeometry(self.ancho - 50, 98, 50, 50)  # posición y tamaño del botón
        botonData_size = botonData.size()
        # botonData.setIconSize(botonData_size)
        botonData.setIcon(QIcon("imagenes/datacomunnity.jpg"))
        botonData.clicked.connect(self.boton_clickeadoData)
        botonData.setStyleSheet("border: 20px solid black;")

        self.fondo.setFixedSize(self.imagenFondo.width(), self.imagenFondo.height())

    def boton_clickeado(self):
        self.hide()
        self.campovaldes = VentanaCampo(self)
        self.campovaldes.show()

    def boton_clickeadoData(self):
        self.hide()
        self.datacomunnity = VentanaDataComunnity(self)
        self.datacomunnity.show()

    def menu_clista_estudiante(self):
        self.hide()
        self.generador = GeneradorListas(self)
        self.generador.show()

    def menu_observa_estudiantes(self):
        self.hide()
        self.obsdocente = Observaciones_docente(self)
        self.obsdocente.show()

    def menu_info_acudiente(self):
        self.hide()
        self.infopadre = Info_padre(self)
        self.infopadre.show()

    def menu_info_alumno(self):
        self.hide()
        self.infoalumno = Info_alumno(self)
        self.infoalumno.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Creamos la ventana y la mostramos
    interfaz = Interfaz()
    interfaz.show()

    # Ejecutamos la aplicación
    sys.exit(app.exec_())