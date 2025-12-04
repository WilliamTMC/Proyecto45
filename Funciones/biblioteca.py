import json
def open_json(path):
    with open(path,"r",encoding="utf-8") as file :
        read = json.loads(file.read())
    return read

def suma(l:list):
    suma = 0
    for i in l:
        suma += i 
    return suma

def promedio(l:list):
    s = suma(l)
    p = s/len(l)
    return p

def convertir(n:int,m:int):
    con = n * m 
    return round(con)

def valores_repetidos(l:list):
    repetidos = []
    for elemento in l:
        if l.count(elemento) > 1 and elemento not in repetidos:
            repetidos.append(elemento)
    return repetidos