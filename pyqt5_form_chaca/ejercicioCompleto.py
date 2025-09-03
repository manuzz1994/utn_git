# Práctico PyQt5: Uso de múltiples ventanas (Herramientas y Contexto)
# -------------------------------------------------------------------
#
# Objetivo: Aprender a crear y manejar dos ventanas simultáneas en PyQt5.
# Una ventana será de herramientas (con botones como Guardar, Abrir, Buscar, etc.)
# y la otra mostrará el contexto: un formulario de afiliados al Club Atlético Chacarita Juniors.
#
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5, QGridLayout y manejo de ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Crear la ventana de contexto (formulario de afiliados)
# -----------------------------------------------------------------------------
# Teoría:
# - QWidget es la base para crear ventanas.
# - QGridLayout organiza los widgets en filas y columnas.
# - QLabel y QLineEdit permiten mostrar e ingresar datos.
#
# Consigna:
# - Crear una ventana principal (QWidget) de 500x350, título "Afiliados - Chacarita Juniors".
# - Agregar QLabel grande y centrado: "Formulario de Afiliación".
# - Agregar QLabel y QLineEdit para Nombre, Apellido, DNI y Fecha de nacimiento.
#
# -----------------------------------------------------------------------------
# Ejercicio 2: Crear la ventana de herramientas
# -----------------------------------------------------------------------------
# Teoría:
# - Otra instancia de QWidget puede funcionar como ventana secundaria.
# - QPushButton permite crear botones de acción.
# - QVBoxLayout organiza widgets en columna.
#
# Consigna:
# - Crear una ventana secundaria de 200x300, título "Herramientas".
# - Agregar botones: "Guardar", "Abrir", "Buscar", "Salir".
#
# -----------------------------------------------------------------------------
# Ejercicio 3: Mostrar ambas ventanas a la vez
# -----------------------------------------------------------------------------
# Teoría:
# - Puedes crear y mostrar varias ventanas instanciando varias clases QWidget.
# - show() en cada ventana las hace visibles simultáneamente.
#
# Consigna:
# - Modifica el script para que ambas ventanas se muestren al ejecutar el programa.
#
# -----------------------------------------------------------------------------
# Ejercicio 4: Conectar botones de herramientas con el formulario
# -----------------------------------------------------------------------------
# Teoría:
# - Los botones pueden ejecutar funciones que interactúan con la otra ventana.
# - Puedes pasar referencias entre ventanas para manipular datos.
#
# Consigna:
# - Haz que el botón "Guardar" muestre un mensaje con los datos ingresados en el formulario.
# - El botón "Salir" debe cerrar ambas ventanas.
#
# -----------------------------------------------------------------------------
# Ejercicio 5: Personalización visual y validaciones
# -----------------------------------------------------------------------------
# Consigna:
# - Cambia colores, fuentes y tamaño de los widgets para una interfaz moderna.
# - Valida que los campos obligatorios estén completos antes de guardar.
#
# -----------------------------------------------------------------------------
# Sugerencia:
# - Usa QDateEdit para la fecha de nacimiento.
# - Usa QMessageBox para mostrar mensajes.
#
# -----------------------------------------------------------------------------
# Esqueleto inicial:

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QSizePolicy, QDateEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon #Para iconos

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ico_chaca_title.png"))
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)

        # Estilos globales para la ventana principal
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f8fafc, stop:1 #e0e7ef);
                font-family: 'Segoe UI', 'Raleway', Arial, sans-serif;
                font-size: 15px;
            }
            QLabel {
                color: #222;
                background: transparent;
            }
            QLineEdit, QDateEdit {
                border: 1px solid #bfc9d1;
                border-radius: 6px;
                padding: 6px 8px;
                background: #fff;
                font-size: 15px;
            }
            QPushButton {
                background: #6c63ff;
                color: #fff;
                border: none;
                border-radius: 8px;
                padding: 8px 20px;
                font-size: 15px;
                font-weight: 500;
                margin-top: 10px;
            }
            QPushButton:hover {
                background: #5548c8;
            }
        """)

        titulo_layout = QVBoxLayout()
        titulo_form = QLabel("Formulario de afiliación")
        titulo_form.setAlignment(Qt.AlignCenter)
        titulo_form.setStyleSheet("font-size: 24px; font-family: 'Raleway', 'Segoe UI', Arial, sans-serif; font-weight: bold; color: #3a3a3a;")
        titulo_form.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        titulo_layout.addWidget(titulo_form)

        layout_form = QGridLayout()

        nombre_afiliado = QLabel("Nombre:")
        self.input_nombre = QLineEdit()
        layout_form.addWidget(nombre_afiliado, 0, 1)
        layout_form.addWidget(self.input_nombre, 0, 2)

        apellido_afiliado = QLabel("Apellido")
        self.input_apellido = QLineEdit()
        layout_form.addWidget(apellido_afiliado, 1, 1)
        layout_form.addWidget(self.input_apellido, 1, 2)

        dni_afiliado = QLabel("N° Documento:")
        self.input_dni = QLineEdit()
        layout_form.addWidget(dni_afiliado, 2, 1)
        layout_form.addWidget(self.input_dni, 2, 2)

        fec_nacim_afiliado = QLabel("Fecha de Nacimiento:")
        self.input_fec = QDateEdit()
        self.input_fec.setCalendarPopup(True)
        layout_form.addWidget(fec_nacim_afiliado, 3, 1)
        layout_form.addWidget(self.input_fec, 3, 2)

        titulo_layout.addLayout(layout_form)
        self.setLayout(titulo_layout)

        boton_abrir_herr = QPushButton("Abrir Herramientas")
        boton_abrir_herr.clicked.connect(self.abrir_herramientas)
        titulo_layout.addWidget(boton_abrir_herr)

    # Función para abrir la ventana de herramientas    
    def abrir_herramientas(self):
        self.ventana_herramientas = VentanaHerramientas(self)
        self.ventana_herramientas.show()
        
# ------- Ventana de herramientas -------
class VentanaHerramientas(QWidget):
    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal  # Referencia a la ventana principal
        self.setWindowIcon(QIcon("ico_chaca_title.png"))
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 220, 200)

        # Estilos para la ventana de herramientas
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f3f6fb, stop:1 #e0e7ef);
                font-family: 'Segoe UI', 'Raleway', Arial, sans-serif;
            }
            QPushButton {
                background: #6c63ff;
                color: #fff;
                border: none;
                border-radius: 8px;
                padding: 8px 20px;
                font-size: 15px;
                font-weight: 500;
                margin-top: 10px;
                transition: background 0.2s;
            }
            QPushButton:hover {
                background: #5548c8;
            }
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        boton_guardar = QPushButton("Guardar")
        layout.addWidget(boton_guardar)

        boton_salir = QPushButton("Salir")
        layout.addWidget(boton_salir)

        boton_guardar.clicked.connect(self.guardar_datos)
        boton_salir.clicked.connect(self.salir_aplicacion)

        self.datos_guardados = []
        
    def guardar_datos(self):
        # Obtener widgets del formulario de la ventana principal
        nombre = self.ventana_principal.findChild(QLineEdit, None)
        apellido = self.ventana_principal.findChild(QLineEdit, None)
        dni = self.ventana_principal.findChild(QLineEdit, None)
        fecha_nac = self.ventana_principal.findChild(QDateEdit, None)

        # Si tienes referencias directas, usa self.ventana_principal.input_nombre, etc.
        # Aquí se asume que los widgets están accesibles como atributos:
        try:
            nombre = self.ventana_principal.input_nombre.text()
            apellido = self.ventana_principal.input_apellido.text()
            dni = self.ventana_principal.input_dni.text()
            fecha_nac = self.ventana_principal.input_fec.date().toString("dd/MM/yyyy")
        except AttributeError:
            # Si no existen como atributos, buscar por orden de aparición
            lineedits = self.ventana_principal.findChildren(QLineEdit)
            nombre = lineedits[0].text() if len(lineedits) > 0 else ""
            apellido = lineedits[1].text() if len(lineedits) > 1 else ""
            dni = lineedits[2].text() if len(lineedits) > 2 else ""
            fecha_nac = self.ventana_principal.findChild(QDateEdit).date().toString("dd/MM/yyyy")

        if not nombre or not apellido or not dni or not fecha_nac:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, complete todos los campos antes de guardar.")
            return

        datos_afiliado = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de Nacimiento": fecha_nac
        }
        self.datos_guardados.append(datos_afiliado)

        # Mostrar los datos en un QMessageBox
        mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha de Nacimiento: {fecha_nac}"
        QMessageBox.information(self, "Datos guardados", mensaje)

        # Guardar los datos en un archivo afiliados.txt dentro de la carpeta 'datos'

        os.makedirs("datos", exist_ok=True)
        ruta_archivo = os.path.join("datos", "afiliados.txt")
        with open(ruta_archivo, "a", encoding="utf-8") as f:
            f.write(f"Nombre: {nombre}, Apellido: {apellido}, DNI: {dni}, Fecha de Nacimiento: {fecha_nac}\n")
        

    
    def salir_aplicacion(self):
        # Cerrar ambas ventanas
        self.close()
        self.ventana_principal.close()

        
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_principal = VentanaFormulario()
    ventana_herramientas = VentanaHerramientas(ventana_principal)
    ventana_principal.show()
    ventana_herramientas.show()
    sys.exit(app.exec_())
