from ASTR    import ASTR
from BPI     import BPI
from BMC     import BMC
from SEML    import SEML
from BG      import BG
from Est2NF  import Est2NF
from Prob2NF import Prob2NF
from EstEsc  import EstEsc
from ProbEsc import ProbEsc
from Solucao import Solucao
import os
import sys
import time

# Constante para limpart terminal (Linux ou WIndows)
CLEAR = 'clear' if sys.platform.startswith('linux') else 'cls'

def main():
    # Cria problemas
    p2nf2 = Prob2NF(N=2)
    p2nf3 = Prob2NF(N=3)
    p2nf4 = Prob2NF(N=4)
    pescs = ProbEsc(tipo='Simples')
    #p1e11 = ProbEsc(tipo='11-1')
    #p2e11 = ProbEsc(tipo='11-2')
    peg18 = ProbEsc(tipo='Gauss-18')

    # Lista de problemas
    listap = [p2nf2, p2nf3, p2nf4, pescs, 'TODO', 'TODO', peg18]

    opt = 0
    busca = 0

    while opt > 8 or opt < 1:
        os.system(CLEAR)
        print("--------------OPCOES--------------")
        print("----------------------------------")
        print("1. 2NFichas com N = 2")
        print("2. 2NFichas com N = 3")
        print("3. 2NFichas com N = 4")
        print("4. Escalonamento - Simples")
        print("5. Escalonamento - Grafo de 11-1")
        print("6. Escalonamento - Grafo de 11-2")
        print("7. Escalonamento - Gauss 18")
        print("8. Sair do Programa")
        opt = int(input("Escolha uma opcao: "))


    if opt == 8: return

    custo_meta = False
    if opt >= 4: custo_meta = True # escalonamento

    problema = listap[opt-1]

    while busca > 5 or busca < 1:
        os.system(CLEAR)
        print("--------------BUSCAS--------------")
        print("----------------------------------")
        print("1. Profundidade Iterativa")
        print("2. Melhor Custo")
        print("3. A Estrela")
        print("4. Subida de Encosta")
        print("5. Busca Gulosa")
        busca = int(input("Escolha uma opcao: "))

    if busca == 1:
        pfd_max = int(input("Limite de altura: "))
        print('\n\n\n')

        start_time = time.time()
        if BPI.busca(problema, pfd_max): print(problema.solucao.__str__(cmeta = custo_meta))
        else: print('Solucao nao encontrada!')

        print(f'\n\nTempo Gasto: {time.time() - start_time}')
        input("\nPressione <Enter> para continuar.")
        main()
    elif busca == 2:
        print('\n\n\n')

        start_time = time.time()
        if BMC.busca(problema): print(problema.solucao.__str__(cmeta = custo_meta))
        else: print('Solucao nao encontrada!')

        print(f'\n\nTempo Gasto: {time.time() - start_time}')
        input("\nPressione <Enter> para continuar.")
        main()
    elif busca == 3:
        print('\n\n\n')

        start_time = time.time()
        if ASTR.busca(problema): print(problema.solucao.__str__(h=True, cmeta = custo_meta))
        else: print('Solucao nao encontrada!')

        print(f'\n\nTempo Gasto: {time.time() - start_time}')
        input("\nPressione <Enter> para continuar.")
        main()
    elif busca == 4:
        if opt >= 4: main()
        print('\n\n\n')

        start_time = time.time()
        if SEML.busca(problema): print(problema.solucao.__str__())
        else: print('Solucao nao encontrada!')

        print(f'\n\nTempo Gasto: {time.time() - start_time}')
        input("\nPressione <Enter> para continuar.")
        main()
    else: # busca == 5:
        if opt <= 3: main()
        print('\n\n\n')

        start_time = time.time()
        if BG.busca(problema): print(problema.solucao.__str__(cmeta = custo_meta))
        else: print('Solucao nao encontrada!')

        print(f'\n\nTempo Gasto: {time.time() - start_time}')
        input("\nPressione <Enter> para continuar.")
        main()


if __name__ == "__main__":
    main()
