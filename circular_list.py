
class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class CircularList:
    def __init__(self):
        self.head = None
 
    def insert(self, value):
        new = Cell(value)
        if not self.head:
            self.head = new
            new.next = new
            return
        tmp = self.head
        while not tmp.next == self.head:
            tmp = tmp.next
        tmp.next = new
        new.next = self.head
 
    def delete(self, value):
        if not self.head:
            print("[*] List is empty.")
            return
        
        if self.head == self.head.next:
            self.head = None
            return
        
        if self.head.value == value:
            tmp = self.head
            self.head = tmp.next
            tmp = None
            return
        front = self.head
        rear = front.next
        isfound = False
        
        while not rear == self.head:
            if rear.value == value:
                isfound = True
                break
            front = rear
            rear = rear.next
        if isfound:
            front.next = rear.next
            rear = None
        else:
            print("[*] Data not found")
 
    def show(self):
        tmp = self.head
        if tmp:
            while tmp:
                print(tmp.value)
                tmp = tmp.next
                if tmp == self.head:
                    break
        else:
            print('[*] List is empty.')
 
l = CircularList()
print('insert 1, 2, 3...')
l.insert(1)
l.insert(2)
l.insert(3)
print('print data')
l.show()
print('delete 2...')
l.delete(2)
print('print data')
l.show()
