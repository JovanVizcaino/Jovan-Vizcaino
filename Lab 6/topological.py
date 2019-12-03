from collections import defaultdict 

class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) #dictionary containing adjacency List 
		self.V = vertices #Number of vertices 

	def addEdge(self,u,v): #Adds edges 
		self.graph[u].append(v) 

	def topologicalSortUtil(self,v,visited,stack): #Toplogical Sorting 

		visited[v] = True #When tracing defualt is False but replaces with True when visited 

		for i in self.graph[v]: #If the index is false meaning hasnt been visted it gets visted and passes through 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		stack.insert(0,v) 

	def topologicalSort(self): 
		visited = [False]*self.V #sets all vertex as false until visited 
		stack =[] #stack 

		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		print(stack) #prints the stack in topological sort

# Graph from homework exercises 
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

