import time
import pyautogui
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Opciones para el ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-chrome-browser-cloud-management")
chrome_options.add_argument("--start-maximized")  # Iniciar maximizado

# Inicializar el servicio del ChromeDriver
chromedriver_path = "C:/Users/Admin/Desktop/Code/formWorker/chromedriver.exe"  # Especifica la ruta al chromedriver.exe
service = Service(chromedriver_path)

# Inicializar el controlador del navegador
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abrir la página web
    driver.get("https://rpachallenge.com/")

    # Enfocar la ventana del navegador
    driver.switch_to.window(driver.current_window_handle)

    # Simular la combinación de teclas Ctrl + P para abrir la ventana de impresión
    pyautogui.hotkey('ctrl', 'p')

    # Esperar unos segundos para que se abra la ventana de impresión
    time.sleep(3)  # Puedes ajustar el tiempo según necesites

    # Simular la tecla Enter para confirmar la impresión
    pyautogui.press('enter')

    # Esperar unos segundos para que se abra el cuadro de diálogo de impresión
    time.sleep(3)

    # Escribir el nombre del archivo
    nombre_archivo = "nombre_de_archivo"  # Cambiar al nombre que desees
    pyautogui.write(nombre_archivo)

    # Simular las teclas para guardar la imagen
    pyautogui.press('tab')  # Seleccionar "Save" en el cuadro de diálogo
    time.sleep(1)

    # Presionar Enter para guardar
    pyautogui.press('enter')

    # Esperar un poco antes de cerrar el navegador
    time.sleep(5)  # Puedes ajustar el tiempo según necesites

    # Obtener la ruta de la carpeta de descargas
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Listar todos los archivos en la carpeta de descargas
    archivos_descargados = os.listdir(downloads_folder)

    # Filtrar archivos por extensión, en este caso, asumiendo que es un archivo PDF
    archivos_pdf = [archivo for archivo in archivos_descargados if archivo.endswith(".pdf")]

    # Obtener el archivo más reciente
    ultimo_archivo_descargado = max(archivos_pdf, key=lambda x: os.path.getctime(os.path.join(downloads_folder, x)))

    # Crear la ruta completa al último archivo descargado
    ruta_ultimo_archivo = os.path.join(downloads_folder, ultimo_archivo_descargado)

    # Definir la carpeta de destino
    carpeta_destino = "C:/Users/Admin/Desktop/Code/formWorker/I94"

    # Mover el archivo a la carpeta de destino
    shutil.move(ruta_ultimo_archivo, carpeta_destino)

    print(f"Se ha movido el archivo '{ultimo_archivo_descargado}' a '{carpeta_destino}'")

finally:
    # Cerrar el navegador al finalizar
    driver.quit()
