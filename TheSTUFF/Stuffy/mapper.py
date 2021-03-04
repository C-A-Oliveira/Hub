from .displayProjects.py import randPassGen

def do_shit(some_shit):
    
    l = some_shit[0] 
    u = some_shit[1] 
    n = some_shit[2] 
    s = some_shit[3] 

    return randPassGen.makePassword(u, l, n, s, int(some_shit.pop()))