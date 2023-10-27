from ASTR    import ASTR
from BPI     import BPI
from BMC     import BMC
from SEML    import SEML
from Est2NF  import Est2NF
from Prob2NF import Prob2NF
from Solucao import Solucao
import os
import sys


p = Prob2NF(N=2)

raiz = p.est_ini

#print(raiz.conteudo)


for vizinho in p.acao(Est2NF(['B','B','P','P',''])):
    print(vizinho.__str__()+'\n')

