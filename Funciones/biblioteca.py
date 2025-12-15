import json
import matplotlib.pyplot as plt
import operator
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

def obtener_nombres_y_precios(contenido):
    productos = {}

    for item in contenido:
        for producto in item["Productos"]:
            nombre = producto["nombre"]
            precio = producto["precio"]
            if nombre not in productos:
                productos[nombre] = []
            productos[nombre].append(precio)
    
    return productos

def extraer_valores_de_cambio(contenido, moneda:str):
    valores = []
    for registro in contenido:
        for cambio in registro.get("Cambio", []):
            if cambio.get("nombre") == moneda:
                valores.append(cambio.get("valor"))
    return valores

def guardar_producto_lista(diccionario, producto, lista_destino):
    if producto in diccionario:
        lista_destino.append((producto, diccionario[producto]))

def acceder_precio_lista(l1:list,l2:list):
    for i in l1:
        l2.append(i[1])
    
def productos_comprables(diccionario:dict, presupuesto:int):
    comprables = []
    for producto, precio in diccionario.items():
        if precio <= presupuesto:
            cantidad = presupuesto // precio
            comprables.append((producto, precio, cantidad))
    return comprables

def convertir_mlc_usd(a:int,b:int):
    resultado = a / b
    return round(resultado)

def graficar_top_productos(productos_con_precios:dict):
    # Calcular frecuencia de cada producto
    frecuencia_de_productos = {
        nombre: len(precios)
        for nombre, precios in productos_con_precios.items()
    }

    # Ordenar por frecuencia descendente:
    #sorted sirve para ordenar elementos de una secuencia en este caso un diccionario y devuelve una lista con tuplas
    #operator.itemgetter(1) ordena la lista tomando en cuenta el segunda valor de cada tupla que seria el precio
    #reverse=True ordena en orden descentente de mayor a menor 
    frecuencia_ordenada = sorted(frecuencia_de_productos.items(),key=operator.itemgetter(1),reverse=True)

    # Tomar los 10 más frecuentes
    top_10_productos = frecuencia_ordenada[:10]#tomo los 10 primeros valores de la lista

    # Separar nombres y cantidades
    nombres = []#lista para almacenar los nombres de los productos
    cantidades = []#lista para almacenar las veces que se repete cada producto 
    for i in top_10_productos:#itero sobre la lista que contiene los 10 productos mas repetidos 
        nombre = i[0] #nombre va a tomar el primer valor de cada tupla que seria el nombre
        cantidad = i [1] #cantidad va a tomar el segundo valor de cada tupla que seria el len
        nombres.append(nombre)
        cantidades.append(cantidad)
        #agrego cada resultado a las listas creadas 

    # Graficar pastel
    plt.figure(figsize=(8, 8))#tamaño del grafico
    plt.pie(cantidades, labels=nombres, autopct='%1.1f%%', startangle=140)#creo un grafico de pastel
    #Aclaraciones:
    #cantidades serian los valores que irian dentro de cada porcion del pastel
    #labels seria los nombres de cada producto que irian afuera de cada porcion del pastel 
    #autopct='%1.1f%%' redondea cada resultado a un lugar despues de la coma 
    #startangle=140 rota el gráfico para que el primer sector comience a 140 grados desde el eje horizontal. Esto mejora la estética y evita que las etiquetas se amontonen.
    plt.title("Distribución de los 10 productos más repetidos en mipymes")#titulo del grafico
    plt.axis('equal')#hace que el gráfico se fuerce a ser perfectamente circular, lo que mejora la estética y la precisión visual.
    plt.tight_layout()#Ajusta automáticamente el diseño de la figura en Matplotlib para que los elementos (gráficos, títulos, etiquetas, leyendas) no se solapen ni queden cortados en la visualización
    plt.show()

    # Imprimir frecuencias y porcentajes
    total_apariciones = sum(cantidades) #Utilizo sum para sumar todos los valores de la lista cantidades 
    print("Productos más repetidos y sus frecuencias en 30 Mipymes:")
    for nombre, cantidad in zip(nombres, cantidades):#itero sobre las dos listas creadas que almacenan los nombres y el len de cada producto
        porcentaje = (cantidad / total_apariciones) * 100#declaro una variable para saber el porciento que representa cada repeticion 
        print(f"{nombre}: {cantidad} veces ({round(porcentaje, 1)}%)")#uso round para redondear el valor del prociento a un lugar despues de la coma
            
