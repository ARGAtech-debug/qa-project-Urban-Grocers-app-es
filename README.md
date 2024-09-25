# Proyecto Urban Grocers 

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

