

#B+ Tree

import math

class Node:

    def __init__(self, isLeaf=False):
      self.keys = []
      self.isLeaf = isLeaf
      self.parent = None

      if self.isLeaf:
        self.values = []
        self.next = None
      else:
        self.children = []


class BPlusTree:
  def __init__(self, order=4):
    self.root = Node(isLeaf=true)
    self.order = order
    self.max_keys = order - 1
    self.min_keys = math.ceil(order / 2) - 1
    self.actual_height = 1


    # TO-DO Define actual height later...
    def get_root(self):
      return self.root

     def get_height(self):
        return self.actual_height

    order               # max number of children per internal node


# SEARCH for a key
function search(key):
    node = root
    while node.isLeaf == False:
        i = 0
        while i < len(node.keys) and key >= node.keys[i]:
            i = i + 1
        node = node.children[i]

    # now we’re in the leaf node
    for i = 0 to len(node.keys) - 1:
        if node.keys[i] == key:
            return node.values[i]

    return null          # key not found


# FIND the leaf node for a key
function find_leaf(key):
    node = root
    while node.isLeaf == False:
        i = 0
        while i < len(node.keys) and key >= node.keys[i]:
            i = i + 1
        node = node.children[i]
    return node


# INSERT a key/value pair
function insert(key, value):
    leaf = find_leaf(key)

    # insert key/value into leaf in sorted order
    insert key, value into leaf.keys and leaf.values in sorted order

    # if the leaf has too many keys, split it
    if len(leaf.keys) > order - 1:
        split_leaf(leaf)


# SPLIT a leaf node
function split_leaf(leaf):
    newLeaf = new Node(isLeaf = True)
    mid = ceil(order / 2)

    # divide keys and values into two halves
    newLeaf.keys = leaf.keys[mid:]
    newLeaf.values = leaf.values[mid:]
    leaf.keys = leaf.keys[:mid]
    leaf.values = leaf.values[:mid]

    # link the new leaf into the chain
    newLeaf.next = leaf.next
    leaf.next = newLeaf

    # promote the first key of new leaf to parent
    promotedKey = newLeaf.keys[0]
    insert_in_parent(leaf, promotedKey, newLeaf)


# INSERT a promoted key into parent
function insert_in_parent(leftNode, key, rightNode):
    # if we just split the root, make a new root
    if leftNode == root:
        newRoot = new Node(isLeaf = False)
        newRoot.keys = [key]
        newRoot.children = [leftNode, rightNode]
        root = newRoot
        return

    parent = leftNode.parent

    # insert key and new child pointer in sorted order
    insert key and rightNode into parent.keys and parent.children in sorted order

    # if parent now has too many keys, split it too
    if len(parent.keys) > order - 1:
        split_internal(parent)


# SPLIT an internal node
function split_internal(node):
    newNode = new Node(isLeaf = False)
    mid = ceil(order / 2)
    promotedKey = node.keys[mid]

    # move half of the keys and children to new internal node
    newNode.keys = node.keys[mid + 1:]
    newNode.children = node.children[mid + 1:]
    node.keys = node.keys[:mid]
    node.children = node.children[:mid + 1]

    # reassign parent pointers for children
    for child in newNode.children:
        child.parent = newNode

    # insert promoted key into parent
    insert_in_parent(node, promotedKey, newNode)


# RANGE QUERY using linked leaves
function range_query(start, end):
    result = []
    leaf = find_leaf(start)

    # scan forward through leaves
    while leaf != null:
        for i = 0 to len(leaf.keys) - 1:
            if start <= leaf.keys[i] <= end:
                result.append((leaf.keys[i], leaf.values[i]))
            else if leaf.keys[i] > end:
                return result
        leaf = leaf.next

    return result
