class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


# [1.] Write a fn list_find(head, target) that takes in the head of a LL.
# The fn should return a boolean indicating whether or not the target exists
# as a value in the LL.
#
# Solve iteratively and recursively.
#
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')

# a.next = b
# b.next = c
# c.next = d
# head = a
#
# iterative
# n is the number of nodes in the LL
# time: O(n)
# space: O(1)
# def list_find(head, target):
#   curr = head
#   while curr != None:
#     if curr.val == target:
#       return True
#     curr = curr.next
#   return False

# recursive
# n is the number of nodes in the LL
# time: O(n)
# space: O(n) // there are n calls on the stack in the WORST case scenario
# def list_find(head, target):
#   # base case
#   if head == None:
#     return False
#   # stop recursion
#   if head.val == target:
#     return True
#   # recursive step
#   # i keep forgetting to RETURN the recursive call
#   return list_find(head.next, target)

# print(list_find(head, 'c')) # True
# print(list_find(head, 'Z')) # False


# [2.] Write a fn list_count(head, target) that takes in the head of a LL.
# The fn should return a number representing the count of that target in the LL.
#
# Solve iteratively and recursively.
#

# V1: recursive solution with counter
# def list_count(head, target, counter=0):
#     # iterate across the linked list until the end
#     # have a counter for occurances of the target
#     if not head.next:
#         return counter
#     if head.val == target:
#         counter += 1
#     return list_count(head.next, target, counter)

# V2: recursive

def list_count(head, target):
    # base cases need to return whatever data type we concatenate in final return
    if not head:
        return 0
    counter = 0
    if head.val == target:
        counter += 1
    return list_count(head.next, target) + counter


# a -> b -> c -> d


a = Node(1)
b = Node(3)
c = Node(7)
d = Node(3)
e = Node(1)
f = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
head = a

print("hi" + str(list_count(a, 3)))


#  iterative
# time: O(n)
# space: O()
# def list_count(head, target):
#   count = 0
#   curr = head
#   while curr != None:
#     if curr.val == target:
#       count += 1
#     curr = curr.next
#   return count

# recursive
# time: O(n)
# space: O(2n) -> O(n)


# def list_count(head, target):
#     if head == None:
#         return 0
#     is_match = 0
#     if head.val == target:
#         is_match += 1
#     return is_match + list_count(head.next, target)

# is this right? not even sure if this method is necessary or not but i cant think of another way to check if its equivalent or not


# def check(head, target):
#     if head.val == target:
#         return 1
#     else:
#         return 0


# print(list_count(head, 1))  # 3
# print(list_count(head, 3))  # 2
# print(list_count(head, 7))  # 1
# print(list_count(head, 42))  # 0
