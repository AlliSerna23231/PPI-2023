import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from acudiente import VentanaAcudiente
from docente import Ventana_Docente
from iniciar import Inicar


class Cliente_Usua(QMainWindow):
    def __init__(self, parent=None):
        super(Cliente_Usua, self).__init__(parent)

        self.setWindowTitle("Data Comunity -- Registro")

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
        self.imagenFondo = QPixmap('imagenes/flore.png')

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
        self.horizontal.setContentsMargins(144, 30, 30, 30)

        # *****************Layout IZQUIERDO******************

        # creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Tipo de Usuario")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Billy Ohio", 12))

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
        self.letrero2.setText("Por favor registre la información en el formulario"
                              "\ncorrespondiente al usuario.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto y margenes:
        self.letrero2.setStyleSheet("color: #215636; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 3px solid #215636;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el botón para el usuario padre:
        self.botonusuariop = QPushButton("Padre")
        self.botonusuariop.setFixedWidth(100)
        self.botonusuariop.setStyleSheet("background-color: #215636;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonusuariop.clicked.connect(self.accion_usuarioPadre)

        # Hacemos el botón para el usuario docente:
        self.botonusuariod = QPushButton("Docente")
        self.botonusuariod.setFixedWidth(100)
        self.botonusuariod.setStyleSheet("background-color: #215636;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonusuariod.clicked.connect(self.accion_usuarioDocente)

        # Hacemos el usuario psicologo:
        self.botonusuariops = QPushButton("Psicólogo")
        self.botonusuariops.setFixedWidth(100)
        self.botonusuariops.setStyleSheet("background-color: #215636;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonusuariops.clicked.connect(self.accion_usuarioPsicologo)

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonusuariop)
        self.ladoIzquierdo.addRow(self.botonusuariod)
        self.ladoIzquierdo.addRow(self.botonusuariops)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # *****************Layout DERECHO******************

        # creamos el layout del lado izquierdo:
        self.ladoDerecho = QFormLayout()

        self.ladoDerecho.setContentsMargins(100, 390, 0, 0)


        # Hacemos el botón para continuar:
        self.botonContinuar = QPushButton("Continuar")
        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet("background-color: #00E420;"
                                            "color: #1E1E1E;"
                                            "padding: 10px;"
                                            "margin-top: 40px;")
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)

        # Agregamos los botones al Layout ladoIzquierdo:
        self.ladoDerecho.addRow(self.botonContinuar)

        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ---------------OJO IMPORTANTE PONER AL FINAL-----------
        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)


        # Crear etiqueta para el pie de página
        footer = QLabel('© 2023 Data Comunity. Todos los derechos reservados.', self)
        footer.setFixedWidth(600)
        footer.setFixedHeight(70)
        footer.setStyleSheet("background-color: #215636; color: #FEFFFF;")
        footer.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # Agregar el pie de página a la barra de estado
        self.statusBar().addWidget(footer)

    def accion_usuarioDocente(self):
        self.hide()
        self.docente = Ventana_Docente(self)
        self.docente.show()

    def accion_usuarioPsicologo(self):
       pass


    def accion_usuarioPadre(self):
        self.hide()
        self.acudiente = VentanaAcudiente(self)
        self.acudiente.show()

    def accion_botonContinuar(self):
        self.hide()
        self.iniciar = Inicar(self)
        self.iniciar.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un onjeto de tipo Ventana1 con el nombre de ventana1
    ventanaUsua = Cliente_Usua()
    # hacer que objeto ventana 1 se vea
    ventanaUsua.show()

    sys.exit(app.exec_())