class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data # can contain number, integers, and complex objects
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
            return
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.next
        print(dllstr)

    def print_backward(self):
        if self.head is None:
            print("Doubly Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        dllstr = ''

        while itr:
            dllstr += str(itr.data) + '-->'
            itr = itr.prev
        print("Doubly Linked list in reverse", dllstr)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data): 
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("This is not a valid index")

        if index==0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1


    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("This is not a valid index")
        
        if index==0:
            self.head=self.head.next
            self.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)






if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_values(["banana","mango","grapes","orange"])
    dll.print_forward()
    dll.print_backward()
    # dll.insert_at_end("figs")
    # dll.print_forward()
    # dll.insert_at(0,"jackfruit")
    # dll.print_forward()
    # dll.insert_at(6,"dates")
    # dll.print_forward()
    # dll.insert_at(2,"kiwi")
    # dll.print_forward()
    
