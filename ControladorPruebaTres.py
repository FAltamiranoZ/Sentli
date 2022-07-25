import multiprocessing
from ScriptPruebaTres import añadirSentli

for i in range(1, 11):
    if __name__ == '__main__':  
        numeroReferencia = str(i)
        proc = multiprocessing.Process(target=añadirSentli, args=(numeroReferencia))
        proc.start()
print('\n')


