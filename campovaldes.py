import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QLabel, QPushButton


class VentanaCampo(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Campo Valdés")

        self.ancho = 1000
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedSize(self.ancho, self.alto)

        # cargar la imagen del icono
        icono = QIcon('imagenes/institucion.jpeg')

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
        self.letrero1.setText("¿Qué es la Campo Valdés?")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setAlignment(Qt.AlignCenter)
        print("Estableciendo estilo para letrero1...")
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 5px;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.letreroM = QLabel()
        self.letreroM.setText("MISIÓN")
        self.letreroM.setFont(self.letra1)
        self.letreroM.setAlignment(Qt.AlignLeft)  # Agregar aquí el atributo Qt.AlignLeft
        self.letreroM.setStyleSheet("background-color: #EEEEEE; color: #002502; padding: 5px;")
        self.vertical.addWidget(self.letreroM)
        self.vertical.addStretch()

        # Agregar QLabel con la Misión de la institución
        self.letra2 = QFont()
        self.letra2.setPointSize(10)

        self.mision = QLabel()
        self.mision.setText(
            "La Institución Educativa Campo Valdés es una entidad de carácter oficial y mixto, ofrece los niveles de Preescolar, Básica y Media Académica; en sus \nprocesos implementa estrategias pedagógicas socioculturales que permiten desarrollar las competencias y estimular las múltiples inteligencias del sujeto. \nBusca formar ciudadanos críticos, honestos, justos, promotores del desarrollo humano y social, con capacidad de liderar la transformación de sus contextos \ny de vincularse a la educación superior.\n")
        self.mision.setFont(self.letra2)
        self.vertical.addWidget(self.mision)
        self.vertical.addStretch()

        self.letreroV = QLabel()
        self.letreroV.setText("VISIÓN")
        self.letreroV.setFont(self.letra1)
        self.letreroV.setAlignment(Qt.AlignLeft)  # Agregar aquí el atributo Qt.AlignLeft
        self.letreroV.setStyleSheet("background-color: #EEEEEE; color: #002502; padding: 4px;")
        self.vertical.addWidget(self.letreroV)
        self.vertical.addStretch()

        # Agregar QLabel con la Visión de la institución
        self.vision = QLabel()
        self.vision.setText(
            "Para el año 2020, la Institución Educativa Campo Valdés será reconocida como una entidad que promueve la vinculación a la educación superior de carácter \npúblico y que forma jóvenes críticos, honestos, justos y promotores\n")
        self.vision.setFont(self.letra2)
        self.vertical.addWidget(self.vision)
        self.vertical.addStretch()

        self.letreroP = QLabel()
        self.letreroP.setText("POLÍTICA DE CALIDAD")
        self.letreroP.setFont(self.letra1)
        self.letreroP.setAlignment(Qt.AlignLeft)  # Agregar aquí el atributo Qt.AlignLeft
        self.letreroP.setStyleSheet("background-color: #EEEEEE; color: #002502; padding: 4px;")
        self.vertical.addWidget(self.letreroP)
        self.vertical.addStretch()

        # Agregar QLabel de Politica de Calidad
        self.polica = QLabel()
        self.polica.setText(
            "Para cumplir eficientemente con su misión, la institución educativa campo valdés se compromete a:"
            "\n\n"
            "* Consolidar canales de comunicación asertivos y eficaces que faciliten una participación e interacción de todos los actores de la institución educativa.\n"
            "* Promover espacios formativos para la comunidad educativa, que permitan el intercambio de conocimientos y experiencias.\n"
            "* Priorizar la asignación de recursos para el desarrollo de los procesos formativos de los estudiantes.\n"
            "* Promover la construcción del proyecto de vida acorde con los principios y valores institucionales.\n")
        self.polica.setFont(self.letra2)
        self.vertical.addWidget(self.polica)
        self.vertical.addStretch()

        self.letreroB = QLabel()
        self.letreroB.setText("OBJETIVOS DE CALIDAD")
        self.letreroB.setFont(self.letra1)
        self.letreroB.setAlignment(Qt.AlignLeft)  # Agregar aquí el atributo Qt.AlignLeft
        self.letreroB.setStyleSheet("background-color: #EEEEEE; color: #002502; padding: 4px;")
        self.vertical.addWidget(self.letreroB)
        self.vertical.addStretch()

        # Agregar QLabel de Objetos de Calidad
        self.objetos = QLabel()
        self.objetos.setText(
            "* Garantizar un proyecto educativo consecuente con la filosofía institucional y con las necesidades de la población que se atiende.\n"
            "* Ofrecer y desarrollar un programa de formación integral orientado al fortalecimiento de las dimensiones humanas y al desarrollo \n    de las inteligencias múltiples, acorde con las necesidades de nuestra población y las exigencias del mundo contemporáneo.\n\n"
            "* Promover en el personal administrativo y docente el desarrollo de habilidades y competencias, la apropiación de la cultura \n    institucional y el buen clima laboral, para garantizar la prestación de un servicio educativo con calidad..\n\n"
            "* Garantizar el mejoramiento continuo a través de acciones preventivas, correctivas y de mejora.\n")
        self.objetos.setFont(self.letra2)
        self.vertical.addWidget(self.objetos)
        self.vertical.addStretch()

        # establecemos los colores de los letreros
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 4px;")
        self.mision.setStyleSheet("color: #364437;")
        self.vision.setStyleSheet("color: #364437;")
        self.polica.setStyleSheet("color: #364437;")
        self.objetos.setStyleSheet("color: #364437;")

        self.botonRegresar = QPushButton("Regresar")
        self.botonRegresar.setFixedWidth(150)
        self.botonRegresar.setStyleSheet("background-color: #AAAAAA; color: #1E1E1E; padding: 5px;")
        self.vertical.addWidget(self.botonRegresar)
        self.botonRegresar.clicked.connect(self.accion_botonRegresar)
        self.vertical.addStretch()

    def accion_botonRegresar(self):
        self.hide()
        self.ventanaAnterior.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    campovaldes = VentanaCampo()
    campovaldes.show()
    sys.exit(app.exec_())
