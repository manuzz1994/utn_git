# Práctico PyQt5: Construcción guiada de una interfaz completa
# ------------------------------------------------------------
#
# Objetivo: Construir paso a paso un formulario de registro moderno y funcional.
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y primer campo
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 400x300, título “Registro de Usuario”.
# - QLabel grande y centrado: “Formulario de Registro”.
# - QLabel “Nombre:” y QLineEdit al lado, usando QGridLayout.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QRadioButton, QButtonGroup, QHBoxLayout, QComboBox, QCheckBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        
        
        layout_principal = QVBoxLayout()
        self.setLayout(layout_principal)

       # COMPLETAR: Crear QLabel grande y centrado ("Formulario de Registro")
        titulo = QLabel("Formulario de Registro")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout_principal.addWidget(titulo)  
        
        #QSpacerItem crea un "espacio flexible", es un espaciador que fija el título arriba de la ventana.
        layout_principal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        #Grid Layout
        grid = QGridLayout()
         
        

        # COMPLETAR: Crear QLabel "Nombre:" y QLineEdit al lado
        nombre_label = QLabel("Nombre:")
        self.input = QLineEdit()

        grid.addWidget(nombre_label, 0, 1)
        grid.addWidget(self.input, 0, 2)

        layout_principal.addLayout(grid)

        # El segundo QSpacerItem o espaciador “rellena” el espacio sobrante al final para que todo se vea equilibrado. 
        layout_principal.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))


# -----------------------------------------------------------------------------
# Ejercicio 2: Más campos de texto
# -----------------------------------------------------------------------------
# Teoría:
# - QLineEdit puede usarse para email y contraseña.
# - setEchoMode(QLineEdit.Password) oculta el texto del input.
#
# Consigna:
# - Agregar debajo los campos “Email:” y “Contraseña:” (QLabel + QLineEdit).
# - El campo contraseña debe ocultar el texto.
        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        grid.addWidget(email_label, 1, 1)
        grid.addWidget(self.email_input, 1, 2)

        password_label = QLabel("Contraseña:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password) #Oculta contrasena
        grid.addWidget(password_label, 2, 1)
        grid.addWidget(self.password_input, 2, 2)

# -----------------------------------------------------------------------------
# Ejercicio 3: Selección de género
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción.
# - QButtonGroup agrupa los radio buttons para que solo uno esté activo.
#
# Consigna:
# - Agregar dos QRadioButton: “Masculino” y “Femenino”, en la misma fila.
# - Usar QButtonGroup para agruparlos.

        genero_label = QLabel("Género:")
        self.masc_radio = QRadioButton("Masculino")
        self.fem_radio = QRadioButton("Femenino")

        genero_group = QButtonGroup(self)
        genero_group.addButton(self.masc_radio)
        genero_group.addButton(self.fem_radio)

        #esta línea crea un box layout horizontal en que el que se agrupan los botones y quedan mas juntos entre sí.
        genero_layout = QHBoxLayout() 
        genero_layout.addWidget(self.masc_radio)
        genero_layout.addWidget(self.fem_radio)

        grid.addWidget(genero_label, 3, 1)
        grid.addLayout(genero_layout, 3, 2)

# -----------------------------------------------------------------------------
# Ejercicio 4: Selección de país
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
#
# Consigna:
# - Agregar QLabel “País:” y QComboBox con al menos 5 países.

        pais_label = QLabel("País:")
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina", "Brasil", "Uruguay", "Paraguay","Otros"])
        grid.addWidget(pais_label, 4, 1)
        grid.addWidget(self.pais_combo, 4, 2)


# -----------------------------------------------------------------------------
# Ejercicio 5: Checkbox de términos
# -----------------------------------------------------------------------------
# Teoría:
# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.
        self.terminos_checkbox = QCheckBox("Acepto los términos y condiciones")
        grid.addWidget(self.terminos_checkbox, 5, 1, 1, 2)

# -----------------------------------------------------------------------------
# Ejercicio 6: Botón de envío y validación
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Registrarse”.
# - Al hacer clic, validar que todos los campos estén completos y el checkbox marcado.
# - Mostrar mensaje de éxito o error.
        self.registrarse_button = QPushButton("Registrarse")
        self.registrarse_button.clicked.connect(self.validar_formulario)
        layout_principal.addWidget(self.registrarse_button)
    def validar_formulario(self):
        nombre = self.input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        genero = "Masculino" if self.masc_radio.isChecked() else "Femenino" if self.fem_radio.isChecked() else ""
        pais = self.pais_combo.currentText()
        terminos_aceptados = self.terminos_checkbox.isChecked()

        if not nombre or not email or not password or not genero or not pais or not terminos_aceptados:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos y acepte los términos.")
        else:
            QMessageBox.information(self, "Éxito", "¡Registro completado con éxito!")

# -----------------------------------------------------------------------------
# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox, QCheckBox, QRadioButton {
                font-size: 13px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
