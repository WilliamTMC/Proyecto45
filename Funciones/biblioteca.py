import json#Sirve para trabajar con datos en formato .json
import matplotlib.pyplot as plt#Sirve para graficar
import numpy as np#Sirve para manejar y calcular datos numéricos de manera rápida
import datetime  #Sirve para trabajar con fechas y horas de manera precisa y flexible. 

#Funciones:
def open_json(direccion):
    with open(direccion,"r",encoding="utf-8") as file :
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

def obtener_nombres_y_precios(contenido:list):
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

def costo_promedio_producto(d:dict,lista_nombres:list):
    diccionario = {}
    for nombre in lista_nombres:  
        precios = d[nombre]  
        promedio_precio = round(promedio(precios))  
        diccionario[nombre] = promedio_precio 
    return diccionario
    
def verificar_existencia(diccionario:dict,lista:list,destino_nombre:list,destino_valor:list):
    for nombre in lista:
        for valor in diccionario["Productos"]:
            if valor["nombre"] == nombre:
                destino_nombre.append(valor['nombre'])
                destino_valor.append(valor['precio'])
                
#Graficos:    

def grafico_pastel(lista_valores:list,lista_nombres:list):
    plt.figure(figsize=(8, 8))
    plt.pie(lista_valores, labels=lista_nombres, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
            
                
def grafico_radar(d:dict):
    #Accedo a los nombres y valores del llaves del diccionario
    nombres = list(d.keys())
    valores = list(d.values())
    #Verifico la cantidad de nombres que hay 
    num_vars = len(nombres)
    #Genero una lista de ángulos uniformemente distribuidos en el círculo
    angulos = np.linspace(0, 2*np.pi, num_vars, endpoint=False).tolist()
    #Aclaraciones
    #0 angulo inicial (0 radianes).
    #2*np.pi  angulo final (un círculo completo = 360° en radianes).
    #num_vars cantidad de divisiones (tantos angulos como productos).
    #endpoint=False evita incluir el angulo final (2π), porque al cerrar el grafico se añade manualmente.
    #.tolist() convierte el resultado en una lista
    valores += valores[:1]#radios de la figura
    angulos += angulos[:1]#posiciones angulares de la figura 
    #Grafico
    fig, ax = plt.subplots(figsize=(7,8), subplot_kw=dict(polar=True))
    ax.plot(angulos, valores,'o', color='darkgreen', linewidth=2)
    ax.fill(angulos, valores, color='lightgreen', alpha=0.4)
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(nombres, fontsize=7)
    ax.set_title("Valor promedio de precios de los 10 productos más repetidos entre Mipymes", y=1.1)
    plt.show()
                
def grafico_tiendas(lista_nombres1:list,preciosl1:list,lista_nombres2:list,preciosl2:list):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    x1 = np.arange(len(lista_nombres1))
    x2 = np.arange(len(lista_nombres2))
    #Grafico de la primera tienda
    ax1.bar(x1, preciosl1, color='skyblue')
    ax1.set_title("Precios en Tienda MLC")
    ax1.set_xlabel("Nombre de productos")
    ax1.set_ylabel("Precio en MLC")
    ax1.set_xticks(x1)
    ax1.set_xticklabels(lista_nombres1, rotation=45, ha='right')
    #Grafico de la segunda tienda
    ax2.bar(x2, preciosl2, color='lightgreen')
    ax2.set_title("Precios en Tienda USD")
    ax2.set_xlabel("Nombre de productos")
    ax2.set_ylabel("Precio en USD")
    ax2.set_xticks(x2)
    ax2.set_xticklabels(lista_nombres2, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
def grafico_linea(lista_fechas:list,lista_valoresmlc:list,lista_valoresusd:list):
    #Convierto las fechas y ordenar todo
    fechas_convertidas = [datetime.datetime.strptime(f, "%d/%m/%y") for f in lista_fechas]
    datos = list(zip(fechas_convertidas, lista_valoresmlc, lista_valoresusd))
    datos.sort()#Ordeno por fecha
    #Aclaraciones
    #datetime.strptime convierte un texto (string) que representa una fecha en un objeto de tipo datetime que Python puede entender y manipular.

    #Separo los datos ya ordenados
    fechas_ordenadas = [d[0] for d in datos]
    mlc_ordenado = [d[1] for d in datos]
    usd_ordenado = [d[2] for d in datos]
    #Grafico
    plt.plot(fechas_ordenadas, mlc_ordenado, 'o-b', label='MLC')
    plt.plot(fechas_ordenadas, usd_ordenado, 's-g', label='USD')
    plt.title("Comportamiento del MLC y USD en el tiempo")
    plt.xlabel("Fecha de Actualización")
    plt.ylabel("Valor en CUP")
    plt.legend()
    plt.grid(True)
    #Uso las fechas originales como etiquetas
    plt.xticks(ticks=fechas_convertidas, labels=lista_fechas, rotation=45)
    plt.tight_layout()
    plt.show()
    
def grafico_comparacion_precios_tiendas(lista_nombres:list,lista_preciosmlc_cup:list,lista_preciosusd_cup:list):
    
    #Posiciones para las barras agrupadas
    x = np.arange(len(lista_nombres))
    #Aclaraciones
    #np.arange(len(nombre_productosmlc))genera un array de NumPy con valores enteros desde 0 hasta el len(nombre_productosmlc) sin incluir el ultimo valor
    #x es un array que representa las posiciones de cada producto en el eje X del gráfico,es decir, cada número corresponde a un producto en tu lista
    #Grafico
    ancho = 0.35  # ancho de cada barra
    fig, ax = plt.subplots(figsize=(12, 6))
    barras_mlc = ax.bar(x - ancho/2, lista_preciosmlc_cup, width=ancho, label='MLC en CUP', color='skyblue')
    barras_usd = ax.bar(x + ancho/2, lista_preciosusd_cup, width=ancho, label='USD en CUP', color='lightgreen')
    #Etiquetas encima de cada barra
    for i in range(len(x)):
        ax.text(x[i] - ancho/2, lista_preciosmlc_cup[i] + 5, str(lista_preciosmlc_cup[i]), ha='center', fontsize=9)
        ax.text(x[i] + ancho/2, lista_preciosusd_cup[i] + 5, str(lista_preciosusd_cup[i]), ha='center', fontsize=9)
    #Etiquetas y título
    ax.set_title("Comparación de precios en CUP desde MLC y USD")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Precio en CUP")
    ax.set_xticks(x)
    ax.set_xticklabels(lista_nombres, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    plt.show()
    
def grafico_tienda_vs_mipymes(lista_nombres:list,lista_preciosmlc_cup:list,lista_preciosusd_cup:list,lista_preciosmipymes):
    
    x = np.arange(len(lista_nombres))
    ancho = 0.25
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar(x - ancho, lista_preciosmlc_cup, width=ancho, label='MLC en CUP', color='skyblue')
    ax.bar(x, lista_preciosusd_cup, width=ancho, label='USD en CUP', color='lightgreen')
    ax.bar(x + ancho, lista_preciosmipymes, width=ancho, label='Mipymes en CUP', color='salmon')
    #Etiquetas encima de cada barra
    for i in range(len(x)):
        # MLC
            ax.text(x[i] - ancho, lista_preciosmlc_cup[i] + 5, f"${lista_preciosmlc_cup[i]}", ha='center', fontsize=8)
        # USD
            ax.text(x[i], lista_preciosusd_cup[i] + 5, f"${lista_preciosusd_cup[i]}", ha='center', fontsize=8)
        # Mipymes
            ax.text(x[i] + ancho, lista_preciosmipymes[i] + 5, f"${lista_preciosmipymes[i]}", ha='center', fontsize=8)
    #Personalizacion
    ax.set_title("Comparación de precios en CUP entre MLC, USD y Mipymes")
    ax.set_xlabel("Productos")
    ax.set_ylabel("Precio en CUP")
    ax.set_xticks(x)
    ax.set_xticklabels(lista_nombres, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    plt.show()

def grafico_precio_canastas(salario:int,precio_canasta1:int,precio_canasta2:int):
    #Calculo de sobrante o déficit
    sobrante1 = max(salario - precio_canasta1, 0)
    deficit1 = max(precio_canasta1 - salario, 0)
    sobrante2 = max(salario - precio_canasta2, 0)
    deficit2 = max(precio_canasta2 - salario, 0)

    #Preparar valores para stacked bar
    labels = ['Canasta 1', 'Canasta 2']
    gastos = [min(precio_canasta1, salario), min(precio_canasta2, salario)]
    sobrantes = [sobrante1, sobrante2]
    deficits = [deficit1, deficit2]

    #Grafico
    fig, ax = plt.subplots(figsize=(8,6))
    #Barras de gasto
    barras_gasto = ax.bar(labels, gastos, color='beige', label='Gasto en canasta')
    #Barras de sobrante
    barras_sobrante = ax.bar(labels, sobrantes, bottom=gastos, color='green', label='Sobrante')
    #Barras de déficit
    barras_deficit = ax.bar(labels, deficits, bottom=gastos, color='red', label='Déficit')
    #Linea de referencia del salario
    ax.axhline(salario, color='gray', linestyle='--', linewidth=1, label='Salario mínimo')
    # Texto sobre la linea
    ax.text(1.05, salario + 50, f"{salario} CUP", color='gray', fontsize=10, va='bottom')
    #Etiquetas en cada segmento
    for i in range(len(labels)):
        #Gasto
        ax.text(i, gastos[i] / 2, f"{gastos[i]} CUP", ha='center', va='center', fontsize=9, color='black')
        #Sobrante
        if sobrantes[i] > 0:
            ax.text(i, gastos[i] + sobrantes[i]/2, f"+{sobrantes[i]} CUP", ha='center', va='center', fontsize=9, color='black')
        #Deficit
        if deficits[i] > 0:
            ax.text(i, gastos[i] + deficits[i]/2, f"-{deficits[i]} CUP", ha='center', va='center', fontsize=9, color='black')
    #Personalizacion
    ax.set_ylabel("Valor de cada canasta en (CUP)")
    ax.set_title("Comparación entre salario mínimo y precio de canastas básicas")
    ax.legend()
    plt.tight_layout()
    plt.show()
    
def grafico_frecuencia_compra(lista_nombres:list,cantidad_compras:list):
    
    #Grafico
    plt.figure(figsize=(10,6))
    plt.scatter(lista_nombres, cantidad_compras, color='dodgerblue', s=100)
    #Etiquetas encima de cada punto
    for i, cantidad in enumerate(cantidad_compras):
        plt.text(i, cantidad + 0.3, str(cantidad), ha='center', va='bottom', fontsize=9)
    #Personalizacion
    plt.title("Cantidad de veces que puedo comprar cada producto con 2100 CUP")
    plt.ylabel("Cantidad de compras ")
    plt.ylim(0, max(cantidad_compras) + 2)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def grafico_analisis_producto(salario:int,nombre_producto:str,precio_producto:int):
    
    #Calculo los meses necesarios (redondeado hacia arriba)
    meses_necesarios = round(precio_producto / salario)
    #Grafico
    plt.figure(figsize=(3,5))
    barra = plt.bar([nombre_producto], [meses_necesarios], color='tomato')
    #Etiqueta encima de la barra
    plt.text(0, meses_necesarios + 0.1, f"{meses_necesarios} meses", ha='center', va='bottom', fontsize=8)
    #Personalizacion
    plt.title(f"Meses necesarios para comprar {nombre_producto}",fontsize=9)
    plt.ylabel("Meses de salario mínimo")
    plt.ylim(0, meses_necesarios + 2)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
    
def grafco_salario_mensual(salario:int,salario_en_mlc:int,salario_en_usd:int):
  
    #Preparo los  datos
    monedas = ['CUP', 'MLC', 'USD']
    valores = [salario, salario_en_mlc, salario_en_usd]
    colores = ['gold', 'mediumseagreen', 'dodgerblue']
    #Grafico
    plt.figure(figsize=(8,6))
    barras = plt.bar(monedas, valores, color=colores)
    #Etiquetas encima de cada barra
    for i, valor in enumerate(valores):
        plt.text(i, valor + salario * 0.02, f"${valor}", ha='center', va='bottom', fontsize=10)
    #Personalizacion
    plt.title("Equivalente del salario mínimo en CUP, MLC y USD mensualmente")
    plt.ylabel("Valor monetario")
    plt.ylim(0, salario + 200)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    #Anotacion
    plt.text(1.5, salario * 0.6,
             "MLC y USD son conversiones aproximadas\nsegún tasas recientes de cambio",
             ha='center', fontsize=9, color='gray')
    plt.tight_layout()
    plt.show()
    
def grafco_salario_anual(salario:int,salario_en_mlc:int,salario_en_usd:int):
  
    #Preparo los  datos
    monedas = ['CUP', 'MLC', 'USD']
    valores = [salario, salario_en_mlc, salario_en_usd]
    colores = ['gold', 'mediumseagreen', 'dodgerblue']
    #Grafico
    plt.figure(figsize=(8,6))
    barras = plt.bar(monedas, valores, color=colores)
    #Etiquetas encima de cada barra
    for i, valor in enumerate(valores):
        plt.text(i, valor + valor * 0.05, f"{valor}", ha='center', va='bottom', fontsize=10)
    #Personalizacion
    plt.title("Equivalente del salario mínimo en CUP, MLC y USD anualmente")
    plt.ylabel("Valor monetario")
    plt.ylim(0, max(valores) * 1.2)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    #Anotacion
    plt.text(1.5, salario * 0.6,
             "MLC y USD son conversiones aproximadas\nsegún tasas recientes de cambio",
             ha='center', fontsize=9, color='gray')
    plt.tight_layout()
    plt.show()


