class Node():
    data:str
    next:"Node"

    def __init__(self,data,next_right=None,next_left=None):
        self.data=data
        self.next_right=next_right
        self.next_left=next_left
    

class Bynary_Tree():
    root:Node

    def __init__(self,root):
        self.root=root
        self.level=0
    def print_structure(self,node):
            
            if self.root is None:
                print("Binary Tree does not have a root, tree cannot be display")
            if node is not None:
                
                current_node=node
                if current_node.next_left is not None or current_node.next_right is not None:
                    self.level+=1
                if current_node.next_left is not None:
                    print(f'This is my level: {self.level}, Im the father: {current_node.data}, and Im his son: {current_node.next_left.data}')
                if current_node.next_right is not None:
                    print(f'This is my level: {self.level}, Im the father: {current_node.data} and Im his son: {current_node.next_right.data}')
                
                self.print_structure(current_node.next_left)
                self.print_structure(current_node.next_right)
            

ninth_node=Node("ninth_node")
eighth_node=Node("eighth_node",ninth_node)
seventh_node=Node("seventh_node")
sixth_node=Node("sixth_node",eighth_node)
fifth_node=Node("fifth node",sixth_node,seventh_node)
fourth_node=Node("forth node",None,fifth_node)
third_node=Node("third node")
second_node=Node("second node",fourth_node)
first_node=Node("first node",second_node,third_node)


my_tree=Bynary_Tree(first_node)
my_tree.print_structure(first_node)







        





