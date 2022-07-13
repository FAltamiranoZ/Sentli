import PySimpleGUI as sg
import GUI as gui
import Comandos as cmd
 
sg.theme('Reddit') 
 
layout = [  [sg.Text('Porfavor inicia sesión para continuar')], 
            [sg.Text('Nombre del usuario y dominio con formato "nombreUsuario@nombreDominio"'), sg.InputText(key='idUsuario')], 
            [sg.Text('Contraseña'), sg.InputText(key='contraseña')],
            [sg.Button('Iniciar sesión')],
            [sg.Button('Salir')] 
        ] 

window = sg.Window('Sentli GUI', layout) 

while True: 
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Salir': 
        break 
    elif event == 'Iniciar sesión':
        #Escribir acá lo del chequeo del inicio de sesión
        idUsuario = values['idUsuario']
        contraseña = values['contraseña']
        if idUsuario == 'admin@domain' and contraseña == 'admin':
            irohaObject = cmd.irohaObject(idUsuario)
            signingPrivateKey = 'f101537e319568c765b2cc89698325604991dca57b9716b58016b253506cab70'
            tipoInterfaz = 'administrador'
            gui.main(window, tipoInterfaz, idUsuario, irohaObject, signingPrivateKey)
        elif idUsuario == 'userone@domain' and contraseña == 'userone':
            irohaObject = cmd.irohaObject(idUsuario)
            signingPrivateKey = '622e124e078333c58c644f5d107ac8a5c0002aeee222104411355ab10fc0faa8'
            tipoInterfaz = 'usuario'
            gui.main(window, tipoInterfaz, idUsuario, irohaObject, signingPrivateKey)
        elif idUsuario == 'usertwo@domain' and contraseña == 'usertwo':
            irohaObject = cmd.irohaObject(idUsuario)
            signingPrivateKey = '116eac80e88983cabb0b47bcf2be1c0a25222e6aa30ec43bd5dcc3144eaf4c60'
            tipoInterfaz = 'usuario'
            gui.main(window, tipoInterfaz, idUsuario, irohaObject, signingPrivateKey)
        elif idUsuario == 'money_administrator@domain' and contraseña == 'money_administrator':
            irohaObject = cmd.irohaObject(idUsuario)
            signingPrivateKey = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
            tipoInterfaz = 'administrador de dinero'
            gui.main(window, tipoInterfaz, idUsuario, irohaObject, signingPrivateKey)
        else:
            sg.popup('Usuario o contraseña incorrectos')

window.close()