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
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        titulo_layout = QVBoxLayout() #Layout principal de la ventana y título
        # COMPLETAR: agregar widgets para el formulario
        titulo_form = QLabel("Formulario de afiliación")
        titulo_form.setAlignment(Qt.AlignCenter)
        titulo_form.setStyleSheet("font-size: 20px; font-weight: bold;")
        titulo_form.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        titulo_layout.addWidget(titulo_form)
        
        layout_form = QGridLayout() #Layout para formulario.
        
        nombre_afiliado = QLabel("Nombre:")
        input_nombre = QLineEdit()
        layout_form.addWidget(nombre_afiliado, 0, 1)
        layout_form.addWidget(input_nombre, 0, 2)
        
        apellido_afiliado = QLabel("Apellido")
        input_apellido = QLineEdit()
        layout_form.addWidget(apellido_afiliado, 1, 1)
        layout_form.addWidget(input_apellido, 1, 2)
        
        dni_afiliado = QLabel("N° Documento:")
        input_dni = QLineEdit()
        layout_form.addWidget(dni_afiliado, 2, 1)
        layout_form.addWidget(input_dni, 2, 2)
        
        
        fec_nacim_afiliado = QLabel("Fecha de Nacimiento:")
        input_fec = QLineEdit()
        layout_form.addWidget(fec_nacim_afiliado, 3, 1)
        layout_form.addWidget(input_fec, 3, 2)
        
        
        titulo_layout.addLayout(layout_form)
        self.setLayout(titulo_layout)
        
        #Boton para abrir ventana herramientas
        boton_abrir_herr = QPushButton("Abrir Herramientas")
        boton_abrir_herr.clicked.connect(self.abrir_herramientas)
        titulo_layout.addWidget(boton_abrir_herr)
        
    def abrir_herramientas(self):
        self.ventana_herramientas = VentanaHerramientas()
        self.ventana_herramientas.show()
        

class VentanaHerramientas(QWidget):
    def __init__(self):
        super().__init__()
        self.ventana_principal = ventana_principal  # Referencia a la ventana principal
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Botones: "Guardar", "Salir".
        boton_guardar = QPushButton("Guardar")
        layout.addWidget(boton_guardar)
        
        boton_salir = QPushButton("Salir")
        layout.addWidget(boton_salir)
        
        # - Haz que el botón "Guardar" muestre un mensaje con los datos ingresados en el formulario.
        # - El botón "Salir" debe cerrar ambas ventanas.
        boton_guardar.clicked.connect(self.guardar_datos)
        boton_salir.clicked.connect(self.salir_aplicacion)
        
        self.datos_guardados = []
        
    def guardar_datos(self):
        # Logica para obtener datos de la ventana principal
        nombre = self.ventana_principal.findChild(QLineEdit, "").text()
        apellido = self.ventana_principal.findChild(QLineEdit, "").text()
        dni = self.ventana_principal.findChild(QLineEdit, "").text()
        fecha_nac = self.ventana_principal.findChild(QLineEdit, "").text()
        
        if not nombre or not apellido or not dni or not fecha_nac:
            print("Por favor, complete todos los campos antes de guardar.")
            return
        
        # Guardar los datos en una lista o estructura
        datos_afiliado = {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de Nacimiento": fecha_nac
        }
        # Mostrar datos por consola
        self.datos_guardados.append(datos_afiliado)
        print("Datos guardados:", datos_afiliado)
        

    
    def salir_aplicacion(self):
        # Cerrar ambas ventanas
        self.close()
        self.ventana_principal.close()

        
        
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_principal = VentanaFormulario()
    ventana_form = VentanaHerramientas()
    ventana_principal.show()
    ventana_form.show()
    
    sys.exit(app.exec_())
