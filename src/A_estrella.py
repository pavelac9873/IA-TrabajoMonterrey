import heapq
def a_star(grafo, origen, destino, heuristica):
    abiertos=[]
    cerrados=set()
    g = {origen:0}
    padres={}
    expandidas=[]
    encontrado=False
    contador=0
    f={}
    f[origen]=g[origen] + heuristica.get(origen)
    heapq.heappush(abiertos,(f[origen],origen))
    while abiertos and not encontrado:
        f_actual, actual=heapq.heappop(abiertos)
        if actual not in cerrados:
            if actual == destino:
                encontrado=True
            else:
                cerrados.add(actual)
                expandidas.append({'estacion':actual, 'f':f_actual  , 'g':g[actual], 'h':heuristica.get(actual),'orden':contador})
                for vecino,coste in grafo[actual].items():
                    nuevo_g=g[actual] + coste
                    if nuevo_g < g.get(vecino,float('inf')):
                        padres[vecino]=actual
                        g[vecino]=nuevo_g
                        f[vecino]=nuevo_g+heuristica.get(vecino)
                        heapq.heappush(abiertos,(f[vecino],vecino))    
                contador=contador+1

    ruta=[]
    if encontrado:
        nodo=destino
        ruta.append(nodo)
        while nodo in padres:
            nodo=padres[nodo]
            ruta.append(nodo)
        ruta.reverse()
        coste_total=g[destino]     
    else:
        coste_total=float('inf')           

    return ruta, coste_total, expandidas

# ==========================================
# PRUEBA 1: ESTACIÓN EXISTENTE PERO AISLADA
# ==========================================

grafo1 = {
    "Origen": {
        "A": 2
    },
    "A": {
        "Origen": 2
    },
    "Aislada": {}
}

h1 = {
    "Origen": 0,
    "A": 0,
    "Aislada": 0
}

print("\n========== PRUEBA 1 ==========")

ruta1, coste1, expandidas1 = a_star(
    grafo1, "Origen", "Aislada", h1
)

print("Ruta:", ruta1)
print("Coste:", coste1)
print("Expandidas:", expandidas1)

assert ruta1 == []
assert coste1 == float('inf')

print("PRUEBA 1 SUPERADA")


# ==========================================
# PRUEBA 2: DUPLICADOS EN HEAPQ
# ==========================================

grafo2 = {
    "Inicio": {
        "C": 10,
        "B": 1
    },
    "B": {
        "Inicio": 1,
        "C": 2
    },
    "C": {
        "Inicio": 10,
        "B": 2,
        "Destino": 100
    },
    "Destino": {
        "C": 100
    }
}

h2 = {
    "Inicio": 0,
    "B": 0,
    "C": 0,
    "Destino": 0
}

print("\n========== PRUEBA 2 ==========")

ruta2, coste2, expandidas2 = a_star(
    grafo2, "Inicio", "Destino", h2
)

print("Ruta:", ruta2)
print("Coste:", coste2)
print("Expandidas:", expandidas2)

assert ruta2 == ["Inicio", "B", "C", "Destino"]
assert coste2 == 103

nombres2 = [e["estacion"] for e in expandidas2]

assert nombres2.count("C") == 1

print("PRUEBA 2 SUPERADA")


# ==========================================
# PRUEBA 3: ORIGEN IGUAL A DESTINO
# ==========================================

grafo3 = {
    "Sol_L1": {
        "Gran_Via_L1": 3
    },
    "Gran_Via_L1": {
        "Sol_L1": 3
    }
}

h3 = {
    "Sol_L1": 0,
    "Gran_Via_L1": 0
}

print("\n========== PRUEBA 3 ==========")

ruta3, coste3, expandidas3 = a_star(
    grafo3, "Sol_L1", "Sol_L1", h3
)

print("Ruta:", ruta3)
print("Coste:", coste3)
print("Expandidas:", expandidas3)

assert ruta3 == ["Sol_L1"]
assert coste3 == 0
assert expandidas3 == []

print("PRUEBA 3 SUPERADA")


# ==========================================
# RESULTADO FINAL
# ==========================================

print("\n================================")
print("¡LAS TRES PRUEBAS HAN TERMINADO!")
print("================================")