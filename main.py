from multiprocessing import Process
from time import sleep
from functions import Saque, Deposito

if __name__ == '__main__':
    print('Operação Iniciada!\n')

    saldoConta1 = 500
    saldoConta2 = 200

    sacar1 = Process(target=Saque, args=(saldoConta1, 50))
    depositar2 = Process(target=Deposito, args=(saldoConta2, 150))

    sacar2 = Process(target=Saque, args=(saldoConta2, 80))
    depositar1 = Process(target=Deposito, args=(saldoConta1, 150))

    sacar1.start()
    depositar2.start()

    sleep(3)

    sacar2.start()
    depositar1.start()

    sleep(5)

    sacar1.terminate()
    depositar2.terminate()

    sacar2.terminate()
    depositar1.terminate()

    print('Operação Finalizada!\n')
