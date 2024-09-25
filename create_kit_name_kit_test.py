import sender_stand_request
import data
from data import kit_body


def get_new_user_token(authorization):
    auth_token = data.auth_token.copy()
    auth_token["authToken"] = authorization
    return auth_token

# Función para cambiar el valor del parámetro name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor name requerido
    return current_body

# Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable get_kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert kit_response.json()["name"] != ""

    # Comprobar que el resultado de la solicitud se guarda en kits_response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # String que debe estar en el cuerpo de respuesta
    str_kit = kit_response.json()["name"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert kit_response.text.count(str_kit) == 1

# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos,  "\
                                         "los nombres deben tener al menos 1 caracter y no más de 511 caracteres"

# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 caracteres
def test_create_kit_511_letter_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Prueba 3. Error. El parámetro firstName contiene 16 caracteres
def test_create_user_512_letter_in_first_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Prueba 4. Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres latinos
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa")

# Prueba 5.  El parámetro name contiene un string de caracteres especiales
def test_create_kit_has_special_symbol_in_first_name_get_error_response():
    positive_assert("\"№%@\",")

# Prueba 6. El parámetro name contiene un string de dígitos
def test_create_kit_has_number_in_name_get_error_response():
    positive_assert("123")

# Prueba 7. Error. Falta el parámetro firstName en la solicitud
def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    kit_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_code_400(kit_body)

# Prueba 8. Error. El parámetro name contiene 0 carácter
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("")

# Prueba 9. Error. El tipo del parámetro firstName: número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = get_kit_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400