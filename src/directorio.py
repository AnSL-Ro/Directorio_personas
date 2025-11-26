import csv
import os


CARPETA_SRC = os.path.dirname(os.path.abspath(__file__))
CARPETA_PROYECTO = os.path.dirname(CARPETA_SRC)
RUTA_ARCHIVO = os.path.join(CARPETA_PROYECTO, 'data', 'personas.csv')

def inicializar_archivo():
    """Crea la carpeta y el archivo con cabeceras si no existen"""
   
    if not os.path.exists(os.path.dirname(RUTA_ARCHIVO)):
        os.makedirs(os.path.dirname(RUTA_ARCHIVO))
    
    
    if not os.path.exists(RUTA_ARCHIVO):
        with open(RUTA_ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Nombre", "Numero"])

def guardar_contacto(nombre, numero):
    """Recibe los datos y los escribe en el CSV"""
    inicializar_archivo() 
    
    with open(RUTA_ARCHIVO, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, numero])
        print(f"Se guardó en: {RUTA_ARCHIVO}") 

        
        