def elefantes(n):
    if n <= 0: return ""
    if n == 1: return "Um elefante incomoda muita gente"
    else:
        return elefantes(n - 1) + '\n'+str(n) + ' elefantes ' + incomodam(n) +('muita mais') + '\n' + str(n) + ' elefantes incomodam muita gente'

def incomodam(n):
    if n <= 0: return ""
    if n == 1: return "incomodam "
    return "incomodam " + incomodam(n - 1)
