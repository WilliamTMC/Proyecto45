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

def convertir(a:int,b:int):
    resultado = a * b
    return round(resultado)

def nombres_sin_repetir(lista):
    nombres_vistos = []
    for nombre in lista:
        if nombre not in nombres_vistos:
            nombres_vistos.append(nombre)
    return nombres_vistos

