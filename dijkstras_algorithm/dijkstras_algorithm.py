"""Dijkstra's Algorithm"""

from weighted_graph import WeightedGraph
from weighted_graph import Vertex

from queue import Queue

class GraphWithDijkstras(WeightedGraph):
	"""GraphWithDijkstras"""


	def dijkstras_algorithm(self, start_node_value, target_node_value):

		nodes_distances = {} # Dictionary to store the best way to get to each
							 # node, the values will keep updating until it
							 # is the best way

		history = {}  # Dictionary to store which previous node to use for
					  # the shortest path

		start_weight = 5000 # Equivalent to setting start distance between nodes to infinity

		# For every node, set the 'best way' as infinity/big number and this will
		# be updated once accurate results are worked out
		for nodes in self.adjacency_list:

			nodes_distances[nodes.value] = start_weight

			history[nodes.value] = None

		# Start node gets set to zero as there is no cost/distance to get to the start
		nodes_distances[start_node_value] = 0

		queue = Queue()

		# Find the node object based on the input value
		start_vertex_object = self.find_vertex_by_value(start_node_value)

		# Add the start node onto the queue
		queue.enqueue(start_vertex_object)

		# While there is an object on the queue
		while queue.size() != 0:

			# Take the node from the front of the queue
			current_vertex = queue.dequeue()

			# Retrieve the node's value attribute
			current_vertex_value = current_vertex.value

			# For all of the neighbours of the current node
			for i in current_vertex.neighbours:

				# The new distance is weight to neighbour plus current one already saved
				current_vertex_distance = i[1] + nodes_distances[current_vertex_value] # i[1] = weight part of neighbour list

				# If the new distance is shorter than the existing one, then replace it
				if current_vertex_distance < nodes_distances[i[0]]:

					# Update the cost for the new distance
					nodes_distances[i[0]] = current_vertex_distance

					# Update the history to say where it came from
					history[i[0]] = current_vertex_value

					# Work out the node object for the next value
					vertex_object = self.find_vertex_by_value(i[0])

					# Add the next node to the queue
					queue.enqueue(vertex_object)

		path = [] # List to save the best path to

		# Work out the best path found starting from target and 'travel' to start
		comparison_node = target_node_value

		# Check all nodes for their history value
		while comparison_node is not None:

			path.append(comparison_node) # Append current node to the path

			comparison_node = history[comparison_node] # Next node to check is the node stated in history

		# The path is worked out from end to start, so reverse it when displaying it
		path.reverse()

		print("Shortest path between these nodes is: " + str(path))
		print("The distance of this path is: " + str(nodes_distances[target_node_value]))


if __name__ == "__main__":

	graph = GraphWithDijkstras()

	# Adds vertices to the graph with values 1 to 10
	for i in range(1, 11):

		graph.add_vertex(Vertex(i)) # The vertex object is created in the same
										# function for when it is added to the graph

	# List of edges for connections to be made for the graph (Vertex_value_1, Vertex_value_2, Weight_between_vertices)
	edges_weights_pairs_list = [(1,2,3), (1,3,5), (1,9,8),
								(2,3,4), (2,8,1),
								(3,4,2), (3,5,9), (3,9,4),
								(4,5,6), (4,7,7),
								(5,6,8),
								(6,10,2),
								(7,8,5),
								(9,10,1)
							]

	# Populate vertices with their neighbours
	for pair in edges_weights_pairs_list:

		vertex_value, vertex_neighbour, weight = pair # Split the edge pairs and save them to new variables
		vertex_object = graph.find_vertex_by_value(vertex_value) # Find the vertex object for the given value
		vertex_object.add_neighbour(vertex_neighbour, weight) # For the vertex object, add the neighbour to it

 		# Same as above is done again but in reverse so the neighbours are added both ways
		vertex_neighbour_object = graph.find_vertex_by_value(vertex_neighbour) # Find the vertex object for the given value
		vertex_neighbour_object.add_neighbour(vertex_value, weight) # For the vertex object, add the neighbour to it

	graph.output_vertices()

	# Run dijkstra's algorithm for user input
	start_point = int(input("Enter a node to start at: "))
	end_point = int(input("Enter a target node to finish at: "))
	print(" ")
	graph.dijkstras_algorithm(start_point, end_point)
