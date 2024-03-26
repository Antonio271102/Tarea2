from openpyxl import load_workbook
import os

# Obtener la ruta del archivo Excel 
archivo_excel = "C:\\Users\\Anton\\OneDrive\\Escritorio\\tarea2\\archivo.xlsx"
ruta_completa = os.path.join(os.getcwd(), archivo_excel)

# Cargar el libro de trabajo (workbook) de Excel
libro_trabajo = load_workbook(ruta_completa)

# Obtener los metadatos del documento de Excel
metadatos = libro_trabajo.properties

# Imprimir los metadatos en consola
print("Metadatos del documento Excel:")
print("Título:", metadatos.title)
print("Autor:", getattr(metadatos, 'author', 'No disponible'))
print("Empresa:", getattr(metadatos, 'company', 'No disponible'))
print("Última vez guardado por:", getattr(metadatos, 'lastModifiedBy', 'No disponible'))
print("Fecha de creación:", getattr(metadatos, 'created', 'No disponible'))
print("Fecha de última modificación:", getattr(metadatos, 'modified', 'No disponible'))