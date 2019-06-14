import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# initial run took 11.4 seconds
# binary search tree?
# run one list through the class function, use contain method to find duplicates

# used BST from earlier this week
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)
    curNode = self
    while True:
      # if cur node goes left
      if curNode.value > new_node.value:
        # if cur node exists
        if curNode.left is not None:
          #cur node becomes that value
          curNode = curNode.left
        else:
          curNode.left = new_node
          break
      # if cur node goes right
      if curNode.value <= new_node.value: #<===== found error in my BST code, changed from "<" to "<="
        if curNode.right is not None:
          curNode = curNode.right
        else:
          curNode.right = new_node
          break


  def contains(self, target):
    curNode = self
    yesContains = False
    while True:
      # if cur node val is the target return true
      if curNode.value == target:
        yesContains = True
        break
      # if not, check if target val would be found to the left or right

      # target would be found to the left
      elif curNode.value > target:
        # check if cur node left exists(similar method used in insert)
        if curNode.left is not None:
          curNode = curNode.left
        else:
          #does not exist, break, returns false
          break
      elif curNode.value < target:
        if curNode.right is not None:
          curNode = curNode.right
        else:
          break
    return yesContains

duplicates = []

# initialize name1 bst sorted list
bstName1 = BinarySearchTree(names_1[0])

# insert the rest of the name1 to the bstName variable
for x in range(1, len(names_1)):
    bstName1.insert(names_1[x])



# use contain method to check if items in name2 are in bstName1 list
for x in range(0, len(names_2)):
    # if sorted list contains item from name2, append item to the dupes list
    if bstName1.contains(names_2[x]):
        duplicates.append(names_2[x])


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

