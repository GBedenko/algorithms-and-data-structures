'''Graph of vertices data structure, with breadth-first and depth-first traversal algorithms'''

from Queue import Queue

# TODO: Use custom queue and stack objects in seperate files
# TODO: Separate folder: weighted_graph
# TODO: Separate folder: dijkstras_algorithm

class Vertex:
	"""Represents a Vertex within a Graph"""

	def __init__(self, value):
		'''Every vertex has a value and a list of its neighbour vertices'''

		self.value = value
		self.neighbours = []


	def add_neighbour(self, neighbour_value):
		'''Add another vertex as a neighbour of the selected vertex'''

		if neighbour_value not in self.neighbours:

			self.neighbours.append(neighbour_value)
			self.neighbours.sort()


class Graph:
	"""Graph is represented as a collection of Vertex objects in an adjacency matrix format"""


	def __init__(self):
		'''Graph has an adjacency list to save the vertices in a list
		   It has a list of vertices to save the vertices as the actual objects'''

		self.adjacency_list = []


	def add_vertex(self, vertex):
		'''Takes the vertex object as its input
		   Checks whether this vertex is already in the graph
		   If not add the object to the adjacency list'''

		if vertex not in self.adjacency_list:
			self.adjacency_list.append(vertex)


	def output_vertices(self):
		'''Iterates over the list of vertices and prints each one's
		   value and its neighbours'''

		for i in self.adjacency_list:
			print("Vertex " + str(i.value) + ": Neighbours: " + str(i.neighbours))
		print("\n")


	def find_vertex_by_value(self, vertex_value):
		'''Takes the value of a vertex and finds which vertex object it relates to
		   Performs a linear search checking the value variable of each vertex object
		   and comparing it to the input value'''

		# Search through all vertex object in the graph
		for i in self.adjacency_list:

			# If object with the right value variable is found, return it
			if i.value == vertex_value:
				return i

		# If not found, return null object, there isnt a vertex object with this value
		return None


	def breadth_first_traversal(self, starting_value):
		'''Breadth first traversal works by:
		   - Taking the first vertex and output all of its neighbours
		   - If more vertex's exist, move to the first of the neighbours
		   - Repeat by outputting all of the new vertex's neighbours
		   - Complete once all vertices are outputted'''

		queue = Queue() # Breadth first requires a queue structure

		visited = [] # List for the final output of visited vertices

		visited_all_vertices = False

		# Objects are added to the queue, so need to convert it from the value
		starting_vertex = self.find_vertex_by_value(starting_value)

		# Add first vertex's object to the queue
		queue.put(starting_vertex)

		# While there are still vertices to visit
		while not visited_all_vertices:

			new_vertex = queue.get() # Take the item from the front of the queue

			# If vertex hasn't been visited
			if new_vertex.value not in visited:

				visited.append(new_vertex.value) # Append it to visited vertices

				# If the length of visted vertices is same as number of vertices, all vertices have been visited
				if len(visited) == len(self.adjacency_list):
					visited_all_vertices = True

				# For every neighbour of the current vertex, add it to the queue
				for value in new_vertex.neighbours:

					# Find vertex object based on the neighbour's value
					found_vertex = self.find_vertex_by_value(value)

					# Add all the neighbours to the queue
					queue.put(found_vertex)

		return visited # Return list of visited vertices in the traversed order


	def depth_first_traversal(self, starting_value):
		'''Depth first traversal works by:
		   - Taking the first vertex and look at its first neighbour
		   - This vertex now becomes the current one and repeat for its neighbour
		   - Keep following the vertices one by one
		   - If it comes to a dead end you have to backtrack to find a new vertex
		   - Complete once all vertices are outputted'''

		stack = [] # Depth first requires a queue structure

		visited = [] # List for the final output of visited vertices

		visited_all_vertices = False

		# Objects are added to the stack, so need to convert it from the value
		starting_vertex = self.find_vertex_by_value(starting_value)

		# Add first vertex's object to the stack
		stack.append(starting_vertex)

		# While there are still vertices to visit
		while not visited_all_vertices:

			new_vertex = stack.pop() # Take the item from the top of the stack

			rightOrderOfNeighbours = new_vertex.neighbours
			rightOrderOfNeighbours.reverse()
			# The next neighbour it was looking for would be the wrong one so needed to
			# reverse the neighbours list so it picked the right one
			# e.g. Would go from 1 to 9 when 2 was the neighbour it should have picked

			# If vertex hasn't been visited
			if new_vertex.value not in visited:

				visited.append(new_vertex.value) # Append it to visited vertices

				# If the length of visted vertices is same as number of vertices, all vertices have been visited
				if len(visited) == len(self.adjacency_list):
					visited_all_vertices = True

				# For each neighbour of the current vertex, add it to the stack
				for value in rightOrderOfNeighbours:

					# Find vertex object based on the neighbour's value
					found_vertex = self.find_vertex_by_value(value)

					# Add all the neighbours to the queue
					stack.append(found_vertex)

		return visited # Return list of visited vertices in the traversed order


if __name__ == "__main__":

	graph = Graph()

	# Adds vertices to the graph with values 1 to 10
	for i in range(1, 11):

		graph.add_vertex(Vertex(i)) # The vertex object is created in the same
										# function for when it is added to the graph

	# List of edges for connections to be made for the graph
	edges_pairs_list = [(1,2), (1,3), (1,9),
						(2,3), (2,8),
						(3,4), (3,5), (3,9),
						(4,5), (4,7),
						(5,6),
						(6,10),
						(7,8),
						(9,10)
					]

	# Populate vertices with their neighbours
	for pair in edges_pairs_list:

		vertex_value, vertex_neighbour = pair # Split the edge pairs and save them to new variables
		vertex_object = graph.find_vertex_by_value(vertex_value) # Find the vertex object for the given value

		vertex_object.add_neighbour(vertex_neighbour) # For the vertex object, add the neighbour to it

 		# Same as above is done again but in reverse so the neighbours are added both ways
		vertex_neighbour_object = graph.find_vertex_by_value(vertex_neighbour) # Find the vertex object for the given value

		vertex_neighbour_object.add_neighbour(vertex_value) # For the vertex object, add the neighbour to it

	# Print the graph showing all vertices and neighbours stored as an adjacency list
	graph.output_vertices()

	breadth_first_output = graph.breadth_first_traversal(1) # Traverse the graph breadth-first
	print("Breadth-First Traversal: " + str(breadth_first_output))

	depth_first_output = graph.depth_first_traversal(1) # Traverse the graph depth-first
	print("Depth-First Traversal: " + str(depth_first_output))
