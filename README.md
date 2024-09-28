# Proyecto Urban Grocers 

Sprint 7 - Introducción a la automatización de pruebas.
Arturo Gallardo Garduño cohort 14 es.

¿Qué librerías se requieren?
Para este proyecto se ocuparán dos librerías:
Pytest: para la creación y ejecución de tests o automatización de pruebas.
Request: para trabajar con las solicitudes HTTP en Python.

¿Cómo instalarlas?

Pytest: Se tiene dos maneras de instalar este paquete de la librería:
A) A través de la terminal.
	1.- Donde debemos de abrirla como primer paso del proceso.
	2.- Ingresa el comando pip install pytest.
B) Mediante la pestaña "Python Packages" (paquetes de Python).
	1.- En PyCharm, dirígete al panel inferior y selcciona la pestaña "Python Packages" (Paquetes de Python).
	2.- En la barra de búsqueda, escribe "Pytest".
	3.- Localiza y selecciona el paquete "Pytest" de la lista.
	4.- Finalmente, haz clic en el botón "Install" (instalar).

Request: Se tiene dos maneras de instalar este paquete de la librería:
A) A través de la terminal.
	1.- Donde debemos de abrirla como primer paso del proceso.
	2.- Ingresa el comando pip install request.
B) Mediante la pestaña "Python Packages" (paquetes de Python).
	1.- En PyCharm, dirígete al panel inferior y selcciona la pestaña "Python Packages" (Paquetes de Python).
	2.- En la barra de búsqueda, escribe "request" (solicitudes).
	3.- Localiza y selecciona el paquete "request" de la lista.
	4.- Finalmente, haz clic en el botón "Install" (instalar).

¿Cómo usarlas?

Ejecución de pruebas: de igual forma que en la instalación, tenemos dos opciones para ejecutar tus pruebas, directamente
directamente desde la consola de PyCharm o utilizando su interfaz gráfica.

A) A través de la terminal.
	1.- Para ejecutar todas la pruebas de tu proyecto, simplemente escribe: pytest ruta/del/proyecto.
	2.- Para ejecutar las pruebas de un solo archivo, simplemente escribe: pytest nombre_de_proyecto.py
B) Ejecución desde la interfaz de PyCharm.
	1.- Mediante el corrido de las pruebas.


Requerimentos del proyecto:

Dentro del proyecto se toma como objetivo general crear un Kit dentro de un usuario o usuaria particular y no una tarjeta.
Para ello, habrá que tomar en cuenta los siguientes puntos:

-Es obligatorio pasar el encabezado Authorization para crear la kit (El programa también permite a través de un cardId,
pero el actual ejercicio no).
-Si se recibe una solicitud con un encabezado Authorisation que contenga el authToken de un/a ususario/a en particular, se
creará la kit de este/a usuario/a.
-Si se percibe el cardId, se creará una kit dentro de la tarjeta correspondiente.(Este no es el objetivo deseado).
-Si no se pasa ninguno de los parámetros, se devolverá un error.
-Cuando se pasan ambos arámetros, Authorization es la prioridad.

A través de las funciones Post se realiza el registro de un nuevo usuario/a para obtener un nuevo token de autorización
mediante el cual se generará el nuevo kit personal.
Dentro de la lista de comprobación que nos han otorgado podemos ver bajo los parámetros que se manejarán as pruebas, que
son los siguientes:

-El número permitido de caracteres para el nombre de la kit, dentro del cuerpo sera de 1 a 511.
-Se permitirán caracteres especiales, espacios y números siempre y cuando se registren como strings.
-Se deberá realizar una comprobación de que los datos estén llegando a la variable adecuada en cada prueba, en caso de que
no lo hagán se marcará el error.

Dentro de las necesidades del proyecto, se plantea el uso de 6 archivos que deberán de involucrarse para generar un proyecto
integro, los cuales son los siguientes:
-configuration.py : URL y rutas de solicitud.
-sender_stand_request.py : envío de solicitudes.
-data.py : datos requeridos y formatos de estos.
-create_kit_name_kit_test.py : pruebas a realizar.
-README.md : descripción del proyecto en general.
.gitignore : por normatividad, si hubiera algo que se debe omitir.

Siendo todo esto lo requerido, gracias por la atención.

