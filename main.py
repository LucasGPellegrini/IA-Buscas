from ASTR    import ASTR
from BPI     import BPI
from BMC     import BMC
from Est2NF  import Est2NF
from Prob2NF import Prob2NF
from Solucao import Solucao

init = Est2NF(['B','B','','P','P'])
meta = [Est2NF(['B','P','P','B','']),
        Est2NF(['P','B','B','P','']),
        Est2NF(['','P','B','B','P']),
        Est2NF(['','B','P','P','B'])]

#estd1 = Est2NF(['B','B','P','P',''])
#estd2 = Est2NF(['B','P','P','B',''])

p1 = Prob2NF(init, meta)
#if BPI.busca(p1, 10):
#    print(p1.solucao.__str__())

#if BMC.busca(p1):
#        print(p1.solucao.__str__())

if ASTR.busca(p1):
        print(p1.solucao.__str__())
