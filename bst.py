class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.parent= None
		self.val = key 
		
def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val), 
		printInorder(root.right) 
		
def printPostorder(root): 
	if root: 
		printPostorder(root.left) 
		printPostorder(root.right) 
		print(root.val), 
		
def printPreorder(root): 
	if root: 
		print(root.val), 
		printPreorder(root.left) 
		printPreorder(root.right)

def Tree_Search(root,sv): 
	if root is None or sv is root.val: 
		return root
	if sv<root.val: 
		return Tree_Search(root.left,sv)
	else:  
		return Tree_Search(root.right,sv)	

def min(root):
	while root.left is not None:
		root=root.left
	return root

def max(root):
	while root.right is not None:
		root=root.right
	return root		

def Tree_Succesor(root):
	if root.right is not None:
		return min(root.right)
	parnt=root.parent	
	while parnt is not None and root is parnt.right:
		root=parnt
		parnt=parnt.parent 
	return parnt 	

def Tree_Predecessor(root):
	if root.left is not None:
		return min(root.left)
	parnt=root.parent	
	while parnt is not None and root is parnt.left:
		root=parnt
		parnt=parnt.parent 
	return parnt 	

def Tree_Insert(root,value):
	if root is None:
		root=node
	else:
		nxtnode=None
		while root is not None:
			nxtnode=root
			if value.val<root.val:
				root=root.left
			else:
				root=root.right
		value.parent=nxtnode
		if nxtnode is None:
			root=value
		elif value.val<nxtnode.val:
				nxtnode.left=value
		else:
			nxtnode.right=value	

	
def Transplant(root,u,v):
	if u.parent is None:
		root=v
	elif u is u.parent.left:
		u.parent.left=v
	else:
		u.parent.right=v
	if v is not None:
		v.parent=u.parent

def Delete(root,z):
	if z.left is None:
		Transplant(root,z,z.right)
	elif z.right is None:
		Transplant(root,z,z.left)
	else:
		y=min(z.right)
		if y.parent is not z:
			Transplant(root,y,y.right)
			y.right=z.right
			y.right.parent=y
		Transplant(root,z,y)
		y.left=z.left
		y.left.parent=y

root=Node(10)
n = input("enter length")
for i in range(1, int(n)):
	k=int(input("enter value"))
	Tree_Insert(root,Node(k))
	
sv=3
print("Preorder traversal of binary tree is")
printPreorder(root) 
print("\nInorder traversal of binary tree is")
printInorder(root) 
print("\nPostorder traversal of binary tree is")  
printPostorder(root) 
print("\nsearching a value in tree")
a=Tree_Search(root,sv) 
print (a.val)
print("\nMinimum value of tree")
b=min(root)
print(b.val)
print("\nMaximum value of tree")
c=max(root)
print(c.val)
print("\nSuccesor")
d=Tree_Succesor(root)
print(d.val)
print("\nPredecessor")
e=Tree_Predecessor(root)
print(e.val)
value=Node(7)
Tree_Insert(root,value)
Delete(root,value)