import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def crear_grafo():
    G = nx.Graph()
    estados = [
        "CDMX", "Estado de México", "Puebla", "Morelos", "Guerrero", "Querétaro", "Hidalgo"
    ]
    conexiones = [
        ("CDMX", "Estado de México", 50),
        ("CDMX", "Puebla", 130),
        ("CDMX", "Morelos", 90),
        ("Estado de México", "Querétaro", 180),
        ("Estado de México", "Hidalgo", 80),
        ("Puebla", "Guerrero", 250),
        ("Morelos", "Guerrero", 150),
        ("Querétaro", "Hidalgo", 100),
        ("Hidalgo", "Puebla", 120)
    ]
    
    for estado in estados:
        G.add_node(estado)
    
    for e1, e2, costo in conexiones:
        G.add_edge(e1, e2, weight=costo)
    
    return G

def camino_mas_corto(G):
    min_costo = float('inf')
    mejor_camino = []
    
    for perm in permutations(G.nodes):
        costo = 0
        valido = True
        for i in range(len(perm) - 1):
            if G.has_edge(perm[i], perm[i+1]):
                costo += G[perm[i]][perm[i+1]]['weight']
            else:
                valido = False
                break
        
        if valido and costo < min_costo:
            min_costo = costo
            mejor_camino = perm
    
    return mejor_camino, min_costo

def camino_con_repeticiones(G):
    mst = nx.minimum_spanning_tree(G, weight='weight')
    mst_edges = list(mst.edges(data=True))
    total_costo = sum(edge[2]['weight'] for edge in mst_edges) * 2
    recorrido = list(G.nodes) + [G.nodes[0]]
    return recorrido, total_costo

def dibujar_grafo(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Crear y mostrar el grafo
G = crear_grafo()
dibujar_grafo(G)

# Resolver inciso a)
camino, costo = camino_mas_corto(G)
print("Recorrido sin repetir estados:", " -> ".join(camino))
print("Costo total del recorrido:", costo)

# Resolver inciso b)
camino_rep, costo_rep = camino_con_repeticiones(G)
print("Recorrido repitiendo al menos un estado:", " -> ".join(camino_rep))
print("Costo total del recorrido:", costo_rep)
