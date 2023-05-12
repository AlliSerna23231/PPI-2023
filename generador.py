import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, QTableWidget, \
    QMessageBox, QListWidget, QListWidgetItem, QLineEdit, QFileDialog


class GeneradorListas(QWidget):
    def __init__(self, anterior=None):
        super().__init__()

        self.ventanaAnterior = anterior

        # poner titulo
        self.setWindowTitle("Generador de listas")

        # propiedades de ancho y largo
        self.ancho = 600
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # cargar la imagen del icono
        icono = QIcon('imagenes/datacomunnity.jpg')

        # establecer el icono de la ventana
        self.setWindowIcon(icono)

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Creamos un botón "Regresar"
        self.regresar_button = QPushButton("Regresar")
        self.regresar_button.setStyleSheet("background-color: #AAAAAA; color: #1E1E1E; padding: 5px;")
        self.regresar_button.clicked.connect(self.regresar)

        # Creamos un layout horizontal y agregamos el botón "Regresar"
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addStretch()
        layout_horizontal.addWidget(self.regresar_button)

        # Agregamos un QLineEdit para que el usuario ingrese la cantidad de filas
        self.cantidad_filas_edit = QLineEdit()
        self.cantidad_filas_edit.setPlaceholderText("Ingrese la cantidad de filas")
        self.cantidad_filas_edit.setMaximumWidth(200)

        # Creamos un botón "Agregar fila"
        self.agregar_fila_button = QPushButton("Agregar fila")
        self.agregar_fila_button.setStyleSheet("background-color: #00E420; color: #1E1E1E; padding: 5px;")
        self.agregar_fila_button.clicked.connect(self.agregar_fila)

        # Creamos una tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["*Nombre", "*Apellido", "*Edad", "*Documento", "*Grupo"])

        # Creamos un botón "Eliminar fila"
        self.eliminar_fila_button = QPushButton("Eliminar fila")
        self.eliminar_fila_button.setStyleSheet("background-color: #FF4500; color: white; padding: 5px;")
        self.eliminar_fila_button.clicked.connect(self.eliminar_fila)

        # Creamos un botón "Limpiar Campo"
        self.limpiar_campo_button = QPushButton("Limpiar campo")
        self.limpiar_campo_button.setStyleSheet("background-color: #FF4500; color: white; padding: 5px;")
        self.limpiar_campo_button.clicked.connect(self.limpiar_campo)

        # Creamos un botón "Mostrar lista"
        self.mostrar_lista_button = QPushButton("Mostrar lista")
        self.mostrar_lista_button.setStyleSheet("background-color: #00E420; color: #1E1E1E; padding: 5px;")
        self.mostrar_lista_button.clicked.connect(self.mostrar_lista)

        # Creamos un layout horizontal y agregamos los botones "Agregar fila" y "Regresar"
        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(self.cantidad_filas_edit)
        layout_horizontal.addStretch()
        layout_horizontal.addWidget(self.agregar_fila_button)
        layout_horizontal.addStretch()
        layout_horizontal.addWidget(self.eliminar_fila_button)
        layout_horizontal.addWidget(self.limpiar_campo_button)
        layout_horizontal.addStretch()
        layout_horizontal.addWidget(self.mostrar_lista_button)
        layout_horizontal.addStretch()
        layout_horizontal.addWidget(self.regresar_button)

        # Creamos un layout vertical y agregamos la tabla y el layout horizontal
        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.tabla)
        layout_vertical.addLayout(layout_horizontal)

        # Establecemos el layout vertical como el layout de la ventana
        self.setLayout(layout_vertical)

    def regresar(self):
        self.hide()
        self.ventanaAnterior.show()

    def agregar_fila(self):
        # Obtener la cantidad de filas ingresada por el usuario
        cantidad_filas_text = self.cantidad_filas_edit.text()
        if not cantidad_filas_text.isdigit():
            # Si la cantidad de filas ingresada no es un número entero, mostrar un mensaje de error
            QMessageBox.warning(self, "Error", "Ingrese un número de filas entero válido")
            return
        cantidad_filas = int(cantidad_filas_text)
        if cantidad_filas <= 0 or cantidad_filas > 50:
            # Si la cantidad de filas ingresada no está en el rango permitido, mostrar un mensaje de error
            QMessageBox.warning(self, "Error", "Ingrese un número entero mayor a 0 y menor o igual a 50")
            return

        # Agregar la cantidad de filas especificada a la tabla
        self.tabla.setRowCount(self.tabla.rowCount() + cantidad_filas)

    def eliminar_fila(self):
        # Obtenemos la fila seleccionada y la eliminamos de la tabla
        fila = self.tabla.currentRow()

        if fila >= 0:

            self.tabla.removeRow(fila)

    def limpiar_campo(self):
        self.tabla.clearContents()  # borra los datos de la tabla
        self.tabla.setHorizontalHeaderLabels(["*Nombre", "*Apellido", "*Edad", "*Documento","*Grupo"])  # establece las etiquetas de la cabecera de la tabla

    def validar_info(self):
        # Comprobar si todos los campos obligatorios están llenos
        nombre = self.tabla.item(self.tabla.rowCount() - 1, 0)
        apellido = self.tabla.item(self.tabla.rowCount() - 1, 1)
        edad = self.tabla.item(self.tabla.rowCount() - 1, 2)
        documento = self.tabla.item(self.tabla.rowCount() - 1, 3)
        grupo = self.tabla.item(self.tabla.rowCount() - 1, 4)

        if nombre is None or nombre.text() == "":
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre")
            return False

        if apellido is None or apellido.text() == "":
            QMessageBox.warning(self, "Error", "Por favor ingrese un apellido")
            return False

        if edad is None or edad.text() == "":
            QMessageBox.warning(self, "Error", "Por favor ingrese una edad")
            return False

        if edad is not None and edad.text().isdigit():
            edad_int = int(edad.text())
            if edad_int < 7 or edad_int > 15:
                QMessageBox.warning(self, "Error", "La edad debe estar entre 7 y 15 años")
                return False
        else:
            QMessageBox.warning(self, "Error", "Por favor ingrese una edad válida (número entero)")
            return False

        if documento is None or documento.text() == "":
            QMessageBox.warning(self, "Error", "Por favor ingrese un número de documento")
            return False

        if documento is not None and documento.text().isdigit():
            if len(documento.text()) != 10:
                QMessageBox.warning(self, "Error", "El documento debe tener 10 dígitos")
                return False
        else:
            QMessageBox.warning(self, "Error", "Por favor ingrese un documento válido (número entero)")
            return False


        if grupo is None or grupo.text() == "":
            QMessageBox.warning(self, "Error", "Por favor seleccione un grupo")
            return False

        # Comprobar si la información ingresada es válida
        # Aquí puedes agregar cualquier otra validación que necesites

        return True

    def mostrar_lista(self):
        # Validar la información antes de mostrar la lista
        if not self.validar_info():
            return

        # Crear una nueva ventana para mostrar la lista
        self.lista_window = QWidget()
        self.lista_window.setWindowTitle("Lista generada")

        # cargar la imagen del icono
        icono = QIcon('imagenes/datacomunnity.jpg')

        # establecer el icono de la ventana
        self.lista_window.setWindowIcon(icono)

        self.lista_window.setGeometry(100, 100, 600, 600)

        # Crear una lista con la información de la tabla
        lista = QListWidget()
        contador = 1  # variable para contar el número de fila
        for fila in range(self.tabla.rowCount()):
            nombre = self.tabla.item(fila, 0).text()
            apellido = self.tabla.item(fila, 1).text()
            edad = self.tabla.item(fila, 2).text()
            documento = self.tabla.item(fila, 3).text()
            grupo = self.tabla.item(fila, 4).text()
            # Agregar el número de fila al inicio del texto
            texto = f"{contador}.  {nombre} {apellido} - Edad: {edad} - Documento: {documento} - Grupo: {grupo}"
            item = QListWidgetItem(texto)
            lista.addItem(item)
            contador += 1

        # Agregar el botón de guardar lista
        boton_guardar = QPushButton("Guardar lista")
        boton_guardar.setStyleSheet("background-color: #00E420; color: #1E1E1E; padding: 5px;")
        boton_guardar.clicked.connect(self.guardar_lista)

        # Crear un atributo de instancia para la lista
        self.lista = lista

        layout = QVBoxLayout()
        layout.addWidget(self.lista)
        layout.addWidget(boton_guardar)

        # Agregar la lista y el botón a la nueva ventana
        self.lista_window.setLayout(layout)

        # Mostrar la nueva ventana
        self.lista_window.show()

    def guardar_lista(self):
        # Obtener el texto de todos los items de la lista
        texto = []
        for fila in range(self.lista.count()):
            item = self.lista.item(fila)
            texto.append(item.text())

        # Abrir un archivo para guardar la lista
        nombre_archivo, _ = QFileDialog.getSaveFileName(self.lista_window, "Guardar lista", "", "Text Files (*.txt)")

        # Escribir el texto de la lista en el archivo
        if nombre_archivo:
            with open(nombre_archivo, "w") as archivo:
                archivo.write("\n".join(texto))


if __name__ == '__main__':
    # Creamos la aplicación
    app = QApplication(sys.argv)

    # Creamos la ventana y la mostramos
    generador = GeneradorListas()
    generador.show()

    # Ejecutamos la aplicación
    sys.exit(app.exec_())



