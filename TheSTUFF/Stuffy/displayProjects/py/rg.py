import random

class RG:
    codigo = ''

    def __init__(self):        
        self.codigo = ''.join(map(str, aleatorio))

    def aleatorio(self):
        DIGITOS = []
        DV = 0
        total = 0
        for i in range(0, 8):
            DIGITOS.append(random.randint(0, 9))
            total += ((i+2) * DIGITOS[i])
        while (DV * 100 + total) % 11 != 0:
            DV += 1
        DIGITOS.append(DV)

        return DIGITOS


    def getCodigo(self):
        return self.codigo

    def getCodigoFormatado(self):
        return '{}.{}.{}-{}'.format(self.codigo[:2], self.codigo[2:5], self.codigo[5:8], self.codigo[8:])

    def getCodigoAleatorio(self):
        return aleatorio()

    def getCodigoAleatorioFormatado(self):
        codigo = aleatorio()
        return '{}.{}.{}-{}'.format(codigo[:2], codigo[2:5], self.codigo[5:8], self.codigo[8:])
