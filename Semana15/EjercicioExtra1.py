class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def bubble_sort(self):
        end=None
        while end!=self.head:
            current_node=self.head
            while current_node.next != end:
                next_node=current_node.next
                print(f'this is next_node:{current_node.data}')
                if current_node.data>next_node.data:
                    print(f'this is current_node:{current_node.data} and this is next_node:{next_node.data}')
                    current_node.data,next_node.data=next_node.data,current_node.data
                    print(f'this is current_node:{current_node.data} and this is next_node:{next_node.data}')
                current_node=current_node.next
            end=current_node

fourth_node=Node(55)
third_node=Node(20,fourth_node)
second_node = Node(15,third_node)
first_node = Node(45, second_node)

linked_list = LinkedList(first_node)
#linked_list.print_structure()

linked_list.bubble_sort()
linked_list.print_structure()