class TreeNode:
	def __init__(self,value):
		self.data=value
		self.left=None
		self.right=None

class Tree:
	def __init__(self):
		self.root=None

	def get_root(self):
		return self.root

	def insert(self,root,value):

		new_node=TreeNode(value)

		if root==None:
			root=new_node 
			return

		else:
			if node.data>val:
				if node.left!=None:
					self.insert(node.left,val)
				else:
					node.left=new_node
			else:
				if node.right!=None:
					self.insert(node.right,val)
				else:
					node.right=new_node



tree=Tree()
root=tree.get_root()
nums=[1,6,2,4,9,7,4,5,7,4,2,1]
for i in nums:
	tree.insert(root,i)