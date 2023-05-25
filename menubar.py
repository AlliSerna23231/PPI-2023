import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMessageBox, QDesktopWidget, QLabel, QPushButton

from PyQt5.QtGui import QIcon, QPixmap

from actualizacion import VentanaActualizacion
from registro import VentanaRegistro
from campovaldes import VentanaCampo
from datacomunnity import VentanaDataComunnity
from iniciar import Inicar

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # poner titulo
        self.setWindowTitle("Data Comunity -- Padre")
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
        menu_contacto = menu.addMenu("&Información de contacto")
        menu_docentes = menu.addMenu("&Observacion de Docentes")
        menu_psicologo = menu.addMenu("&Observaciones de Psicologo")

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_contacto_abrir = QAction(QIcon(), "&Registrar Estudiante", self)
        menu_contacto_abrir.setShortcut("Ctrl+e")  # atajo de tecladp
        menu_contacto_abrir.setStatusTip("Registrar estudiante")  # mensaje en la barra de estado
        menu_contacto_abrir.triggered.connect(self.menu_contacto_registrar_estudiante)  # lanzador
        menu_contacto.addAction(menu_contacto_abrir)

        # agregar un elemento de accion al menu, el QIcon es para agregarle un icono
        menu_contacto_abrir = QAction(QIcon(), "&Actualización de datos", self)
        menu_contacto_abrir.setShortcut("ctrl+p")  # atajo de tecladp
        menu_contacto_abrir.setStatusTip("Actualización de datos")  # mensaje en la barra de estado
        menu_contacto_abrir.triggered.connect(self.menu_contacto_datos)  # lanzador
        menu_contacto.addAction(menu_contacto_abrir)

        # agregamos un submenu al menu
        menu_docentes_opciones = menu_docentes.addMenu("&Grupos")
        menu_docentes_opciones_grupos = QAction(QIcon(), "2°1", self)
        menu_docentes_opciones_grupos.setShortcut("Ctrl+f")
        menu_docentes_opciones_grupos.setStatusTip("2°1")
        menu_docentes_opciones_grupos.triggered.connect(self.menu_docentes_buscar)
        menu_docentes_opciones.addAction(menu_docentes_opciones_grupos)

        # agregamos un elemento de acción al submenú
        menu_docentes_opciones_grupos_2 = QAction(QIcon(), "2°2", self)
        menu_docentes_opciones_grupos_2.setShortcut("Ctrl+g")
        menu_docentes_opciones_grupos_2.setStatusTip("2°2")
        menu_docentes_opciones_grupos_2.triggered.connect(self.menu_docentes_buscar)
        menu_docentes_opciones.addAction(menu_docentes_opciones_grupos_2)

        # agregamos un elemento de acción al submenú
        menu_docentes_opciones_grupos_3 = QAction(QIcon(), "2°3", self)
        menu_docentes_opciones_grupos_3.setShortcut("Ctrl+h")
        menu_docentes_opciones_grupos_3.setStatusTip("2°3")
        menu_docentes_opciones_grupos_3.triggered.connect(self.menu_docentes_buscar)
        menu_docentes_opciones.addAction(menu_docentes_opciones_grupos_3)

        # Agregamos un submenu al menu Observaciones de Psicologo
        menu_psicologo_opciones = menu_psicologo.addMenu("&Grupos")
        menu_psicologo_opciones_grupos = QAction(QIcon(), "2°1", self)
        menu_psicologo_opciones_grupos.setShortcut("Ctrl+j")
        menu_psicologo_opciones_grupos.setStatusTip("2°1")
        menu_psicologo_opciones_grupos.triggered.connect(self.menu_psicologo_buscar)
        menu_psicologo_opciones.addAction(menu_psicologo_opciones_grupos)

        # Agregamos dos nuevos elementos de acción al submenú
        menu_psicologo_opciones_grupos_4 = QAction(QIcon(), "2°2", self)
        menu_psicologo_opciones_grupos_4.setShortcut("Ctrl+k")
        menu_psicologo_opciones_grupos_4.setStatusTip("2°2")
        menu_psicologo_opciones_grupos_4.triggered.connect(self.menu_psicologo_buscar)
        menu_psicologo_opciones.addAction(menu_psicologo_opciones_grupos_4)

        menu_psicologo_opciones_grupos_5 = QAction(QIcon(), "2°3", self)
        menu_psicologo_opciones_grupos_5.setShortcut("Ctrl+l")
        menu_psicologo_opciones_grupos_5.setStatusTip("2°3")
        menu_psicologo_opciones_grupos_5.triggered.connect(self.menu_psicologo_buscar)
        menu_psicologo_opciones.addAction(menu_psicologo_opciones_grupos_5)
        # agregamos el color de la letra del menú
        menu.setStyleSheet("color: #FEFFFF;")

        # boton de campo valdes
        boton = QPushButton(self)
        boton.setGeometry(self.ancho - 50, 40, 50, 50)
        boton.setStyleSheet("color: #215636;  padding-bottom: 12px;")
        boton.setIcon(QIcon("imagenes/institucion.jpeg"))
        boton.setIconSize(boton.size())  # Establecer el tamaño del icono igual al tamaño del botón
        boton.clicked.connect(self.boton_clickeado)


        botonData = QPushButton(self)
        botonData.setGeometry(self.ancho - 50, 98, 50, 50)
        botonData.setIcon(QIcon("imagenes/datacomunnity.jpg"))
        botonData.setIconSize(botonData.size())  # Establecer el tamaño del icono igual al tamaño del botón
        botonData.clicked.connect(self.boton_clickeadoData)
        botonData.setStyleSheet("color: #215636;  padding-bottom: 10px;")

        botoncerrar = QPushButton(self)
        botoncerrar.setGeometry(self.ancho - 50, 155, 50, 50)
        botoncerrar.setIcon(QIcon("imagenes/x.webp"))
        botoncerrar.setIconSize(botoncerrar.size())  # Establecer el tamaño del icono igual al tamaño del botón
        botoncerrar.clicked.connect(self.boton_clickeadoCerrar)


        self.fondo.setFixedSize(self.imagenFondo.width(), self.imagenFondo.height())

    def boton_clickeado(self):
        self.hide()
        self.campovaldes = VentanaCampo(self)
        self.campovaldes.show()

    def boton_clickeadoData(self):
        self.hide()
        self.datacomunnity = VentanaDataComunnity(self)
        self.datacomunnity.show()

    def boton_clickeadoCerrar(self):
        sys.exit()

    def menu_contacto_datos(self):
        self.hide()
        self.actualizacion = VentanaActualizacion(self)
        self.actualizacion.show()

    def menu_contacto_registrar_estudiante(self):
        self.hide()
        self.registro = VentanaRegistro(self)
        self.registro.show()

    def menu_docentes_grupos(self):
        QMessageBox.information(self, "Grupos", "Accion Grupos", QMessageBox.Discard)

    def menu_docentes_buscar(self):
        pass

    def menu_psicologo_grupos(self):
        QMessageBox.information(self, "Grupos", "Accion Grupos", QMessageBox.Discard)

    def menu_psicologo_buscar(self):
       pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    menubar = Ventana()
    menubar.show()
    app.exec_()
