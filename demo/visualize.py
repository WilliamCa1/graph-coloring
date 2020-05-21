import networkx as nx
import matplotlib.pyplot as plt

n = len([float(l.split()[1]) for l in open('tt.txt')])

file_read = open('tt.txt', 'r')
file_color = open('c.txt', 'r')

try:
     #Read adjacent matrix
     matrix = [[0 for x in range(n)] for y in range(n)]
     i = 0
     for line in file_read:
          matrix[i] = line.split(' ')
          i = i + 1
     
     #Create graph   
     G = nx.Graph()
     v = range(0, len(matrix))
     G.add_nodes_from(v)
     line = file_color.read()
     colors = (line.split(' '))
     for i in range(len(colors)):
          colors[i] = int(colors[i])
     for x in range(0, len(matrix)):
          for y in range(0, len(matrix)):
               if matrix[x][y] == '1':
                    G.add_edge(x, y)

     nx.draw(G, with_labels=True, node_color=colors) 
     plt.show()
finally:
     file_read.close()

