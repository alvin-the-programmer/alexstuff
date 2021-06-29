

# https://www.algoexpert.io/questions/Validate%20BST
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, mini = float('-inf'), maxi = float('inf')):
	if tree is None:
		return True
    
	if tree.value < mini or tree.value >= maxi:
		return False
	
	left = validateBst(tree.left, mini, tree.value)
	right = validateBst(tree.right, tree.value, maxi)
	
	return left and right

# https://www.algoexpert.io/questions/BST%20Traversal
def inOrderTraverse(tree, array):
	if tree is None:
		return array
	else:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array
	
def preOrderTraverse(tree, array):
    if tree is None:
		return array
	else:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array


def postOrderTraverse(tree, array):
    if tree is None:
		return array
	else:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array

# https://www.algoexpert.io/questions/Min%20Height%20BST
def minHeightBst(array):
	return minHeightBstHelper(None, array)

def minHeightBstHelper(bst, slicedArr):
	if not slicedArr:
		return
	
	middleIdx = len(slicedArr) // 2
	middleNum = slicedArr[middleIdx]
	
	if bst is None:
    	bst = BST(middleNum)
	else:
		bst.insert(middleNum)
	
	left = minHeightBstHelper(bst, slicedArr[0:middleIdx])
	right = minHeightBstHelper(bst, slicedArr[middleIdx + 1:])
	
	return bst
			

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
