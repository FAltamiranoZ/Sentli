import PySimpleGUI as sg
import Comandos as cmd

#TODO: Cambiar todos los print('Hola') por la funcionalidad de Comandos.py e implementar las funcionalidades.
def crear_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario'), sg.InputText(key='nombreUsuario')], 
        [sg.Text('Escribe el nombre del dominio'), sg.InputText(key='nombreDominio')],
        [sg.Text('Escribe su llave pública'), sg.InputText(key='publicKey')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_una_cuenta_window = sg.Window('Crear una cuenta', layout)

    while True: 
        event, values = crear_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            nombreUsuario = values['nombreUsuario']
            nombreDominio = values['nombreDominio']
            publicKey = values['publicKey']
            sg.popup(cmd.create_account(nombreUsuario, nombreDominio, publicKey, irohaObject, signingPrivateKey))
    crear_una_cuenta_window.close()

def asignar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')], 
        [sg.Text('Escribe el nombre del rol'), sg.InputText(key='nombreRol')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    asignar_un_rol_de_una_cuenta_window = sg.Window('Asignar un rol de una cuenta', layout)

    while True: 
        event, values = asignar_un_rol_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            nombreRol = values['nombreRol']
            sg.popup(cmd.set_role(idUsuario, nombreRol, irohaObject, signingPrivateKey))
    asignar_un_rol_de_una_cuenta_window.close()

def eliminar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')], 
        [sg.Text('Escribe el nombre del rol'), sg.InputText(key='nombreRol')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    eliminar_un_rol_de_una_cuenta_window = sg.Window('Eliminar un rol de una cuenta', layout)

    while True: 
        event, values = eliminar_un_rol_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            nombreRol = values['nombreRol']
            sg.popup(cmd.detach_role(idUsuario, nombreRol, irohaObject, signingPrivateKey))
    eliminar_un_rol_de_una_cuenta_window.close()

def consultar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_la_informacion_de_una_cuenta_window = sg.Window('Consultar la informacion de una cuenta', layout)

    while True: 
        event, values = consultar_la_informacion_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            sg.popup(cmd.get_account(idUsuario, irohaObject, signingPrivateKey))
    consultar_la_informacion_de_una_cuenta_window.close()

def modificar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')], 
        [sg.Text('Escribe el nombre del campo a modificar'), sg.InputText(key='nombreCampo')],
        [sg.Text('Escribe el nuevo valor'), sg.InputText(key='valor')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    modificar_la_informacion_de_una_cuenta_window = sg.Window('Modificar la informacion de una cuenta', layout)

    while True: 
        event, values = modificar_la_informacion_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            nombreCampo = values['nombreCampo']
            valor = values['valor']
            sg.popup(cmd.set_detail_to_account(idUsuario, nombreCampo, valor, irohaObject, signingPrivateKey))
    modificar_la_informacion_de_una_cuenta_window.close()

def crear_una_moneda_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre de la moneda'), sg.InputText(key='nombreMoneda')],
        [sg.Text('Escribe el nombre del dominio'), sg.InputText(key='nombreDominio')],
        [sg.Text('Escribe la cantidad de decimales que usará la moneda'), sg.InputText(key='decimales')], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_una_moneda_window = sg.Window('Crear una moneda', layout)

    while True: 
        event, values = crear_una_moneda_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            nombreMoneda = values['nombreMoneda']
            nombreDominio = values['nombreDominio']
            decimales = values['decimales']
            sg.popup(cmd.create_asset(nombreDominio, nombreMoneda, decimales, irohaObject, signingPrivateKey))
    crear_una_moneda_window.close()

def consultar_la_informacion_de_una_moneda_window(irohaObject, signingPrivateKey): 
    layout = [  
        [sg.Text('Escribe el nombre de la moneda y dominio con formato "nombreMoneda#nombreDominio"'), sg.InputText(key='idMoneda')], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_la_informacion_de_una_moneda_window = sg.Window('Consultar la informacion de una moneda', layout)

    while True: 
        event, values = consultar_la_informacion_de_una_moneda_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idMoneda = values['idMoneda']
            sg.popup(cmd.get_asset_info(idMoneda, irohaObject, signingPrivateKey))
    consultar_la_informacion_de_una_moneda_window.close()

def crear_un_dominio_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el nombre del dominio'), sg.InputText(key='nombreDominio')],
        [sg.Text('Escribe el nombre del rol default del dominio'), sg.InputText(key='rolDefault')], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    crear_un_dominio_window = sg.Window('Crear un dominio', layout)

    while True: 
        event, values = crear_un_dominio_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            nombreDominio = values['nombreDominio']
            rolDefault = values['rolDefault']
            sg.popup(cmd.create_domain(nombreDominio, rolDefault, irohaObject, signingPrivateKey))
    crear_un_dominio_window.close()

def añadir_un_nodo_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la dirección ip y puerto del nodo que se va a crear con formato "direcciónIP:puerto"'), sg.InputText(key='ipYPuerto')],
        [sg.Text('Escribe el la llave pública del nodo que se va a crear, esta debe contener exactamente 64 caracteres'), sg.InputText(key='llavePublica')], 
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_un_nodo_window = sg.Window('Añadir un nodo', layout)

    while True: 
        event, values = añadir_un_nodo_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            ipYPuerto = values['ipYPuerto']
            llavePublica = values['llavePublica']
            sg.popup(cmd.add_peer(idUsuario, ipYPuerto, llavePublica, irohaObject, signingPrivateKey))
    añadir_un_nodo_window.close()

def eliminar_un_nodo_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la llave pública del nodo que se va a eliminar, esta debe contener exactamente 64 caracteres'), sg.InputText(key='llavePublica')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    eliminar_un_nodo_window = sg.Window('Eliminar un nodo', layout)

    while True: 
        event, values = eliminar_un_nodo_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            llavePublica = values['llavePublica']
            sg.popup(cmd.remove_peer(llavePublica, irohaObject, signingPrivateKey))
    eliminar_un_nodo_window.close()

def consultar_informacion_sobre_una_transaccion_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el hash la transaccion'), sg.InputText(key='hash')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_informacion_sobre_una_transaccion_window = sg.Window('Consultar informacion sobre una transaccion', layout)

    while True: 
        event, values = consultar_informacion_sobre_una_transaccion_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            hash = values['hash']
            sg.popup(cmd.get_transaction_data(hash, irohaObject, signingPrivateKey))
    consultar_informacion_sobre_una_transaccion_window.close()

def consultar_informacion_sobre_varias_transacciones_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el hash de las transacciones separadas por comas, mínimo más de 1'), sg.InputText(key='hashes')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_informacion_sobre_varias_transacciones_window = sg.Window('Consultar informacion sobre varias transacciones', layout)

    while True: 
        event, values = consultar_informacion_sobre_varias_transacciones_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            hashes = values['hashes']
            sg.popup(cmd.get_transactions_data(hashes, irohaObject, signingPrivateKey))
    consultar_informacion_sobre_varias_transacciones_window.close()

def consultar_las_transacciones_de_una_cuenta_en_un_dominio_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario que va a consultar las transacciones con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    consultar_las_transacciones_de_una_cuenta_en_un_dominio_window = sg.Window('Consultar las transacciones de una cuenta en un dominio', layout)

    while True: 
        event, values = consultar_las_transacciones_de_una_cuenta_en_un_dominio_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            sg.popup(cmd.get_account_transactions(idUsuario, irohaObject, signingPrivateKey))
    consultar_las_transacciones_de_una_cuenta_en_un_dominio_window.close()

#Aquí hacer una llamada a transfer a los comandos de money administrator para que este se agregue a si mismo la cantidad especificada y luego haga una transacción a este usuario por esa cantidad
def convertir_pesos_a_sentli_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Introduce la cantidad de pesos que deseas convertir en Sentli'), sg.InputText(key='cantidad')],
        [sg.Text('A continuación, introduce la información de pago')],
        [sg.Text('Nombre del titular'), sg.InputText(key='nombre')],
        [sg.Text('Número de tarjeta'), sg.InputText(key='numero')],
        [sg.Text('Fecha de expiración'), sg.InputText(key='fecha')],
        [sg.Text('CVV'), sg.InputText(key='cvv')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    convertir_pesos_a_sentli_window = sg.Window('Convertir pesos a sentli', layout)

    while True: 
        event, values = convertir_pesos_a_sentli_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            cantidad = values['cantidad']
            nombre = values['nombre']
            numero = values['numero']
            fecha = values['fecha']
            cvv = values['cvv']
            moneyAdministratorIrohaObject = cmd.irohaObject('money_administrator@domain')
            moneyAdministratorSigningPrivateKey = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
            sg.popup(cmd.add_assets('sentli#domain', cantidad, moneyAdministratorIrohaObject, moneyAdministratorSigningPrivateKey))
            sg.popup(cmd.transfer_asset_from_account_one_to_account_two('money_administrator@domain', idUsuario, 'sentli#domain', 'Pago de Sentli a la cuenta: ' + idUsuario, cantidad, moneyAdministratorIrohaObject, moneyAdministratorSigningPrivateKey))
    convertir_pesos_a_sentli_window.close()

def transferir_sentli_a_otro_usuario_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario que va a recibir los Sentli con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario2')],
        [sg.Text('Escribe la cantidad de sentli que deseas transferir utilizando dos decimales'), sg.InputText(key='cantidad')],
        [sg.Text('Escribe la descripición de esta transacción'), sg.InputText(key='descripcion')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    transferir_sentli_a_otro_usuario_window = sg.Window('Transferir sentli a otro usuario', layout)

    while True: 
        event, values = transferir_sentli_a_otro_usuario_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idMoneda = 'sentli#domain'
            idUsuario2 = values['idUsuario2']
            cantidad = values['cantidad']
            descripcion = values['descripcion']
            sg.popup(cmd.transfer_asset_from_account_one_to_account_two(idUsuario, idUsuario2, idMoneda, descripcion, cantidad, irohaObject, signingPrivateKey))
    transferir_sentli_a_otro_usuario_window.close()

def añadir_llaves_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la llave que desees añadir'), sg.InputText(key='llave')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_llaves_window = sg.Window('Añadir llaves', layout)

    while True: 
        event, values = añadir_llaves_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            llave = values['llave']
            sg.popup(cmd.add_signatory(idUsuario, llave, irohaObject, signingPrivateKey))
    añadir_llaves_window.close()

def añadir_sentli_a_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la cantidad de sentli que deseas añadir utilizando dos decimales'), sg.InputText(key='cantidad')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    añadir_sentli_a_mi_cuenta_window = sg.Window('Añadir sentli a mi cuenta', layout)

    while True: 
        event, values = añadir_sentli_a_mi_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            cantidad = values['cantidad']
            idMoneda = 'sentli#domain'
            sg.popup(cmd.add_assets(idMoneda, cantidad, irohaObject, signingPrivateKey))
    añadir_sentli_a_mi_cuenta_window.close()

def quitar_sentli_de_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe la cantidad de sentli que deseas quitar utilizando dos decimales'), sg.InputText(key='cantidad')],
        [sg.Button('Confirmar')], 
        [sg.Button('Volver')] 
    ]

    quitar_sentli_de_mi_cuenta_window = sg.Window('Quitar sentli de mi cuenta', layout)

    while True: 
        event, values = quitar_sentli_de_mi_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            cantidad = values['cantidad']
            sg.popup(cmd.substract_assets('sentli#domain', cantidad, irohaObject, signingPrivateKey))
    quitar_sentli_de_mi_cuenta_window.close()

def consultar_las_transacciones_de_sentli_de_una_cuenta_window(irohaObject, signingPrivateKey):
    layout = [  
        [sg.Text('Escribe el id del usuario con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')],
        [sg.Button('Confirmar')],
        [sg.Button('Volver')] 
    ]

    consultar_las_transacciones_de_sentli_de_una_cuenta_window = sg.Window('Consultar las transacciones de sentli de una cuenta en un dominio', layout)

    while True:
        event, values = consultar_las_transacciones_de_sentli_de_una_cuenta_window.read() 
        if event == sg.WIN_CLOSED or event == 'Volver': 
            break 
        elif event == 'Confirmar':
            idUsuario = values['idUsuario']
            idMoneda = 'sentli#domain'
            sg.popup(cmd.get_account_asset_transactions(idUsuario, idMoneda, irohaObject, signingPrivateKey))
    consultar_las_transacciones_de_sentli_de_una_cuenta_window.close()


