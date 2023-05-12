import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


class VentanaDataComunnity(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Data Comunity")

        self.ancho = 1000
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

        self.vertical = QVBoxLayout(self)

        # cargar la fuente en la aplicación
        QFontDatabase.addApplicationFont("fonts/Billy Ohio.otf")

        self.letra1 = QFont()
        self.letra1.setFamily("Billy Ohio")
        self.letra1.setPointSize(12)

        self.letrero1 = QLabel()
        self.letrero1.setText("SOBRE NOSOTROS")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 5px;")
        self.vertical.addWidget(self.letrero1)

        # Agregar QLabel con la Misión de la institución
        self.letra2 = QFont()
        self.letra2.setPointSize(10)

        self.mision = QLabel()
        self.mision.setText(
            "La Institución Educativa Campo Valdés es una entidad de carácter oficial y mixto, ofrece los niveles de Preescolar, Básica y Media Académica; en sus \nprocesos implementa estrategias pedagógicas socioculturales que permiten desarrollar las competencias y estimular las múltiples inteligencias del sujeto. \nBusca formar ciudadanos críticos, honestos, justos, promotores del desarrollo humano y social, con capacidad de liderar la transformación de sus contextos \ny de vincularse a la educación superior.\n")
        self.mision.setFont(self.letra2)
        self.vertical.addWidget(self.mision)
        self.vertical.addStretch()

        # Crear layout horizontal para las imágenes de usuario
        layout_imagenes = QHBoxLayout()

        # Crear diseño vertical para la primera imagen de usuario
        layout_imagen1 = QVBoxLayout()
        imagen1 = QLabel(self)
        imagen1.setPixmap(QPixmap('imagenes/Allis.jpg').scaledToWidth(100))
        imagen1.setAlignment(Qt.AlignCenter)
        layout_imagen1.addWidget(imagen1)
        texto1 = QLabel("Allison Serna Lopera")
        texto1.setAlignment(Qt.AlignCenter)
        layout_imagen1.addWidget(texto1)

        # Agregar el diseño vertical de la primera imagen al diseño horizontal principal
        layout_imagenes.addLayout(layout_imagen1)

        # Crear diseño vertical para la segunda imagen de usuario
        layout_imagen2 = QVBoxLayout()
        imagen2 = QLabel(self)
        imagen2.setPixmap(QPixmap('imagenes/Alex.jpg').scaledToWidth(100))
        imagen2.setAlignment(Qt.AlignCenter)
        layout_imagen2.addWidget(imagen2)
        texto2 = QLabel("Alexander Restrepo")
        texto2.setAlignment(Qt.AlignCenter)
        layout_imagen2.addWidget(texto2)

        # Agregar el diseño vertical de la segunda imagen al diseño horizontal principal
        layout_imagenes.addLayout(layout_imagen2)

        # Crear diseño vertical para la tercera imagen de usuario
        layout_imagen3 = QVBoxLayout()
        imagen3 = QLabel(self)
        imagen3.setPixmap(QPixmap('imagenes/Juan.jpg').scaledToWidth(100))
        imagen3.setAlignment(Qt.AlignCenter)
        layout_imagen3.addWidget(imagen3)
        texto3 = QLabel("Juan Diego Mesa") #Texto debajo de la imagen
        texto3.setAlignment(Qt.AlignCenter)
        layout_imagen3.addWidget(texto3)

        # Agregar el diseño vertical de la tercera imagen al diseño horizontal principal
        layout_imagenes.addLayout(layout_imagen3)

        # Agregar el layout de las imágenes al layout vertical principal
        self.vertical.addLayout(layout_imagenes)

        self.botonRegresar = QPushButton("Regresar")
        self.botonRegresar.setFixedWidth(150)
        self.botonRegresar.setStyleSheet("background-color: #AAAAAA; color: #1E1E1E; padding: 5px;")
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accion_botonRegresar)

        # Crear etiqueta para información de contacto
        contacto = QLabel(
            'Contáctenos: \n\nAllison Serna Lopera - Celular: +57 300 9460711\nAlexander Restrepo - Celular: +57 300 5119170\nJuan Diego Mesa - Celular: +57 322 6505292\n\n\n\n© 2023 Data Comunity. Todos los derechos reservados.',
            self)
        contacto.setFixedWidth(979)
        contacto.setFixedHeight(170)
        contacto.setStyleSheet("background-color: #215636; color: #FEFFFF;")
        contacto.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.vertical.addWidget(contacto)



    def accion_botonRegresar(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    datacomunnity = VentanaDataComunnity()
    datacomunnity.show()
    sys.exit(app.exec_())
