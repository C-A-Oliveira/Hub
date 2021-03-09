import random
import re
def newCPF():
    PDV = 0
    SDV = 0
    CPF = []
    for i in range(9):
        CPF.append(random.randint(0, 9))
        PDV += CPF[i] * (10 - i)
        SDV += CPF[i] * (11 - i)
    if PDV % 11 < 2:
        CPF.append(0)
    else:
        CPF.append(11 - PDV % 11)
    SDV += 2 * CPF[9]
    if SDV % 11 < 2:
        CPF.append(0)
    else:
        CPF.append(11 - SDV % 11)
    CPF = map(str, CPF)
    CPF = "".join(CPF)
    return  CPF

def newCPF_formatado():
    cpf = newCPF()
    return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

def validaCPF(target):
    # adicionar mais "checks"
    # > vazio
    # > não numeros
    if re.search('[a-zA-Z]', target): return 'Invalid input'
    # > tamanho
    target = target.replace('.','')
    target = target.replace('-','')
    if len(target) != 11 or not re.search('([0-9]){11}', target): return 'Invalid input'

    PDV = 0
    SDV = 0
    d_10 = 0
    d_11 = 0
    for i in range(9):
        PDV += int(target[i]) * (10 - i)
        SDV += int(target[i]) * (11 - i)
    if PDV % 11 < 2: d_10 = 0
    else: d_10 = 11 - PDV % 11
    if int(target[9]) != d_10: 
        return 'Invalid'
    else:
        SDV += 2 * int(target[9])
        if SDV % 11 < 2: d_11 = 0
        else: d_11 = 11 - SDV % 11
        if int(target[10]) != d_11: 
            return 'Invalid'
        else: return 'All OK' 

