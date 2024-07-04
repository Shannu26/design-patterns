from abc import ABC, abstractmethod
from collections import deque

class TreeNode:
	def __init__(self, value: int):
		self.value = value
		self.left = None
		self.right = None

class Iterator(ABC):
	@abstractmethod
	def __next__(self):
		pass

	@abstractmethod
	def __iter__(self):
		pass

# DFS Iterator (using in-order traversal)
class DFSIterator(Iterator):
	def __init__(self, root: TreeNode):
		self.stack = []
		self._push_left(root)

	def _push_left(self, node: TreeNode):
		while node:
			self.stack.append(node)
			node = node.left

	def __iter__(self):
		return self

	def __next__(self):
		if not self.stack:
			raise StopIteration
		node = self.stack.pop()
		result = node.value
		if node.right:
			self._push_left(node.right)
		return result

# BFS Iterator
class BFSIterator(Iterator):
	def __init__(self, root: TreeNode):
		self.queue = deque()
		if root:
			self.queue.append(root)

	def __iter__(self):
		return self

	def __next__(self):
		if not self.queue:
			raise StopIteration
		node = self.queue.popleft()
		result = node.value
		if node.left:
			self.queue.append(node.left)
		if node.right:
			self.queue.append(node.right)
		return result

class BinaryTree:
	def __init__(self, root: TreeNode = None):
		self.root = root

	def create_dfs_iterator(self):
		return DFSIterator(self.root)

	def create_bfs_iterator(self):
		return BFSIterator(self.root)

# Helper function to add nodes to the tree
def add_node(root, value):
	if root is None:
		return TreeNode(value)
	if value < root.value:
		root.left = add_node(root.left, value)
	else:
		root.right = add_node(root.right, value)
	return root

# Usage
if __name__ == "__main__":
	# Create a binary tree
	values = [7, 3, 9, 1, 5, 8, 10]
	tree = BinaryTree()
	for value in values:
		tree.root = add_node(tree.root, value)

	# Create a DFS iterator for the tree
	print("DFS Traversal:")
	dfs_iterator = tree.create_dfs_iterator()
	for value in dfs_iterator:
		print(value, end=" ")  # Output: 1 3 5 7 8 9 10
	print()

	# Create a BFS iterator for the tree
	print("BFS Traversal:")
	bfs_iterator = tree.create_bfs_iterator()
	for value in bfs_iterator:
		print(value, end=" ")  # Output: 7 3 9 1 5 8 10
	print()