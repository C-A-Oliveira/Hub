from .displayProjects.py import randPassGen, cpf

def do_shit(some_shit):
    if some_shit['type'] == 'password_generator':
        pass_args = list(some_shit.values())[1:]
        l = pass_args[0] 
        u = pass_args[1] 
        n = pass_args[2] 
        s = pass_args[3] 

        return randPassGen.makePassword(u, l, n, s, int(pass_args.pop()))
    elif some_shit['type'] == 'doc_cpf':
        if some_shit['action'] == 'new':
            if some_shit['formated']: 
                return cpf.newCPF_formatado()
            else:
                return cpf.newCPF()
        elif some_shit['action'] == 'check':
            if some_shit['input'] == '': return
            if cpf.validaCPF(some_shit['input']):
                return 'OK'
            else:
                return 'Não'
    else:
        return "error"