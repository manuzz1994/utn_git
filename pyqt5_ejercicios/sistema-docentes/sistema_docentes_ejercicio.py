# Práctico PyQt5: Sistema de Gestión de Docentes con Archivo TXT
# ----------------------------------------------------------
#
# Objetivo: Crear un sistema completo para gestionar información de docentes
# que permita agregar, visualizar, buscar, modificar y eliminar registros
# guardándolos en un archivo de texto para persistencia de datos.
#
# Este ejercicio integra todos los conceptos aprendidos y agrega manipulación de archivos.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y formulario de datos
# -----------------------------------------------------------------------------
# Teoría:
# - Persistencia de datos: guardar información para que no se pierda al cerrar la app.
# - Archivos de texto: formato simple para almacenar datos estructurados.
# - Separadores: usar caracteres especiales (|, ;, tabs) para dividir campos.
#
# Consigna:
# - Crear QMainWindow de 800x600, título "Sistema de Gestión de Docentes".
# - Formulario con campos: Legajo, Nombre, Apellido, DNI, Email, Teléfono, Materia, Categoría.
# - Botones: Agregar, Buscar, Modificar, Eliminar, Limpiar.

import sys
import os
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
                             QPushButton, QTextEdit, QComboBox, QMessageBox,
                             QFileDialog, QGroupBox, QListWidget, QSplitter, QListWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class SistemaDocentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión de Docentes")
        self.setGeometry(100, 100, 1000, 700)
        
        # Archivo donde se guardarán los datos
        self.archivo_datos = "docentes.txt"
        
        # Configurar interfaz
        self.configurar_interfaz()
        # Cargar datos existentes
        self.cargar_datos()
        
        # Estilo personalizado
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QPushButton:pressed {
                background-color: #004085;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #007bff;
            }
            QListWidget {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
            QTextEdit {
                border: 1px solid #ced4da;
                border-radius: 4px;
                background-color: white;
            }
        """)

    def configurar_interfaz(self):
        """Configurar la interfaz principal"""
        # Widget central con división
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal horizontal
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Crear splitter para dividir la pantalla
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Panel izquierdo: Formulario y botones
        panel_izquierdo = self.crear_panel_formulario()
        splitter.addWidget(panel_izquierdo)
        
        # Panel derecho: Lista y detalles
        panel_derecho = self.crear_panel_lista()
        splitter.addWidget(panel_derecho)
        
        # Configurar proporciones del splitter
        splitter.setSizes([400, 600])

    def crear_panel_formulario(self):
        """Crear el panel con el formulario de datos"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # COMPLETAR: Crear grupo de formulario
        grupo_form = QGroupBox("Datos del Docente")
        form_layout = QGridLayout()
        
        # Crear campos del formulario
        # Repite para: Nombre, Apellido, DNI, Email, Teléfono, Materia

        # Legajo
        self.legajo_edit = QLineEdit()
        self.legajo_edit.setPlaceholderText("Ej: DOC001")
        form_layout.addWidget(QLabel("Legajo:"), 0, 0)
        form_layout.addWidget(self.legajo_edit, 0, 1)
        # Nombre
        self.nombre_edit = QLineEdit()
        self.nombre_edit.setPlaceholderText("Ej: Marcelo Daniel")
        form_layout.addWidget(QLabel("Nombre:"), 1, 0)
        form_layout.addWidget(self.nombre_edit, 1, 1)
        # Apellido
        self.apellido_edit = QLineEdit()
        self.apellido_edit.setPlaceholderText("Ej: Gallardo")
        form_layout.addWidget(QLabel("Apellido:"), 2, 0)
        form_layout.addWidget(self.apellido_edit, 2, 1)
        # DNI
        self.dni_edit = QLineEdit()
        self.dni_edit.setPlaceholderText("Ej: 12345678")
        form_layout.addWidget(QLabel("DNI:"), 3, 0)
        form_layout.addWidget(self.dni_edit, 3, 1)
        # Email
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Ej: mi_email@ejemplo.com")
        form_layout.addWidget(QLabel("Email:"), 4, 0)
        form_layout.addWidget(self.email_edit, 4, 1)
        # Teléfono
        self.telefono_edit = QLineEdit()
        self.telefono_edit.setPlaceholderText("Sin 0 ni 15, Ej: 1123456789")
        form_layout.addWidget(QLabel("Teléfono:"), 5, 0)
        form_layout.addWidget(self.telefono_edit, 5, 1)
        # Materia
        self.materia_edit = QLineEdit()
        self.materia_edit.setPlaceholderText("Ej: Matemática")
        form_layout.addWidget(QLabel("Materia:"), 6, 0)
        form_layout.addWidget(self.materia_edit, 6, 1) 
        
        # Campo Categoría con ComboBox
        self.categoria_combo = QComboBox()
        self.categoria_combo.addItems(["Titular", "Asociado", "Adjunto", "Auxiliar", "Interino"])
        form_layout.addWidget(QLabel("Categoría:"), 7, 0)
        form_layout.addWidget(self.categoria_combo, 7, 1)

        
        grupo_form.setLayout(form_layout)
        layout.addWidget(grupo_form)
        
        # Crear grupo de botones
        grupo_botones = QGroupBox("Acciones")
        botones_layout = QVBoxLayout()

        #BTN Agregar Docente
        self.btn_agregar = QPushButton("Agregar Docente")
        self.btn_agregar.clicked.connect(self.agregar_docente)
        botones_layout.addWidget(self.btn_agregar)
        # Repite para: Buscar, Modificar, Eliminar, Limpiar
        #BTN Buscar Docente
        self.btn_buscar = QPushButton("Buscar Docente")
        self.btn_buscar.clicked.connect(self.buscar_docente)
        botones_layout.addWidget(self.btn_buscar)
        #BTN Modificar Docente
        self.btn_modificar = QPushButton("Modificar Docente")
        self.btn_modificar.clicked.connect(self.modificar_docente)
        botones_layout.addWidget(self.btn_modificar)
        #BTN Eliminar Docente
        self.btn_eliminar = QPushButton("Eliminar Docente")
        self.btn_eliminar.clicked.connect(self.eliminar_docente)
        botones_layout.addWidget(self.btn_eliminar)
        #BTN Limpiar Formulario
        self.btn_limpiar = QPushButton("Limpiar Formulario")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)
        botones_layout.addWidget(self.btn_limpiar)
        #BTN Exportar Datos
        self.btn_exportar = QPushButton("Exportar Datos")
        self.btn_exportar.clicked.connect(self.exportar_datos)
        botones_layout.addWidget(self.btn_exportar)
        #BTN Mostrar Estadísticas
        self.btn_estadisticas = QPushButton("Mostrar Estadísticas")
        self.btn_estadisticas.clicked.connect(self.mostrar_estadisticas)
        botones_layout.addWidget(self.btn_estadisticas)
                
        grupo_botones.setLayout(botones_layout)
        layout.addWidget(grupo_botones)
        
        widget.setLayout(layout)
        return widget

# -----------------------------------------------------------------------------
# Ejercicio 2: Implementar funciones de archivo
# -----------------------------------------------------------------------------
# Teoría:
# - Formato de archivo: cada línea representa un docente.
# - Separador: usar | para dividir los campos.
# - Estructura: legajo|nombre|apellido|dni|email|telefono|materia|categoria
#
# Consigna:
# - Implementar cargar_datos(): leer archivo y mostrar en lista.
# - Implementar guardar_datos(): escribir lista completa al archivo.
# - Implementar agregar_docente(): validar y agregar nuevo registro.

    def cargar_datos(self):
        """Cargar datos desde el archivo"""
        # COMPLETAR: Verificar si existe el archivo
        if not os.path.exists(self.archivo_datos):    
            return
        
        # COMPLETAR: Leer líneas del archivo
        try: # Manejo de errores al leer el archivo
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo: # Abrir archivo en modo lectura
                for linea in archivo: # Leer línea por línea
                    if linea.strip():  # Ignorar líneas vacías
                        datos = linea.strip().split('|') # Dividir por el separador |
                        if len(datos) == 8:  # Verificar que tenga todos los campos
                            self.agregar_a_lista(datos) # Agregar a la lista
        except Exception as e: # Capturar cualquier error
            QMessageBox.critical(self, 'Error', f'Error al cargar datos:\n{e}') 
        
    
    def guardar_datos(self):
        """Guardar todos los datos al archivo"""
        # COMPLETAR: Obtener todos los elementos de la lista
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for i in range(self.lista_docentes.count()):
                    item = self.lista_docentes.item(i)
                    datos = item.data(Qt.UserRole)  # Datos completos guardados en el item
                    linea = '|'.join(datos) + '\n'
                    archivo.write(linea)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error al guardar datos:\n{e}')
        
    
    def agregar_docente(self):
        """Agregar un nuevo docente"""
        # COMPLETAR: Validar campos obligatorios
        valido, mensaje = self.validar_campos_obligatorios() #METODO AUXILIAR QUE SE CREA AL FINAL, evita repetir código
        if not valido:
            QMessageBox.warning(self, 'Error', mensaje)
            return
        
        
        # COMPLETAR: Recopilar datos del formulario
        datos = self.obtener_datos_formulario() #METODO AUXILIAR QUE SE CREA AL FINAL, evita repetir código
        
        # COMPLETAR: Agregar a la lista y guardar
        self.agregar_a_lista(datos)
        self.guardar_datos()
        self.limpiar_formulario()
        QMessageBox.information(self, 'Éxito', 'Docente agregado correctamente')

# -----------------------------------------------------------------------------
# Ejercicio 3: Implementar búsqueda y visualización
# -----------------------------------------------------------------------------
# Teoría:
# - QListWidget para mostrar lista de elementos.
# - Búsqueda: filtrar elementos que contengan el texto buscado.
# - Selección: mostrar detalles del elemento seleccionado.
#
# Consigna:
# - Crear lista que muestre "Apellido, Nombre (Legajo)".
# - Implementar búsqueda por apellido, nombre o legajo.
# - Al seleccionar un item, mostrar todos los datos.

    def crear_panel_lista(self):
        """Crear el panel con la lista y detalles"""
        widget = QWidget() # Contenedor principal
        layout = QVBoxLayout() 
        # COMPLETAR: Crear título
        titulo = QLabel("Lista de Docentes")
        titulo.setFont(QFont('Arial', 16, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        
        # COMPLETAR: Crear área de búsqueda
        busqueda_layout = QHBoxLayout()
        busqueda_layout.addWidget(QLabel("Buscar:"))
        self.busqueda_edit = QLineEdit()
        self.busqueda_edit.setPlaceholderText("Buscar por apellido, nombre o legajo...")
        self.busqueda_edit.textChanged.connect(self.filtrar_lista) # Filtrar al escribir
        busqueda_layout.addWidget(self.busqueda_edit)
        layout.addLayout(busqueda_layout)
        
        # COMPLETAR: Crear lista de docentes
        self.lista_docentes = QListWidget()
        self.lista_docentes.itemClicked.connect(self.mostrar_detalles)
        layout.addWidget(self.lista_docentes)
        
        # COMPLETAR: Crear área de detalles
        grupo_detalles = QGroupBox("Detalles del Docente Seleccionado") #
        self.detalles_text = QTextEdit() # Área de texto para detalles
        self.detalles_text.setReadOnly(True) # Solo lectura
        self.detalles_text.setMaximumHeight(200) # Altura máxima
        detalles_layout = QVBoxLayout() # Layout vertical
        detalles_layout.addWidget(self.detalles_text) # Agregar área de texto al layout 
        grupo_detalles.setLayout(detalles_layout) # Asignar layout al grupo
        layout.addWidget(grupo_detalles) # Agregar grupo al layout principal
        
        widget.setLayout(layout) # Asignar layout al widget 
        return widget
    
    def agregar_a_lista(self, datos): 
        """Agregar un docente a la lista"""
        # COMPLETAR: Crear texto para mostrar en la lista
        texto_item = f"{datos[2]}, {datos[1]} ({datos[0]})"  # Apellido, Nombre (Legajo)
        item = QListWidgetItem(texto_item) # Crear item de lista
        item.setData(Qt.UserRole, datos)  # Guardar datos completos, UserRole es un rol personalizado para guardar datos adicionales
        self.lista_docentes.addItem(item) # Agregar item a la lista
    
    def filtrar_lista(self):
        """Filtrar la lista según el texto de búsqueda"""
        # COMPLETAR: Obtener texto de búsqueda
        texto_busqueda = self.busqueda_edit.text().lower()
        
        # COMPLETAR: Mostrar/ocultar items según coincidencia
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            # Buscar en legajo, nombre y apellido
            coincide = (texto_busqueda in datos[0].lower() or  # legajo
                       texto_busqueda in datos[1].lower() or   # nombre
                       texto_busqueda in datos[2].lower())     # apellido
            item.setHidden(not coincide)

    def buscar_por_legajo(self, legajo):
        """Buscar un docente por legajo"""
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                return item
        return None
    def buscar_por_nombre_apellido(self, texto):
        """Buscar un docente por nombre o apellido"""
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if (texto.lower() in datos[1].lower()) or (texto.lower() in datos[2].lower()):
                return item
        return None
    
    def mostrar_detalles(self, item):
        """Mostrar detalles del docente seleccionado"""
        # COMPLETAR: Obtener datos del item seleccionado
        datos = item.data(Qt.UserRole)
        detalles = f"""
        INFORMACIÓN DEL DOCENTE
        ========================
        Legajo: {datos[0]}
        Nombre: {datos[1]}
        Apellido: {datos[2]}
        DNI: {datos[3]}
        Email: {datos[4]}
        Teléfono: {datos[5]}
        Materia: {datos[6]}
        Categoría: {datos[7]}
        """
        self.detalles_text.setPlainText(detalles)

# -----------------------------------------------------------------------------
# Ejercicio 4: Implementar modificación y eliminación
# -----------------------------------------------------------------------------
# Teoría:
# - Modificar: cargar datos en formulario, permitir edición, actualizar archivo.
# - Eliminar: confirmar acción, quitar de lista, actualizar archivo.
#
# Consigna:
# - Botón "Modificar": cargar datos del seleccionado en formulario.
# - Botón "Eliminar": pedir confirmación y eliminar registro.
# - Actualizar archivo después de cada cambio.

    def buscar_docente(self):
        """Buscar docente por legajo"""
        # COMPLETAR: Pedir legajo a buscar
        legajo = self.legajo_edit.text().strip()
        if not legajo:
            QMessageBox.warning(self, 'Error', 'Ingrese un legajo para buscar')
            return
        
        # COMPLETAR: Buscar en la lista y seleccionar
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            if datos[0].lower() == legajo.lower():
                self.lista_docentes.setCurrentItem(item)
                self.mostrar_detalles(item)
                return
        
        QMessageBox.information(self, 'No encontrado', f'No se encontró docente con legajo: {legajo}')

    
    def modificar_docente(self):
        """Modificar el docente seleccionado"""
        # COMPLETAR: Verificar que hay un elemento seleccionado
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para modificar')
            return
        
        # COMPLETAR: Cargar datos en el formulario
        # ... cargar todos los campos
        datos = item_actual.data(Qt.UserRole)
        self.legajo_edit.setText(datos[0])
        self.nombre_edit.setText(datos[1])
        self.apellido_edit.setText(datos[2])
        self.dni_edit.setText(datos[3])
        self.email_edit.setText(datos[4])
        self.telefono_edit.setText(datos[5])
        self.materia_edit.setText(datos[6])
        categoria_index = self.categoria_combo.findText(datos[7])
        if categoria_index != -1:
            self.categoria_combo.setCurrentIndex(categoria_index)       
        
        
        # COMPLETAR: Cambiar botón "Agregar" por "Actualizar"
        self.btn_agregar.setText("Actualizar Docente") # Cambiar texto del botón
        self.btn_agregar.clicked.disconnect() # Desconectar función anterior 
        self.btn_agregar.clicked.connect(lambda: self.actualizar_docente(item_actual)) # Conectar nueva función con el item actual
    
    def actualizar_docente(self, item):
        """Actualizar los datos del docente"""
        # COMPLETAR: Validar y obtener nuevos datos
        # COMPLETAR: Actualizar el item en la lista
        # COMPLETAR: Guardar cambios y restaurar botón "Agregar"
        valido, mensaje = self.validar_campos_obligatorios()
        if not valido:
            QMessageBox.warning(self, 'Error', mensaje)
            return
        
        # Obtener datos del formulario      
        datos = self.obtener_datos_formulario() #METODO AUXILIAR QUE SE CREA AL FINAL, evita repetir código

        texto_item = f"{datos[2]}, {datos[1]} ({datos[0]})"
        item.setText(texto_item)
        item.setData(Qt.UserRole, datos)

        

        self.guardar_datos()
        self.limpiar_formulario()
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)
        QMessageBox.information(self, 'Éxito', 'Docente modificado correctamente')
    
    def eliminar_docente(self):
        """Eliminar el docente seleccionado"""
        # COMPLETAR: Verificar selección
        item_actual = self.lista_docentes.currentItem()
        if not item_actual:
            QMessageBox.warning(self, 'Error', 'Seleccione un docente para eliminar')
            return
        
        # COMPLETAR: Pedir confirmación
        datos = item_actual.data(Qt.UserRole)
        respuesta = QMessageBox.question(self, 'Confirmar eliminación',
                                       f'¿Está seguro de eliminar a {datos[1]} {datos[2]}?',
                                       QMessageBox.Yes | QMessageBox.No)
        
        if respuesta == QMessageBox.Yes:
            # COMPLETAR: Eliminar de la lista y guardar
            row = self.lista_docentes.row(item_actual)
            self.lista_docentes.takeItem(row)
            self.guardar_datos()
            QMessageBox.information(self, 'Éxito', 'Docente eliminado correctamente')

    def limpiar_formulario(self):
        """Limpiar todos los campos del formulario"""
        # COMPLETAR: Limpiar todos los campos
        self.legajo_edit.clear()
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.email_edit.clear()
        self.telefono_edit.clear()
        self.materia_edit.clear()
        # ... limpiar todos los campos
        self.categoria_combo.setCurrentIndex(0)
        self.detalles_text.clear()
        self.lista_docentes.clearSelection()
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)

# -----------------------------------------------------------------------------
# Ejercicio 5: Funciones adicionales
# -----------------------------------------------------------------------------
# Consigna:
# - Implementar exportar datos a otro archivo.
# - Agregar validación de email y teléfono.
# - Crear estadísticas (cantidad por categoría).

    def exportar_datos(self):
        """Exportar datos a un archivo CSV"""
        # COMPLETAR: Pedir nombre de archivo
        archivo, _ = QFileDialog.getSaveFileName(self, 'Exportar datos', 
                                               'docentes_export.csv', 
                                               'Archivos CSV (*.csv)')
        if archivo:
            # COMPLETAR: Escribir datos en formato CSV
            try:
                with open(archivo, 'w', encoding='utf-8') as f:
                    f.write("Legajo,Nombre,Apellido,DNI,Email,Teléfono,Materia,Categoría\n")
                    for i in range(self.lista_docentes.count()):
                        item = self.lista_docentes.item(i)
                        datos = item.data(Qt.UserRole)
                        linea = ','.join(datos) + '\n'
                        f.write(linea)
                QMessageBox.information(self, 'Éxito', f'Datos exportados a {archivo}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error al exportar datos:\n{e}')
        # Exportar datos a CSV

    def mostrar_estadisticas(self):
        """Mostrar estadísticas de docentes por categoría"""
        categorias = {}
        for i in range(self.lista_docentes.count()):
            item = self.lista_docentes.item(i)
            datos = item.data(Qt.UserRole)
            categoria = datos[7]
            if categoria in categorias:
                categorias[categoria] += 1
            else:
                categorias[categoria] = 1
        
        estadisticas = "ESTADÍSTICAS DE DOCENTES POR CATEGORÍA\n===============================\n"
        for cat, count in categorias.items():
            estadisticas += f"{cat}: {count}\n"
        
        QMessageBox.information(self, 'Estadísticas', estadisticas)

#VALIDACIONES Y MÉTODOS AUXILIARES ====================================================
    def validar_email(self, email):
        """Validar formato de email"""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    def validar_telefono(self, telefono):
        """Validar formato de teléfono (solo dígitos, 7-15 caracteres)"""
        patron = r'^\d{7,15}$'
        return re.match(patron, telefono) is not None
    def validar_campos_obligatorios(self):
        """Validar que los campos obligatorios no estén vacíos"""
        if not self.legajo_edit.text().strip():
            return False, 'El legajo es obligatorio'
        if not self.nombre_edit.text().strip():
            return False, 'El nombre es obligatorio'
        if not self.apellido_edit.text().strip():
            return False, 'El apellido es obligatorio'
        if not self.dni_edit.text().strip():
            return False, 'El DNI es obligatorio'
        if not self.email_edit.text().strip():
            return False, 'El email es obligatorio'
        if not self.telefono_edit.text().strip():
            return False, 'El teléfono es obligatorio'
        if not self.materia_edit.text().strip():
            return False, 'La materia es obligatoria'
        return True, ''
        if not self.validar_email(self.email_edit.text().strip()):
            return False, 'El formato del email es inválido'
        if not self.validar_telefono(self.telefono_edit.text().strip()):
            return False, 'El formato del teléfono es inválido'
        return True, ''

    def obtener_datos_formulario(self):
        """Obtener datos del formulario"""
        datos = [
            self.legajo_edit.text().strip(),
            self.nombre_edit.text().strip(),
            self.apellido_edit.text().strip(),
            self.dni_edit.text().strip(),
            self.email_edit.text().strip(),
            self.telefono_edit.text().strip(),
            self.materia_edit.text().strip(),
            self.categoria_combo.currentText()
        ]
        return datos

    def restaurar_boton_agregar(self):
        """Restaurar el botón Agregar"""
        self.btn_agregar.setText("Agregar Docente")
        self.btn_agregar.clicked.disconnect()
        self.btn_agregar.clicked.connect(self.agregar_docente)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sistema = SistemaDocentes()
    sistema.show()
    sys.exit(app.exec_())

# -----------------------------------------------------------------------------
# Estructura del archivo docentes.txt:
# -----------------------------------------------------------------------------
# Cada línea representa un docente con el formato:
# legajo|nombre|apellido|dni|email|telefono|materia|categoria
#
# Ejemplo:
# DOC001|Juan|Pérez|12345678|juan.perez@universidad.edu|123456789|Matemática|Titular
# DOC002|María|González|87654321|maria.gonzalez@universidad.edu|987654321|Física|Adjunto
# DOC003|Carlos|Rodríguez|11223344|carlos.rodriguez@universidad.edu|456789123|Química|Asociado
