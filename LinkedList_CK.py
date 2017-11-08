class LinkedList:
    # singly linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None
        
    def add_head(self,head):
        # if empty set head/tail to new
        if self.head is None:
            self.head = head
            # find end of new 
            self.tail = self.find_tail()
        # if has head add all to end of new 
        else:
            temp = self.head
            node = head
            # find end of new
            while node.next is not None:
                node = node.next
            # attach old tail to end of new
            node.next = temp
            # set new as head
            self.head = head
        # update length
        self.get_length()
        
    def add_tail(self, tail):
        # if empty set head/tail to new
        if (self.head is None) and (self.tail is None):
            self.head = tail
        # if has tail append new to it and get new tail and length
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = tail
        self.tail = self.find_tail()
        self.get_length()
        
    def find_tail(self):
        # search until hit tail and return node
        node = self.head
        while node.next is not None:
            node = node.next
        return node
        
    def get_length(self):
        # increment counter until hit a nextless node
        counter = 1
        node = self.head
        while node.next is not None:
            counter += 1
            node = node.next
        self.length = counter
        
    def insert_after(self, number, new_node):
        counter = 1
        node = self.head
        # move until we get to 'at' position 
        while counter < number:
            node = node.next
            counter += 1
        # copy previous next chain to temp
        temp = node.next
        # find end of new
        node2 = new_node
        while node2.next is not None:
            node2 = node2.next
        # attach old tail to new
        node2.next = temp
        # attach new to old front
        node.next = new_node
        # update length
        self.get_length()
        
    def remove_at(self, number):
        counter = 1
        node = self.head
        # go to one before 'at'
        while counter < number-1:
            node = node.next
            counter += 1
        # attach one before to one after
        node.next = node.next.next
        # can just decrement length by 1
        self.length -= 1
        
    def print_list(self):
        # loop through list and print a string with all vals
        node = self.head
        outstr = str(node.value)
        while node.next is not None:
            node = node.next
            outstr = outstr + ' -> ' + str(node.value)
        print outstr
        
    def find_loop(self):
        slow = self.head.next
        fast = self.head.next.next
        while (slow != fast) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        if fast.next.next is None:
            print 'found tail, list is not looped'
            return
        else:
            slow = self.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            print 'loop starts at ', fast.value
            return fast
    
    def remove_loop(self, loop_node):
        # look for second time loop_node is hit
        hit_once = False
        node = self.head
        while (hit_once == False) or (node.next != loop_node):
            if node.next == loop_node: hit_once = True
            node = node.next
        node.next = None
                    
        
class Node:    
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
# various testing         
        
# start with 3->4->5
a = Node(3)
b = Node(4)
a.next = b
c = Node(5)
b.next = c

# actually put in a list
LL = LinkedList()
LL.add_head(a)
print 'initiate linked list'
LL.print_list()
print 'length = ', LL.length
print ''

LL.add_head(Node(9))
print 'add single node to head'
LL.print_list()
print 'length = ', LL.length
print ''

print 'add single node to tail'
LL.add_tail(Node(2))
LL.print_list()
print 'length = ', LL.length
print ''


LL.insert_after(2, Node(7))
print 'insert single node'
LL.print_list()
print 'length = ', LL.length
print ''

LL.remove_at(4)
print 'remove single node'
LL.print_list()
print 'length = ', LL.length
print ''

d = Node(44)
d.next = Node(21)
d.next.next = Node(13)

LL.add_tail(d)
print 'add long tail'
LL.print_list()
print 'length = ', LL.length
print ''

e = Node(41)
e.next = Node(11)
LL.add_head(e)
print 'add long head'
LL.print_list()
print 'length = ', LL.length
print ''

f = Node(222)
f.next = Node(111)
LL.insert_after(1,f)
print 'insert linked nodes'
LL.print_list()
print 'length = ', LL.length
print ''


LL2 = LinkedList()
LL2.head = Node(1)
LL2.head.next = Node(2)
LL2.head.next.next = Node(3)
LL2.head.next.next.next = Node(4)
LL2.head.next.next.next.next = Node(5)
LL2.head.next.next.next.next.next = Node(6)
LL2.head.next.next.next.next.next.next = LL2.head.next.next.next

print 'Search for a loop (has/does not have)'
r = LL2.find_loop()
r2 = LL.find_loop()
print ''

print 'Remove loop'
LL2.remove_loop(r)
LL2.print_list()