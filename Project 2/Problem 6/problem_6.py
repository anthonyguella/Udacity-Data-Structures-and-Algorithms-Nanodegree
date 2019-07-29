class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    llist_1_copy = llist_deepcopy(llist_1)
    llist_2_copy = llist_deepcopy(llist_2)
    node = llist_1_copy.head
    if node is None:
        return llist_2
    while node.next:
        node = node.next
    node.next = llist_2_copy.head
    return llist_1_copy
    

def intersection(llist_1, llist_2):
    intersection = LinkedList()
    node = llist_1.head
    list1_dict = {}
    while node:
        if not node.value in list1_dict:
            list1_dict[node.value] = 0
        list1_dict[node.value] += 1
        node = node.next
    node = llist_2.head
    while node:
        if node.value in list1_dict:
            new_node = Node(node.value)
            intersection.append(new_node)
            list1_dict[node.value] -= 1
            if list1_dict[node.value] == 0:
                del list1_dict[node.value]
        node = node.next
    return intersection

def llist_deepcopy(llist):
    new_list = LinkedList()
    node = llist.head
    while node:
        new_node = Node(node.value)
        new_list.append(new_node)
        node = node.next
    return new_list

# **** Test case 1 ****
# Normal Inputs

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 1 -> 
print (intersection(linked_list_1,linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 


# **** Test case 2 ****
# No Intersection

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 3 ****
# Element 1 empty

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 4 ****
# Element 2 empty

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 5 ****
# Element 1 None

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = None
element_2 = [1,7,8,9,11,21,1]

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 6 ****
# Element 2 None

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = None

for i in element_1:
    linked_list_3.append(i)

print (union(linked_list_3,linked_list_4))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 
print (intersection(linked_list_3,linked_list_4))
# (No Output)


# **** Test case 7 ****
# Identical list

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 -> 4 ->
print (intersection(linked_list_3,linked_list_4))
# 1 -> 2 -> 3 -> 4 -> 


# **** Test case 8 ****
# Same Reference

linked_list_3 = LinkedList()

element_1 = [1,2,3,4]

for i in element_1:
    linked_list_3.append(i)

print (union(linked_list_3,linked_list_3))
# 1 -> 2 -> 3 -> 4 -> 1 -> 2 -> 3 -> 4 -> 
print (intersection(linked_list_3,linked_list_3))
# 1 -> 2 -> 3 -> 4 -> 
