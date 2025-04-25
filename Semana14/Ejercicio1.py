class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        current_node=new_node
        current_node.next = self.head
        self.head=current_node
        #print(f'El valor es: {self.head.data}')

        
    def pop(self):
        if self.head:
            self.head = self.head.next

first_node=Node("Hola")
myqueue=Queue(first_node)
#myqueue.print_structure()

second_node=Node("Mundo")
myqueue.push(second_node)
#myqueue.print_structure()

tird_node=Node("Esto")
myqueue.push(tird_node)
#myqueue.print_structure()

myqueue.pop()
#myqueue.print_structure()

myqueue.pop()
#myqueue.print_structure()

myqueue.pop()
myqueue.print_structure()

myqueue.pop()
myqueue.print_structure()