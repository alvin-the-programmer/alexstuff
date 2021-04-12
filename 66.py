class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
a.next = b
b.next = c
c.next = d
d.next = e

def copy_deep_list(head):
    if head is None:
        return None
    new_root = Node(head.val + '!')
    new_root.next = copy_deep_list(head.next)
    return new_root


def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)
    return


# print_list(a)
# print('---')
# new_root = copy_deep_list(a)
# print_list(new_root)


def copy_list_random_ptr(head):
    copies = {}
    return copy_helper(head, copies)


# 0: 7
# 1: 13
# 2: 11


def copy_helper(head, copies):
    if head is None:
        return None

    new_root = copies[id(head)] if id(head) in copies else Node(head.val)
    copies[id(head)] = new_root

    curr_random = head.random
    if curr_random is not None:
      new_random = copies[id(curr_random)] if id(curr_random) in copies else Node(curr_random.val)
      copies[id(curr_random)] = new_random
      new_root.random = new_random

    new_root.next = copy_helper(head.next, copies)
    return new_root

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy_list_random_ptr(head)


def copy_list_random_ptr(head):
    copies = {}
    tag_nodes(head)
    return copy_helper(head, copies)

def tag_nodes(head, idx = 0):
  if head is None:
    return

  head.id = idx

  tag_nodes(head.next, idx + 1)
  return head

def copy_helper(head, copies):
    if head is None:
        return None

    new_root = copies[head.id] if head.id in copies else Node(head.val)
    copies[head.id] = new_root

    curr_random = head.random
    if curr_random is not None:
      new_random = copies[curr_random.id] if curr_random.id in copies else Node(curr_random.val)
      copies[curr_random.id] = new_random
      new_root.random = new_random

    new_root.next = copy_helper(head.next, copies)
    return new_root




# my_string = "alvin"
# my_list = [1,5,1,2,2]

# len(my_string)
# len(my_list)



class Dog:
  def __init__(self, name, color, height):
    self.name = name
    self.color = color
    self.height = height
#   def __str__(self):
#       return self.name + " the " + self.color + "doge"

  def __len__(self):
    return self.height


my_dog = Dog('fido', 'brown', 30)
# print(len(my_dog))
print(my_dog)
print(id(my_dog))

