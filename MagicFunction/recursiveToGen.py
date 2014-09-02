import pdb
class TreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
"""
def preorder(tree):
	yield tree.value
	if not tree.left is None:
		for subtree in preorder(tree.left):
			yield subtree
	if not tree.right is None:
		for subtree in preorder(tree.right):
			yield subtree
"""
class Solution:
    def preorder(self, node):
        if not node is None:
            yield node.value
        if not node.left is None:
            for subtree in self.preorder(node.left):
                yield subtree
        if not node.right is None:
            for subtree in self.preorder(node.right):
                yield subtree
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        return list(self.preorder(root))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

tree2 = TreeNode(1)

test = Solution()
print list(test.preorderTraversal(tree2))
