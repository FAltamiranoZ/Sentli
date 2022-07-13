import PySimpleGUI as sg
import Comandos as cmd

#TODO: Cambiar todos los print('Hola') por la funcionalidad de Comandos.py e implementar las funcionalidades.
def crear_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario'), sg.InputText()], 
        [sg.Text('Escribe el nombre del dominio'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_una_cuenta_window = sg.Window('Crear una cuenta', layout)

    while True: 
        event, values = crear_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    crear_una_cuenta_window.close()

def asignar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText()], 
        [sg.Text('Escribe el nombre del rol'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    asignar_un_rol_de_una_cuenta_window = sg.Window('Asignar un rol de una cuenta', layout)

    while True: 
        event, values = asignar_un_rol_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    asignar_un_rol_de_una_cuenta_window.close()

#Falta implementar esta funcionalidad
def eliminar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText()], 
        [sg.Text('Escribe el nombre del rol'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    eliminar_un_rol_de_una_cuenta_window = sg.Window('Eliminar un rol de una cuenta', layout)

    while True: 
        event, values = eliminar_un_rol_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    eliminar_un_rol_de_una_cuenta_window.close()

def consultar_todos_los_roles_activos_window(irohaObject, signingPrivateKey):
    layout = [   
        #print('Hola')
        [sg.Button('Volver')] 
    ]

    consultar_todos_los_roles_activos_window = sg.Window('Consultar todos los roles activos', layout)

    while True: 
        event, values = consultar_todos_los_roles_activos_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
    consultar_todos_los_roles_activos_window.close()

def consultar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText()], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_la_informacion_de_una_cuenta_window = sg.Window('Consultar la informacion de una cuenta', layout)

    while True: 
        event, values = consultar_la_informacion_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_la_informacion_de_una_cuenta_window.close()

def modificar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText()], 
        [sg.Text('Escribe el nombre del campo a modificar'), sg.InputText()],
        [sg.Text('Escribe el nuevo valor'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    modificar_la_informacion_de_una_cuenta_window = sg.Window('Modificar la informacion de una cuenta', layout)

    while True: 
        event, values = modificar_la_informacion_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    modificar_la_informacion_de_una_cuenta_window.close()

#Tecnicamente ya está pero falta implementarlo como standalone
def crear_una_moneda_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre de la moneda'), sg.InputText()],
        [sg.Text('Escribe el nombre del dominio'), sg.InputText()],
        [sg.Text('Escribe la cantidad de decimales que usará la moneda'), sg.InputText()], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_una_moneda_window = sg.Window('Crear una moneda', layout)

    while True: 
        event, values = crear_una_moneda_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    crear_una_moneda_window.close()

def consultar_la_informacion_de_una_moneda_window(irohaObject, signingPrivateKey): 
    layout = [  
        [sg.Text('Escribe el nombre de la moneda y dominio con formato "nombreMoneda#nombreDominio"'), sg.InputText()], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_la_informacion_de_una_moneda_window = sg.Window('Consultar la informacion de una moneda', layout)

    while True: 
        event, values = consultar_la_informacion_de_una_moneda_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_la_informacion_de_una_moneda_window.close()

#Tecnicamente ya está pero falta implementarlo como standalone
def crear_un_dominio_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del dominio'), sg.InputText()],
        [sg.Text('Escribe el nombre del rol default del dominio'), sg.InputText()], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_un_dominio_window = sg.Window('Crear un dominio', layout)

    while True: 
        event, values = crear_un_dominio_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    crear_un_dominio_window.close()

def añadir_un_nodo_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la dirección ip y puerto del nodo que se va a crear con formato "direcciónIP:puerto"'), sg.InputText()],
        [sg.Text('Escribe el la llave pública del nodo que se va a crear, esta debe contener exactamente 64 caracteres'), sg.InputText()], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_un_nodo_window = sg.Window('Añadir un nodo', layout)

    while True: 
        event, values = añadir_un_nodo_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    añadir_un_nodo_window.close()

def eliminar_un_nodo_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la dirección ip y puerto del nodo que se va a eliminar con formato "direcciónIP:puerto"'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    eliminar_un_nodo_window = sg.Window('Eliminar un nodo', layout)

    while True: 
        event, values = eliminar_un_nodo_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    eliminar_un_nodo_window.close()

def consultar_todos_los_nodos_activos_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario que va a consultar los nodos con formato "nombreUsuario@nombreDominio"'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_todos_los_nodos_activos_window = sg.Window('Consultar todos los nodos activos', layout)

    while True: 
        event, values = consultar_todos_los_nodos_activos_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_todos_los_nodos_activos_window.close()

def consultar_informacion_sobre_una_transaccion_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el hash la transaccion'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_informacion_sobre_una_transaccion_window = sg.Window('Consultar informacion sobre una transaccion', layout)

    while True: 
        event, values = consultar_informacion_sobre_una_transaccion_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_informacion_sobre_una_transaccion_window.close()

def consultar_informacion_sobre_varias_transacciones_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el hash de las transacciones separadas por comas, mínimo más de 1'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_informacion_sobre_varias_transacciones_window = sg.Window('Consultar informacion sobre varias transacciones', layout)

    while True: 
        event, values = consultar_informacion_sobre_varias_transacciones_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_informacion_sobre_varias_transacciones_window.close()

def consultar_las_transacciones_de_una_cuenta_en_un_dominio_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario que va a consultar las transacciones con formato "nombreUsuario@nombreDominio"'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_las_transacciones_de_una_cuenta_en_un_dominio_window = sg.Window('Consultar las transacciones de una cuenta en un dominio', layout)

    while True: 
        event, values = consultar_las_transacciones_de_una_cuenta_en_un_dominio_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_las_transacciones_de_una_cuenta_en_un_dominio_window.close()

#Falta implementar esta funcionalidad
def convertir_pesos_a_sentli_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Introduce la cantidad de pesos que deseas convertir en Sentli'), sg.InputText()],
        [sg.Text('A continuación, introduce la información de pago')],
        [sg.Text('Nombre del titular'), sg.InputText()],
        [sg.Text('Número de tarjeta'), sg.InputText()],
        [sg.Text('Fecha de expiración'), sg.InputText()],
        [sg.Text('CVV'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    convertir_pesos_a_sentli_window = sg.Window('Convertir pesos a sentli', layout)

    while True: 
        event, values = convertir_pesos_a_sentli_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    convertir_pesos_a_sentli_window.close()

#No olvidar agregar el parámetro del sentli#domain
def transferir_sentli_a_otro_usuario_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario que va a recibir los Sentli con formato "nombreUsuario@nombreDominio"'), sg.InputText()],
        [sg.Text('Escribe la cantidad de sentli que deseas transferir utilizando dos decimales'), sg.InputText()],
        [sg.Text('Escribe la descripición de esta transacción'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    transferir_sentli_a_otro_usuario_window = sg.Window('Transferir sentli a otro usuario', layout)

    while True: 
        event, values = transferir_sentli_a_otro_usuario_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    transferir_sentli_a_otro_usuario_window.close()

#No olvidar agregar el parámetro del sentli#domain
def consultar_mi_cantidad_de_sentli_actual_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        #print('Hola')
        [sg.Button('Volver')] 
    ]

    consultar_mi_cantidad_de_sentli_actual_window = sg.Window('Consultar mi cantidad de sentli actual', layout)

    while True: 
        event, values = consultar_mi_cantidad_de_sentli_actual_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
    consultar_mi_cantidad_de_sentli_actual_window.close()

#No olvidar agregar el parámetro del sentli#domain
def consultar_todas_mis_transacciones_de_sentli_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        #print('Hola')
        [sg.Button('Volver')] 
    ]

    consultar_todas_mis_transacciones_de_sentli_window = sg.Window('Consultar todas mis transacciones de sentli', layout)

    while True: 
        event, values = consultar_todas_mis_transacciones_de_sentli_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
    consultar_todas_mis_transacciones_de_sentli_window.close()
    
def consultar_la_informacion_de_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        #print('Hola')
        [sg.Button('Volver')] 
    ]

    consultar_la_informacion_de_mi_cuenta_window = sg.Window('Consultar la información de mi cuenta', layout)

    while True: 
        event, values = consultar_la_informacion_de_mi_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
    consultar_la_informacion_de_mi_cuenta_window.close()

#Falta implementar esta funcionalidad
def añadir_llaves_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la llave que desees añadir'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_llaves_window = sg.Window('Añadir llaves', layout)

    while True: 
        event, values = añadir_llaves_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    añadir_llaves_window.close()

#No olvidar agregar el parámetro del sentli#domain
def añadir_sentli_a_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la cantidad de sentli que deseas añadir utilizando dos decimales'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_sentli_a_mi_cuenta_window = sg.Window('Añadir sentli a mi cuenta', layout)

    while True: 
        event, values = añadir_sentli_a_mi_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    añadir_sentli_a_mi_cuenta_window.close()

#Falta implementar esta funcionalidad
def quitar_sentli_de_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la cantidad de sentli que deseas quitar utilizando dos decimales'), sg.InputText()],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    quitar_sentli_de_mi_cuenta_window = sg.Window('Quitar sentli de mi cuenta', layout)

    while True: 
        event, values = quitar_sentli_de_mi_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    quitar_sentli_de_mi_cuenta_window.close()

def consultar_las_transacciones_de_sentli_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario con formato "nombreUsuario@nombreDominio"'), sg.InputText()],
        [sg.Button('Confirmar')],
        [sg.Button('Volver')] 
    ]

    consultar_las_transacciones_de_sentli_de_una_cuenta_window = sg.Window('Consultar las transacciones de sentli de una cuenta en un dominio', layout)

    while True:
        event, values = consultar_las_transacciones_de_sentli_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            print('Hola')
    consultar_las_transacciones_de_sentli_de_una_cuenta_window.close()


