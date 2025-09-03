import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QMenuBar, 
                             QAction, QFileDialog, QMessageBox, QStatusBar,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

'''
Aclaraciones:
- El código está dividido en secciones según los ejercicios.
- No se utiliza el metodo QMenuBar() para crear la barra de menús ya que QMainWindow ya lo tiene incorporado.
- Se agregó el método closeEvent para preguntar si se desean guardar los cambios antes de salir.
'''

class EditorTexto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Texto")
        self.setGeometry(100, 100, 800, 600)
        
    # COMPLETAR: Crear QTextEdit y establecerlo como widget central
    def VentanaPrincipal(self):
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.setPlaceholderText("Escribe aquí tu texto...")
    
    # Crear la barra de menús
    def crear_menus(self):
        menuBar = self.menuBar()
        #Archivo(Nuevo, Abrir, Guardar, Salir)
        menuArchivo = menuBar.addMenu('&Archivo')
        #Nuevo
        accionNuevo = QAction('&Nuevo', self)
        accionNuevo.setShortcut(QKeySequence.New)
        accionNuevo.triggered.connect(self.nuevo_archivo)
        menuArchivo.addAction(accionNuevo)
        #Abrir
        accionAbrir = QAction('&Abrir', self)
        accionAbrir.setShortcut(QKeySequence.Open)
        accionAbrir.triggered.connect(self.abrir_archivo)
        menuArchivo.addAction(accionAbrir)
        #Guardar
        accionGuardar = QAction('&Guardar', self)
        accionGuardar.setShortcut(QKeySequence.Save)
        accionGuardar.triggered.connect(self.guardar_archivo)
        menuArchivo.addAction(accionGuardar)
        #Salir
        accionSalir = QAction('&Salir', self)
        accionSalir.setShortcut(QKeySequence.Quit)
        accionSalir.triggered.connect(self.close)
        menuArchivo.addAction(accionSalir)
        
        #Editar(Cortar, Copiar, Pegar)
        menuEditar = menuBar.addMenu('&Editar')
        #Cortar
        accionCortar = QAction('&Cortar', self)
        accionCortar.setShortcut(QKeySequence.Cut)
        accionCortar.triggered.connect(self.editor.cut)
        menuEditar.addAction(accionCortar)
        #Copiar
        accionCopiar = QAction('&Copiar', self)
        accionCopiar.setShortcut(QKeySequence.Copy)
        accionCopiar.triggered.connect(self.editor.copy)
        menuEditar.addAction(accionCopiar)
        #Pegar
        accionPegar = QAction('&Pegar', self)
        accionPegar.setShortcut(QKeySequence.Paste)
        accionPegar.triggered.connect(self.editor.paste)
        menuEditar.addAction(accionPegar)
        
        #Ayuda(Acerca de)
        menuAyuda = menuBar.addMenu('&Ayuda')
        accionAcerca = QAction('Acerca de', self)
        accionAcerca.triggered.connect(self.acercaDe)
        menuAyuda.addAction(accionAcerca)
        
# Ejercicio 3: Implementar funciones de archivo
    def nuevo_archivo(self):
        
        self.editor.clear() #Limpiar el contenido del editor
        self.crear_barra_estado()
    
    def abrir_archivo(self):
        # Usar QFileDialog para seleccionar y abrir un archivo
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)", options=opciones)
        if nombre_archivo:
            try:
                with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                    contenido = archivo.read()
                    self.editor.setText(contenido)
                    self.crear_barra_estado()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo:\n{e}")
                self.crear_barra_estado()
    
    def guardar_archivo(self):
        # Usar QFileDialog para seleccionar ubicación y guardar el archivo
        opciones = QFileDialog.Options()
        nombre_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)", options=opciones)
        if nombre_archivo:
            try:
                with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                    contenido = self.editor.toPlainText()
                    archivo.write(contenido)
                    self.crear_barra_estado()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{e}") 
                self.crear_barra_estado()       
        
# Ejercicio 4: Agregar diálogos informativos
    def acercaDe(self):
        QMessageBox.information(self, "Acerca de", "Editor de Texto\nVersión 1.0\nDesarrollado con PyQt5")
        
    
    
#Modificar salir para preguntar si desea guardar cambios
    def closeEvent(self, event):
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Desea guardar los cambios antes de salir?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
        )
        if respuesta == QMessageBox.Yes:
            self.guardar_archivo()
            event.accept()
        elif respuesta == QMessageBox.No:
            event.accept()
        else:
            event.ignore()

#Barra de estado
    def crear_barra_estado(self):
        self.statusBar().showMessage('Listo', 4000)  # Mensaje que desaparece después de 4 segundos





if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorTexto()
    editor.VentanaPrincipal()
    # COMPLETAR: Llamar métodos de configuración
    editor.crear_menus()
    editor.crear_barra_estado()
    editor.show()
    sys.exit(app.exec_())    