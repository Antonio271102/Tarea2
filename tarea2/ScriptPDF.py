import fitz  # PyMuPDF

def leer_metadatos_pdf(nombre_archivo):
    try:
        documento = fitz.open(nombre_archivo)
        metadatos = documento.metadata
        print("Metadatos del PDF:")
        for clave, valor in metadatos.items():
            print(f"{clave}: {valor}")
    except Exception as e:
        print(f"Error al leer el archivo PDF: {e}")

# Nombre del archivo PDF
nombre_archivo = "C:\\Users\\Anton\\OneDrive\\Escritorio\\tarea2\\documento.pdf"

# Llamada a la función para leer los metadatos del PDF
leer_metadatos_pdf(nombre_archivo)