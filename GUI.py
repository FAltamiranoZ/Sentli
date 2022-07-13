import PySimpleGUI as sg
import GUIWindows as gw
 
sg.theme('Reddit') 

#Interfaz del usuario 
layout = [  [sg.Text('Bienvenido a tu portal Sentli')], 
#            [sg.Text('Enter something on Row 2'), sg.InputText()], 
            [sg.Button('Convertir pesos a Sentli', size=(50,1))], 
            [sg.Button('Transferir Sentli a otro usuario', size=(50,1))], 
            [sg.Button('Consultar mi cantidad de Sentli actual', size=(50,1))], 
            [sg.Button('Consultar todas mis transacciones', size=(50,1))], 
            [sg.Button('Consultar la información de mi cuenta', size=(50,1))], 
            [sg.Button('Añadir llaves', size=(50,1))], 
            [sg.Button('Salir')] 
        ] 
 
#Interfaz del administrador de dinero 
layout = [  [sg.Text('Bienvenido a tu portal Sentli')], 
            [sg.Button('Transferir Sentli a otro usuario', size=(50,1))], 
            [sg.Button('Consultar la información de una moneda', size=(50,1))], 
            [sg.Button('Añadir Sentli a mi cuenta', size=(50,1))], 
            [sg.Button('Quitar Sentli de mi cuenta', size=(50,1))], 
            [sg.Button('Consultar la información de una cuenta', size=(50,1))], 
            [sg.Button('Consultar todas las cuentas', size=(50,1))], 
            [sg.Button('Salir')] 
        ] 
 
#Interfaz del administrador 
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
            [sg.Button('Consultar las cuentas existentes en un dominio', size=(50,1))], 
            [sg.Button('Consultar las monedas existentes en un dominio', size=(50,1))], 
            [sg.Button('Consultar las transacciones existentes en un dominio', size=(50,1))], 
            [sg.Button('Consultar las transacciones de una cuenta en un dominio', size=(50,1))], 
            [sg.Button('Salir')] 
        ] 
 
window = sg.Window('Sentli GUI', layout)

while True: 
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED:
            break
        case 'Salir':
            break
        case 'Crear una cuenta':
            gw.crear_una_cuenta_window()
        case 'Asignar un rol de una cuenta':
            gw.asignar_un_rol_de_una_cuenta_window()
        case 'Eliminar un rol de una cuenta':
            gw.eliminar_un_rol_de_una_cuenta_window()
        case 'Consultar todos los roles activos':
            gw.consultar_todos_los_roles_activos_window()
        case 'Consultar la información de una cuenta':
            gw.consultar_la_informacion_de_una_cuenta_window()
        case 'Modificar la información de una cuenta':
            gw.modificar_la_informacion_de_una_cuenta_window()
        case 'Crear una moneda':
            gw.crear_una_moneda_window()
        case 'Consultar la información de una moneda':
            gw.consultar_la_informacion_de_una_moneda_window()
        case 'Crear un dominio':
            gw.crear_un_dominio_window()
        case 'Añadir un nodo':
            gw.añadir_un_nodo_window()
        case 'Eliminar un nodo':
            gw.eliminar_un_nodo_window()
        case 'Consultar todos los nodos activos':
            gw.consultar_todos_los_nodos_activos_window()
        case 'Consultar las cuentas existentes en un dominio':
            gw.consultar_las_cuentas_existentes_en_un_dominio_window()
        case 'Consultar todas las cuentas':
            gw.consultar_las_cuentas_existentes_en_un_dominio_window()
        case 'Consultar las monedas existentes en un dominio':
            gw.consultar_las_monedas_existentes_en_un_dominio_window()
        case 'Consultar las transacciones existentes en un dominio':
            gw.consultar_las_transacciones_existentes_en_un_dominio_window()
        case 'Consultar las transacciones de una cuenta en un dominio':
            gw.consultar_las_transacciones_de_una_cuenta_en_un_dominio_window()
        case 'Convertir pesos a Sentli':
            gw.convertir_pesos_a_sentli_window()
        case 'Transferir Sentli a otro usuario':
            gw.transferir_sentli_a_otro_usuario_window()
        case 'Consultar mi cantidad de Sentli actual':
            gw.consultar_mi_cantidad_de_sentli_actual_window()
        case 'Consultar todas mis transacciones':
            gw.consultar_todas_mis_transacciones_window()
        case 'Consultar la información de mi cuenta':
            gw.consultar_la_informacion_de_mi_cuenta_window()
        case 'Añadir llaves':
            gw.añadir_llaves_window()
        case 'Consultar la información de una moneda':
            gw.consultar_la_informacion_de_una_moneda_window()
        case 'Añadir Sentli a mi cuenta':
            gw.añadir_sentli_a_mi_cuenta_window()
        case 'Quitar Sentli de mi cuenta':
            gw.quitar_sentli_de_mi_cuenta_window()
        
window.close()