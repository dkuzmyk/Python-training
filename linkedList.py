# linked lists
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def append(self, data):
        if self.head is None:
            newNode = node(data)
            self.head = newNode
        else:
            new_node = node(data)
            cur = self.head

            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            elems.append(cur_node.data)
            cur_node = cur_node.next

        print(elems)

    def pushFront(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode

    def erase(self, data):
        len = 0
        curr = self.head
        while curr.next.data is not data:
            curr = curr.next
            len += 1
            if len >= self.length():
                return 0
        toDel = curr.next
        curr.next = curr.next.next
        del toDel

    def eraseAt(self, idx):
        if idx > self.length() or idx < 0:
            print("no, can't do")
            return

        if idx == 0:
            toDel = self.head
            self.head = self.head.next
            del toDel
            return
        else:
            i = 1
            curr = self.head
            prev = self.head
            while i is not idx:
                prev = curr
                curr = curr.next
                i += 1

            prev.next = curr.next
            return curr.data



my_list = LinkedList()
my_list.append(1)
my_list.display()
my_list.append(0)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
my_list.pushFront(99)
my_list.pushFront(66)
my_list.pushFront(33)
my_list.pushFront(11)
my_list.display()
my_list.erase(99)
my_list.display()
print('erasing ' + str(my_list.eraseAt(1)))
my_list.display()

