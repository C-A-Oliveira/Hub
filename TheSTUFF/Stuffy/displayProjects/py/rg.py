import random
import re

def newRG():
    RG = []
    DV = 0
    total = 0
    for i in range(8):
        RG.append(random.randint(0, 9))
        total += ((i+2) * RG[i])
    while (DV * 100 + total) % 11 != 0:
        DV += 1
    RG.append(DV)
    
    RG = map(str, RG)
    RG = "".join(RG)
    return RG

def newRG_formatado():
    rg = newRG()
    return '{}.{}.{}-{}'.format(rg[:2], rg[2:5], rg[5:8], rg[8:])


def validaRG(target):
    # adicionar mais "checks"
    # > vazio
    # > não numeros
    if re.search('[a-zA-Z]', target): return 'Invalid input'
    # > tamanho
    target = target.replace('.','')
    target = target.replace('-','')
    if len(target) != 9 or not re.search('([0-9]){9}', target): return 'Invalid input'

    DV = 0
    total = 0
    for i in range(8):
        total += ((i+2) * int(target[i]))
    while (DV * 100 + total) % 11 != 0:
        DV += 1
    if DV != int(target[8]):
        return 'Invalid'
    else: return 'All OK' 

