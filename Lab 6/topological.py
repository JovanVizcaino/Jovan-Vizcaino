from collections import defaultdict 

class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #Number of vertices 

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self,v,visited,stack): 

		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of stack 
		print(stack) 

g = Graph(9) 
g.addEdge(0, 1) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(7, 4) 
g.addEdge(5, 4) 
g.addEdge(5, 7) 
g.addEdge(8, 7) 
g.addEdge(8, 5) 
g.addEdge(5, 1) 
g.addEdge(2, 1) 
g.addEdge(2, 3) 
g.addEdge(5, 2) 
g.addEdge(6, 2) 
g.addEdge(6, 3) 
g.addEdge(6, 5) 
g.addEdge(6, 8) 
g.addEdge(3, 1) 

g.topologicalSort() 

