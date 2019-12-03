from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #Number of vertices 
		self.graph = [] # default dictionary to store graph 
		
	def addEdge(self,u,v,w): #Adds an edge 
		self.graph.append([u,v,w]) 

	def find(self, parent, i): #finds a vertex 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	def union(self, parent, rank, x, y): #union set 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	def KruskalMST(self): 

		list = [] #list

		i = 0 
		e = 0

		self.graph = sorted(self.graph,key=lambda item: item[2]) # order all edges in non ascedning order by weight #copy of graph 

		parent = [] ; rank = [] 

		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		while e < self.V -1 : #edges is equal to number of V-1

			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			if x != y:  #if edge doesnt make cycle then add it to list 
				e = e + 1	
				list.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge 

		print ("Kruskal's Algorithm: ")
		for u,v,weight in list: 
			print ("Vertex %d to Vertex %d with a weight of  %d" % (u,v,weight)) 

# Homework Graph 
g = Graph(9)
g.addEdge(0, 1, 4) 
g.addEdge(0, 4, 3) 
g.addEdge(1, 4, 2) 
g.addEdge(1, 5, 5) 
g.addEdge(1, 2, 4) 
g.addEdge(2, 5, 6)
g.addEdge(2, 6, 9)
g.addEdge(3, 6, 13)
g.addEdge(4, 7, 1)
g.addEdge(4, 5, 12)
g.addEdge(5, 7, 21)
g.addEdge(7, 8, 14)
g.addEdge(5, 8, 11)
g.addEdge(5, 6, 17)
g.addEdge(6, 8, 10)
g.addEdge(8, 9, 16)
g.addEdge(3, 9, 20) 

g.KruskalMST() 