from ASTR    import ASTR
from BPI     import BPI
from BMC     import BMC
from SEML    import SEML
from Est2NF  import Est2NF
from Prob2NF import Prob2NF
from Solucao import Solucao
import os
import sys

# Constante para limpart terminal (Linux ou WIndows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():
    # Cria problemas
    p2nf2 = Prob2NF(N=2)
    p2nf3 = Prob2NF(N=3)
    p2nf4 = Prob2NF(N=4)

    # Lista de problemas
    listap = [p2nf2, p2nf3, p2nf4, 'TODO', 'TODO']

    opt = 0
    busca = 0

    while opt > 6 or opt < 1:
        os.system(CLEAR)
        print("--------------OPCOES--------------")
        print("----------------------------------")
        print("1. 2NFichas com N = 2")
        print("2. 2NFichas com N = 3")
        print("3. 2NFichas com N = 4")
        print("4. Escalonamento - Grafo de 11")
        print("5. Escalonamento - Grafo de 18")
        print("6. Sair do Programa")
        opt = int(input("Escolha uma opcao: "))


    if opt == 6: return

    problema = listap[opt-1]

    while busca > 4 or busca < 1:
        os.system(CLEAR)
        print("--------------BUSCAS--------------")
        print("----------------------------------")
        print("1. Profundidade Iterativa")
        print("2. Melhor Custo")
        print("3. A Estrela")
        print("4. Subida de Encosta")
        busca = int(input("Escolha uma opcao: "))

    if busca == 1:
        pfd_max = int(input("Limite de altura: "))
        print('\n\n\n')
        if BPI.busca(problema, pfd_max): print(problema.solucao.__str__())
        else: print('Solucao nao encontrada!')
        input("\n\nPressione <Enter> para continuar.")
        main()
    elif busca == 2:
        print('\n\n\n')
        if BMC.busca(problema): print(problema.solucao.__str__())
        else: print('Solucao nao encontrada!')
        input("\n\nPressione <Enter> para continuar.")
        main()
    elif busca == 3:
        print('\n\n\n')
        if ASTR.busca(problema): print(problema.solucao.__str__(h=True))
        else: print('Solucao nao encontrada!')
        input("\n\nPressione <Enter> para continuar.")
        main()
    else: # busca == 4:
        print('\n\n\n')
        if SEML.busca(problema): print(problema.solucao.__str__())
        else: print('Solucao nao encontrada!')
        input("\n\nPressione <Enter> para continuar.")
        main()


if __name__ == "__main__":
    main()
