import multiprocessing
import time
from ScriptPruebaTres import añadirSentli
from iroha import IrohaCrypto
import Comandos as cmd

money_administrator_private_key = '61c8067b64855de16e56504b316d06c64652faf1f83cabc8684887cd2682ccc4'
money_administrator_public_key = IrohaCrypto.derive_public_key(money_administrator_private_key)
money_administrator_iroha = cmd.irohaObject('money_administrator@domain')

start_time = time.time()
for i in range(1, 11):
    if __name__ == '__main__':  
        numeroReferencia = str(i)
        proc = multiprocessing.Process(target=añadirSentli, args=(numeroReferencia))
        proc.start()
print('\n')

for i in range(1, 11):
    if __name__ == '__main__':  
        proc.join()
print('\n')

cmd.get_account_assets('money_administrator@domain', money_administrator_iroha, money_administrator_private_key)
print('La ejecución ha durado: ' + str(time.time() - start_time) + ' segundos')
