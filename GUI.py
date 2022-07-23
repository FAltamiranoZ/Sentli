import PySimpleGUI as sg
import GUIWindows as gw
import Comandos as cmd

def main(window, tipoInterfaz, idUsuario, irohaObject, signingPrivateKey):

    window.close()

    if tipoInterfaz == 'usuario':
        layout = [  [sg.Text('Bienvenido a tu portal Sentli')], 
                    [sg.Button('Convertir pesos a Sentli', size=(50,1))],
                    [sg.Button('Transferir Sentli a otro usuario', size=(50,1))], 
                    [sg.Button('Consultar mi cantidad de Sentli actual', size=(50,1))], 
                    [sg.Button('Consultar todas mis transacciones de Sentli', size=(50,1))], 
                    [sg.Button('Consultar la información de mi cuenta', size=(50,1))], 
                    [sg.Button('Añadir llaves', size=(50,1))], 
                    [sg.Button('Consultar mis llaves', size=(50,1))],
                    [sg.Button('Salir')] 
                ] 
    elif tipoInterfaz == 'administrador de dinero':
        layout = [  [sg.Text('Bienvenido a tu portal Sentli')], 
                    [sg.Button('Transferir Sentli a otro usuario', size=(50,1))], 
                    [sg.Button('Consultar la información de una moneda', size=(50,1))], 
                    [sg.Button('Añadir Sentli a mi cuenta', size=(50,1))], 
                    [sg.Button('Quitar Sentli de mi cuenta', size=(50,1))], 
                    [sg.Button('Consultar mi cantidad de Sentli actual', size=(50,1))], 
                    [sg.Button('Consultar la información de una cuenta', size=(50,1))], 
                    [sg.Button('Consultar las transacciones de Sentli de una cuenta', size=(50,1))], 
                    [sg.Button('Salir')] 
                ] 
    else:
        layout = [  [sg.Text('Bienvenido a tu portal Sentli')], 
                    [sg.Button('Crear una cuenta', size=(50,1))], 
                    [sg.Button('Asignar un rol de una cuenta', size=(50,1))], 
                    [sg.Button('Eliminar un rol de una cuenta', size=(50,1))], 
                    [sg.Button('Consultar todos los roles activos', size=(50,1))], 
                    [sg.Button('Consultar la información de una cuenta', size=(50,1))], 
                    [sg.Button('Modificar la información de una cuenta', size=(50,1))], 
                    [sg.Button('Crear una moneda', size=(50,1))], 
                    [sg.Button('Consultar la información de una moneda', size=(50,1))], 
                    [sg.Button('Crear un dominio', size=(50,1))], 
                    [sg.Button('Añadir un nodo', size=(50,1))], 
                    [sg.Button('Eliminar un nodo', size=(50,1))], 
                    [sg.Button('Consultar todos los nodos activos', size=(50,1))],  
                    [sg.Button('Consultar información sobre una transacción', size=(50,1))], 
                    [sg.Button('Consultar información sobre varias transacciones', size=(50,1))], 
                    [sg.Button('Consultar las transacciones de una cuenta en un dominio', size=(50,1))], 
                    [sg.Button('Salir')] 
                ] 
    
    windowMain = sg.Window('Sentli GUI', layout)

    while True: 
        event, values = windowMain.read()
        match event:
            case sg.WIN_CLOSED:
                break
            case 'Salir':
                break
            case 'Crear una cuenta':
                gw.crear_una_cuenta_window(irohaObject, signingPrivateKey)
            case 'Asignar un rol de una cuenta':
                gw.asignar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey)
            case 'Eliminar un rol de una cuenta':
                gw.eliminar_un_rol_de_una_cuenta_window(irohaObject, signingPrivateKey)
            case 'Consultar todos los roles activos':
                sg.popup(cmd.get_roles(irohaObject, signingPrivateKey))
            case 'Consultar la información de una cuenta':
                gw.consultar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey)
            case 'Modificar la información de una cuenta':
                gw.modificar_la_informacion_de_una_cuenta_window(irohaObject, signingPrivateKey)
            case 'Crear una moneda':
                gw.crear_una_moneda_window(irohaObject, signingPrivateKey)
            case 'Consultar la información de una moneda':
                gw.consultar_la_informacion_de_una_moneda_window(irohaObject, signingPrivateKey)
            case 'Crear un dominio':
                gw.crear_un_dominio_window(irohaObject, signingPrivateKey)
            case 'Añadir un nodo':
                gw.añadir_un_nodo_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Eliminar un nodo':
                gw.eliminar_un_nodo_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Consultar todos los nodos activos':
                sg.popup(cmd.get_peers(idUsuario, irohaObject, signingPrivateKey))
            case 'Consultar información sobre una transacción':
                gw.consultar_informacion_sobre_una_transaccion_window(irohaObject, signingPrivateKey)
            case 'Consultar información sobre varias transacciones':
                gw.consultar_informacion_sobre_varias_transacciones_window(irohaObject, signingPrivateKey)
            case 'Consultar las transacciones de una cuenta en un dominio':
                gw.consultar_las_transacciones_de_una_cuenta_en_un_dominio_window(irohaObject, signingPrivateKey)
            case 'Convertir pesos a Sentli':
                gw.convertir_pesos_a_sentli_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Transferir Sentli a otro usuario':
                gw.transferir_sentli_a_otro_usuario_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Consultar mi cantidad de Sentli actual':
                sg.popup(cmd.get_account_assets(idUsuario, irohaObject, signingPrivateKey))
            case 'Consultar todas mis transacciones de Sentli':
                sg.Print(cmd.get_account_asset_transactions(idUsuario, 'sentli#domain', irohaObject, signingPrivateKey))
            case 'Consultar la información de mi cuenta':
                sg.popup(cmd.get_account_details(idUsuario, irohaObject, signingPrivateKey))
            case 'Añadir llaves':
                gw.añadir_llaves_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Consultar mis llaves':
                sg.popup(cmd.get_signatories(idUsuario, irohaObject, signingPrivateKey))
            case 'Añadir Sentli a mi cuenta':
                gw.añadir_sentli_a_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Quitar Sentli de mi cuenta':
                gw.quitar_sentli_de_mi_cuenta_window(idUsuario, irohaObject, signingPrivateKey)
            case 'Consultar las transacciones de Sentli de una cuenta':
                gw.consultar_las_transacciones_de_sentli_de_una_cuenta_window(irohaObject, signingPrivateKey)

    windowMain.close()