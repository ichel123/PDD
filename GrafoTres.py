import networkx as nx
import pylab

grafo = nx.DiGraph()

grafo.add_edges_from([('B', 'F'),('E','G'),('D','F')], costo=7)
grafo.add_edges_from([('A','D'),('F','G')], costo=6)
grafo.add_edges_from([('A','B')], costo=8)
grafo.add_edges_from([('A','C')], costo=3)
grafo.add_edges_from([('B','E')], costo=4)
grafo.add_edges_from([('D','E')], costo=9)
grafo.add_edges_from([('C','E')], costo=5)

solucion = [('A','C'),('C','E'),('E','G')]
color_aristas = ['black' if not arista in solucion else 'red' for arista in grafo.edges()]

valores = {
    'node_color': 'yellow',
    'node_size': 170,
    'width': 1,
    'arrowsize': 12
}

nx.draw_networkx(grafo, **valores,edge_color = color_aristas)
pylab.show()