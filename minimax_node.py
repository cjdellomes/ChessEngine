class minimax_node:

	def __init__(self, value = None, player = None, children = []):
		self.value = value
		self.player = player
		self.children = children

	def __str__(self):
		return self.value

	def __lt__(self, other):
		return self.value < other.value

	def __gt__(self, other):
		return self.value > other.value

	def insert_children(self, children):
		self.children.extend(children)

	def remove_children(self, children):
		for c in children:
			self.children.remove(c)