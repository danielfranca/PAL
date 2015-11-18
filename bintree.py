#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Node(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def add_child(self, node):
		if node.data > self.data:
			if self.right:
				self.right.add_child(node)
			else:
				self.right = node
		else:
			if self.left:
				self.left.add_child(node)
			else:
				self.left = node


class BinTree(object):

	root = None

	def add_data(self, data):
		node = Node(data)
		if self.root is None:
			self.root = node
		elif self.root:
			self.root.add_child(node)

	def find_data(self, data, node=None):
		if node is None or node.data == data:
			return node

		if data > node.data:
			return self.find_data(data, node.right)
		else:
			return self.find_data(data, node.left)


def test():
	bTree = BinTree()

	bTree.add_data(5)
	bTree.add_data(2)
	bTree.add_data(3)
	bTree.add_data(0)

	node = bTree.find_data(10)
	assert node is None

	node = bTree.find_data(100)
	assert node is None

	node = bTree.find_data(5, bTree.root)
	assert node.data == 5

	node = bTree.find_data(2, bTree.root)
	assert node.data == 2

	node = bTree.find_data(0, bTree.root)
	assert node.data == 0

	node = bTree.find_data(3, bTree.root)
	assert node.data == 3

	print('All tests passed')


if __name__ == '__main__':
	test()