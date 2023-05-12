import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QVBoxLayout, QLabel, QPushButton


class VentanaActualizacion(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        self.setWindowTitle("Actualización de datos")

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

        self.vertical = QVBoxLayout()
        self.setLayout(self.vertical)

        # cargar la fuente en la aplicación
        QFontDatabase.addApplicationFont("fonts/Billy Ohio.otf")

        self.letra1 = QFont()
        self.letra1.setFamily("Billy Ohio")
        self.letra1.setPointSize(12)

        self.letrero1 = QLabel()
        self.letrero1.setText("Actualizar Datos")
        self.letrero1.setFont(self.letra1)
        self.letrero1.setAlignment(Qt.AlignCenter)
        self.letrero1.setStyleSheet("background-color: #215636; color: #FFFFFF; padding: 5px;")
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        self.botonRegresar = QPushButton("Regresar al inicio")
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
    actualizacion = VentanaActualizacion()
    actualizacion.show()
    sys.exit(app.exec_())



