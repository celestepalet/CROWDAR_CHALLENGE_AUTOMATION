# CROWDAR_CHALLENGE_AUTOMATION

### Para ejecutar las pruebas en WINDOWS debes tener instalado:

1. Python 3.11.5. Puedes descargarlo desde [python.org](https://www.python.org/downloads/)

2. Navegadores Chrome, Firefox o Edge en su útlima versión:

### Para configurar el ambiente ejecuta estos comandos en una terminal PowerShell en la raiz del proyecto (donde esta guardado el archivo requirements.txt):

1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requierements.txt
4. deactivate

### Para correr las pruebas:

1. Abra el archivo constants.py (ruta: ui>utils>constants.py) y añada las credenciales validas, en los campos VALID_USERNAME y VALID_PASSWORD.
2. Abra una terminal en la raiz del proyecto.
2. Active el entorno virtual: venv\Scripts\activate
3. Ejecute el comando: pytest --html=reports/report.html --browser chrome

Si cambias el tag "--browser chrome" por "--browser edge" o por "--browser firefox" las pruebas se ejecutaran en ese navegador.

Con el tag "--html=reports/report.html" se esta generando el reporte y guardando en la carpeta "reports" si lo sacas no se generará el reporte.

En caso de no querer correr todos los test puedes usar el tag "-k " y el nombre del la etiqueta de la prueba que quieres correr. Ejemplo "-k api_testing"

Cada prueba tiene sus etiquetas para correrlas indivivualmente.


-----------------------


### Posibles problemas
#### 1. Drivers

En caso de falla de las pruebas por los navegadores, debes configurar los drivers (no siempre es necesario)

Descarga los controladores (drivers) para Chrome, Firefox or Edge y agrega sus rutas al sistema.

ChromeDriver: https://sites.google.com/chromium.org/driver/

GeckoDriver (Firefox): https://github.com/mozilla/geckodriver/releases

Asegúrate de que las rutas de los controladores estén agregadas al PATH de tu sistema.

En cado de que no esten agregadas pueder hacerlo desde una terminal powershell con el comando "$env:PATH += ";C:\ruta\del\driver"

#### 2. Importaciones de los modulos

En caso de falla de las pruebas por las importaciones de los modulos asegurate de tener configurado la raiz del proyecto.

Asegúrate de que la variable de entorno PYTHONPATH esté configurada correctamente para que Python pueda encontrar los módulos.

Puedes hacerlo en una terminal PowerShell: $env:PYTHONPATH = "C:\ruta\del\proyecto;" + $env:PYTHONPATH