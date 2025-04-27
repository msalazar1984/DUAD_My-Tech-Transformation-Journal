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
        my_result_string=""
        while current_node is not str_result:
            #print(f'este es el current node: {current_node}')
            my_result_string+=f'{current_node.data} <-> '
            
            #self.tail=current_node
            self.tail=current_node
            current_node= current_node.next
        print(my_result_string)
            
    def push_left(self, new_node):
        current_node=new_node
        current_node.next = self.head
        self.head=current_node
        while current_node is not None:
            current_node=current_node.next
        self.tail.next=current_node


    def push_right(self, new_node):
        current_node=self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node=self.tail
        self.tail=new_node
        self.tail.next=current_node.next
        current_node.next=new_node
        
        
    def pop_left(self):
        if self.head:
            self.head = self.head.next

    
    def pop_right(self):
        current_node=self.head
        while current_node.next is not self.tail:
            current_node=current_node.next
        self.tail=current_node
    

        
first_node=Node("Hello")
myqueue=Queue(first_node)
#myqueue.print_structure()

second_node=Node("world")
myqueue.push_left(second_node)
#myqueue.print_structure()

third_node=Node("this")
myqueue.push_right(third_node)
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

sixth_node=Node("Programming")
myqueue.push_right(sixth_node)
#myqueue.print_structure()

myqueue.pop_right()
#myqueue.print_structure()

seventh_node=Node("Language")
myqueue.push_right(seventh_node)
#myqueue.print_structure()

#myqueue.pop_right()
myqueue.print_structure()










