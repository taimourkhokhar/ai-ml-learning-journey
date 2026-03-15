class Tree:
  def __init__(self,data):
    self.data=data
    self.children=[]
    self.parent=None

  def add_child(self,child):
    child.parent=self
    self.children.append(child)
  
  def get_level(self):
    level=0
    p=self.parent
    while p:
      level+=1
      p=p.parent
    return level

  def print_Tree(self):
    spaces=' '*self.get_level()*2
    print(spaces+self.data)
    if self.children:
     for child in self.children:
      child.print_Tree()

def build_product_tree():
    root=Tree("Electronice")

    laptop=Tree("laptop")
    laptop.add_child(Tree("Mac"))
    laptop.add_child(Tree("Surface"))
    
    cellphone=Tree("Cell Phone")
    cellphone.add_child(Tree("iphone"))
    cellphone.add_child(Tree("Google pixel"))
    root.add_child(laptop)
    root.add_child(cellphone)

    print(laptop.get_level())
    return root



if __name__=='__main__':
 root= build_product_tree()
 print(root.get_level())
 print(root.print_Tree())
 pass