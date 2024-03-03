### Automatización de Descarga y Guardado de Archivos PDF

Este script de Python utiliza Selenium y PyAutoGUI para automatizar el proceso de descarga y guardado de archivos PDF desde un sitio web. En este ejemplo, el script está diseñado para trabajar con el desafío RPA en "https://rpachallenge.com/", pero puedes personalizarlo para otros sitios web con archivos descargables.

### Requisitos Previos
- Python 3.x instalado en tu sistema
- `selenium` y `pyautogui` instalados. Puedes instalarlos usando pip:
  ```
  pip install selenium
  pip install pyautogui
  ```
- ChromeDriver instalado y configurado en tu sistema. Asegúrate de especificar la ruta correcta en el código.

### Uso del Script
1. Clona o descarga este repositorio en tu máquina local.
2. Asegúrate de tener los requisitos previos instalados y configurados.
3. Ejecuta el script `descarga_guarda_pdf.py`.

### Funcionamiento
1. El script abre una instancia del navegador Chrome utilizando Selenium.
2. Navega a la página web "https://rpachallenge.com/".
3. Simula la combinación de teclas Ctrl + P para abrir la ventana de impresión.
4. Espera unos segundos para que aparezca la ventana de impresión.
5. Simula la tecla Enter para confirmar la impresión.
6. Espera unos segundos para que aparezca el cuadro de diálogo de guardado.
7. Especifica un nombre de archivo y guarda el archivo PDF en la carpeta de descargas.
8. Mueve el archivo PDF más reciente descargado a una carpeta específica.

### Personalización
- Cambia la URL en `driver.get("https://rpachallenge.com/")` para adaptarlo a tu sitio web.
- Modifica el nombre del archivo en `nombre_archivo` según tus preferencias.
- Ajusta los tiempos de espera (`time.sleep()`) según sea necesario.
- Cambia la ruta de la carpeta de destino en `carpeta_destino` para guardar los archivos PDF en otro lugar.

### Notas
- Este script está diseñado para archivos PDF, pero puedes modificarlo para otros tipos de archivos.
- Asegúrate de tener los permisos necesarios para mover archivos en las carpetas especificadas.

¡Disfruta de esta automatización para descargar y organizar tus archivos PDF de manera eficiente! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.
