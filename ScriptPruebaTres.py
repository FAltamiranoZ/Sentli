from iroha import IrohaCrypto
import Comandos as cmd

money_administrator_private_key = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
money_administrator_public_key = IrohaCrypto.derive_public_key(money_administrator_private_key)
money_administrator_iroha = cmd.irohaObject('money_administrator@domain')

def añadirSentli(numeroProceso):
    print('\nProceso ' + str(numeroProceso) + ': Añadir 100 de Sentli a la cuenta money_administrator de uno en uno:')
    for i in range(1, 101):
        print('\nProceso ' + str(numeroProceso) + ': Añadiendo el Sentli número ' + str(i) + ' de 100 a la cuenta money_administrator')
    print('\n')


    