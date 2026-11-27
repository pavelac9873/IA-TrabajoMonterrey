import heapq
def a_star(grafo:dict[str, dict[str, float]], origen:str, destino:str, heuristica:dict[str, float]) -> tuple[list[str], float, list[dict]]:
    """
    A* con cola de prioridad. Esta implemetación solo encuentra la ruta óptima si h es consistente
    grafo: dict {nodo: {vecino: coste_en_minutos}}
             Los costes ya incluyen el tiempo de transbordo en las aristas que conectan las dos versiones de una estación de transbordo.
    heuristica: dict {nodo: h(n)}
    Devuelve: (ruta, coste_total_minutos, expandidas),expandidas = [{orden, estacion, g, h, f}]
    """
    abiertos:list[tuple[float, str]] = []
    cerrados:set[str] = set()
    g:dict[str, float] = {origen: 0}
    padres:dict[str, str] = {}
    expandidas:list[dict] = []
    encontrado:bool=False
    contador:int=0
    f:dict[str, float] = {}
    f[origen]=g[origen] + heuristica.get(origen)
    heapq.heappush(abiertos,(f[origen],origen))
    while abiertos and not encontrado:
        f_actual, actual=heapq.heappop(abiertos)
        if actual not in cerrados:
            cerrados.add(actual)
            expandidas.append({'estacion':actual, 'f':f_actual  , 'g':g[actual], 'h':heuristica.get(actual),'orden':contador})
            contador=contador+1
            if actual == destino:
                encontrado=True
            else:
                for vecino,coste in grafo[actual].items():
                    nuevo_g=g[actual] + coste
                    if nuevo_g < g.get(vecino,float('inf')):
                        padres[vecino]=actual
                        g[vecino]=nuevo_g
                        f[vecino]=nuevo_g+heuristica.get(vecino)
                        heapq.heappush(abiertos,(f[vecino],vecino))    

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