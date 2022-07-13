import PySimpleGUI as sg
import Comandos as cmd


def crear_una_cuenta_window():
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

def asignar_un_rol_de_una_cuenta_window():
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

