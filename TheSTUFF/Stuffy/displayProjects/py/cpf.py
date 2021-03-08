import random

def newCPF():
    PDV = 0
    SDV = 0
    CPF = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        CPF[i] = random.randint(0, 9)
        PDV += CPF[i] * (10 - i)
        SDV += CPF[i] * (11 - i)
    if PDV % 11 < 2:
        CPF[9] = 0
        SDV += 2 * CPF[9]
    else:
        CPF[9] = 11 - PDV % 11
        SDV += 2 * CPF[9]
    if SDV % 11 < 2:
        CPF[10] = 0
    else:
        CPF[10] = 11 - SDV % 11
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
    # > tamanho
    target = target.replace('.','')
    target = target.replace('-','')
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
        return False
    else:
        SDV += 2 * int(target[9])
        if SDV % 11 < 2: d_11 = 0
        else: d_11 = 11 - SDV % 11
        if int(target[10]) != d_11: 
            return False
        else: return True 

