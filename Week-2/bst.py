class binarySearch:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

  def add(self,data):
    if data==self.data:
      return
    
    if data<self.data:
      #add data in left subtree
      if self.left:
        self.left.add(data)
      else:
        self.left=binarySearch(data)
    else:
      #add data in righ subtree
      if self.right:
        self.right.add(data)
      else:
        self.right=binarySearch(data)

  
  def inorder(self):
    elements=[]
    
    #visit left tree
    if self.left:
      elements+=self.left.inorder()
    #base node
    elements.append(self.data)
    
    #right node

    if self.right:
      elements+=self.right.inorder()


    return elements


  def search(self,val):
    if self.data == val:
        return True

    if val < self.data:
        if self.left:
            return self.left.search(val)
        else:
            return False

    if val > self.data:
        if self.right:
            return self.right.search(val)
        else:
            return False
  
  def find_max(self):
     if self.right is None:
        return self.data
     return self.right.find_max()


  def find_min(self):
     if self.left is None:
        return self.data
     return self.left.find_min()



  def delete(self, val):
    # 1. Search for the node to delete
    if val < self.data:
        if self.left:
            self.left = self.left.delete(val)
    elif val > self.data:  # Now properly aligned
        if self.right:
            self.right = self.right.delete(val)
    else:
        # 2. We found the node! Now handle the 3 sub-cases:
        
        # Case A: No children (Leaf node)
        if self.left is None and self.right is None:
            return None
        
        # Case B: Only one child
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left  # Fixed: returns left if right is missing

        # Case C: Two children
        # Find the smallest value in the right subtree to replace this node
        min_val = self.right.find_min()
        self.data = min_val
        self.right = self.right.delete(min_val)

    return self











def build(elements):
  root=binarySearch(elements[0])
  for i in range(1,len(elements)):
    root.add(elements[i])

  return root

if __name__=='__main__':
  numbers=[17,4,1,20,23,18,34]
  numbers_tree=build(numbers)
  print(numbers_tree.inorder())

  numbers_tree.delete(20)
  print(numbers_tree.inorder())

#   print(numbers_tree.search(34))