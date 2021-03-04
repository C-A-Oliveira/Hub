import random
    
UPR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LWR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NBR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPC = ['!', '?', '@', '#', '$', '%', '&', '+', '-', '*', '/', '\\', '|', '(', ')', '[', ']', '{', '}', '<', '>']#, 'ç', 'Ç'

def getRandChar(key):
    if key == 1:    return(random.choice(UPR))
    elif key == 2:  return(random.choice(LWR))
    elif key == 3:  return(random.choice(NBR))
    else:           return(random.choice(SPC))


def makePassword(U, L, N, S, l):
    op = []
    if U == True: op.append(1)
    if L == True: op.append(2)
    if N == True: op.append(3)
    if S == True: op.append(4)

    lenght = l if l >= 8 and l <= 128 else 16
    i = 0

    STG = ""
    while i < lenght:
        STG+=getRandChar(random.choice(op))
        i+=1
    #print(STG)
    return STG


#randStg(0, 0, 1, 0, 31)

