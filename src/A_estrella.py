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