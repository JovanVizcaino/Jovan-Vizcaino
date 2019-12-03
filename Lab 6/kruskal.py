from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #Number of vertices 
		self.graph = [] # default dictionary to store graph 
		
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	def union(self, parent, rank, x, y): 
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

		result =[] #This will store the resultant MST 

		i = 0 # An index variable, used for sorted edges 
		e = 0 # An index variable, used for result[] 

			# 1: Sort all the edges in non-decreasing 
				# order of their 
				# weight. If we are not allowed to change the 
				# given graph, we can create a copy of graph 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 

		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		# Number of edges to be taken is equal to V-1 
		while e < self.V -1 : 

			# 2: Pick the smallest edge and increment 
					# the index for next iteration 
			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			# If including this edge does't cause cycle, 
						# include it in result and increment the index 
						# of result for next edge 
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge 

		print ("Kruskal's Algorithm: ")
		for u,v,weight in result: 
			print ("%d -> %d = %d" % (u,v,weight)) 

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

