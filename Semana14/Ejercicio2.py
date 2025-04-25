class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node
    tail: Node

    def __init__(self, head):
        self.head =head
        self.tail=head

    def print_structure(self):
        current_node = self.head
        str_result=self.tail.next
        #self.tail.next=current_node.next
        #print (f'Este es el valor del string: {str_result}')
        while current_node is not str_result:
            #print(f'este es el current node: {current_node}')
            print(current_node.data)
            #self.tail=current_node
            self.tail=current_node
            current_node= current_node.next
        
            
        #print(f'El valor de self_tile es: {self.tail.data}')


    def push_left(self, new_node):
        current_node=new_node
        current_node.next = self.head
        self.head=current_node
        while current_node is not None:
            #print(f'Cual es el final aqui1: {current_node.data}')
            current_node=current_node.next
        self.tail.next=current_node
        #print(f'Aqui el valor de tail es: {self.tail.next}')
            
        
        #print(f'Cual es el final aqui2: {self.tail.next}')
        #print(f'Cual es el final aqui3: {self.tail.next}')

    #print(f'El valor es: {self.head.data}')
    def push_right(self, new_node):
        current_node=self.head
        self.tail=new_node
        while current_node.next is not None:
            current_node = current_node.next
        
        self.tail.next=current_node.next
        current_node.next=new_node
        
        
        
    def pop_left(self):
        if self.head:
            self.head = self.head.next

    
    def pop_right(self):
        #print(f'es aqui5{self.tail.data}')
        self.tail.next=self.tail
        #print(f'es aqui4{self.tail.data}')
    

        
first_node=Node("Hello")
myqueue=Queue(first_node)
#myqueue.print_structure()

second_node=Node("world")
myqueue.push_left(second_node)
#myqueue.print_structure()

tird_node=Node("this")
myqueue.push_right(tird_node)
#myqueue.print_structure()

fourth_node=Node("is")
myqueue.push_left(fourth_node)
#myqueue.print_structure()


fith_node=Node("Python")
myqueue.push_right(fith_node)
#myqueue.print_structure()
#myqueue.print_structure()

myqueue.pop_left()
#myqueue.print_structure()

myqueue.pop_right()
myqueue.print_structure()












