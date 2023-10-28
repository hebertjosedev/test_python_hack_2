"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""
    

def fn_hack_1(palabra):
    if len(palabra) < 3:return palabra
    palabra = list(palabra)
    rango_inicial= 1
    pivote = rango_inicial
    for k in range(len(palabra)):
        if rango_inicial == 0:
            palabra[k] = palabra[k].upper()
            rango_inicial = pivote + 1
            pivote = rango_inicial
        else:
            rango_inicial -=1

    return ("".join(palabra))
    
    