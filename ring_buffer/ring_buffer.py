class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # start at 0 index, set item to storage[0]
    self.storage[self.current] = item
    # increase current by 1
    self.current += 1
    # do this until reaches capacity then reset back to zero
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    store = self.storage
    answer = [x for x in store if x is not None]
    return answer