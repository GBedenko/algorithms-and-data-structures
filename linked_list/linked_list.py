'''Linked List with insert, search and delete functionalities'''


class Node(object):

	def __init__(self, value):
		'''Every node has a value, pointer to the next node, pointer to the previous node'''
		self.value=value
		self.next=None
		self.prev=None


class List(object):


	def __init__(self):
		'''The list has a start and end, i.e. head and tail'''
		self.head=None
		self.tail=None


	def insert(self, node, prev_node):
		'''Insert function adds a node to the linked list'''

		# If there is a previous node
		if prev_node != None:

			node.next = prev_node.next # Node points where the prev node is pointing
			prev_node.next = node      # Previous node's next node is pointing to the node
			node.prev = prev_node      # Node points to previous node

			# If there is a next node
			if node.next != None:

				node.next.prev = node # The next node's previous pointer points to the new node

		# If there is no node at the head
		if self.head == None:

			self.head = self.tail = node # The start and end of the list is the single node

			node.prev = node.next= None # There is no next or previous node

		# If the previous node is the last node
		elif self.tail == prev_node:

			self.tail = node # The new node is now the tail node


	def display(self):
		'''Display function prints out the linked list'''

		values=[]
		n = self.head

		# Loop through all nodes in the linked list
		while n != None:
			values.append(str(n.value))
			n=n.next

		print("List: " + ",".join(values))


	def search(self, value):
		'''Function that searches through the linked list to find a node
		   with the input value
		   Returns the node object for the node of that value'''

		# If the head node is empty, there is an empty linked list so return None
		if self.head == None:
			return None

		current_node = self.head # Start comparing from the head node

		# Loop keeps going while there is a next node to look at
		while current_node.next != None:

			# If the node's value is the one looking for, return the node object
			if current_node.value == value:
					return current_node

			# Otherwise, move to the next node
			current_node = current_node.next

		# If there isn't a next node, but it's the last node, do one final check
		# after the loop has ended for the last node, return if it is one looking for
		if current_node.value == value:
			return current_node


	def delete(self, number):
		'''Deleting a node is done by changing the links between nodes
		   Searches for the node you want to delete
		   The link from the previous node now points to the node after
		   The link from the next node now points to the node before'''

		node = self.search(number)

		# If the node doesn't have a previous node
		if node.prev == None:

			# The previous node points to the node next to the input node
			node.prev.next = node.next

		# If the node doesn't have a next node
		elif node.next == None:

			# The next node points to the node previous to the input node
			node.next.prev = node.next

		# The node is a normal case (inbetween two other nodes)
		else:
			node.prev.next = node.next
			node.next.prev = node.prev


if __name__ == '__main__':

	# Create a new linked list with two nodes
	l = List()
	l.insert(Node(4), None)
	l.display()
	l.insert(Node(6), l.head)
	l.display()

	# Insert new nodes
	new_node = Node(8)
	l.insert(new_node, l.head) # Insert so that node is after the head
	l.display()
	l.insert(Node(12), new_node) # Insert so that node is after the node just inserted
	l.display()

	# Delete new nodes
	l.delete(12)
	l.display()
	l.delete(8)
	l.display()
