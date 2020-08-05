class LinkedList:
  
  def __init__(self):
    self.first = None
    self.length = 0

  class Node:
    def __init__(self, value, index, *nxt):
      self.value = value
      self.index = index
      if nxt:
        self.nxt = nxt
      else:
        self.nxt = None

    def add_next(self, nxt):
      if self.nxt == None:
        self.nxt = nxt
      else:
        self.nxt.add_next(nxt)
  
    def remove_next(self):
      self.nxt = None
    
    def to_string(self):
      return (self.value if self.value != None else "nothing") +", " + (self.nxt.to_string() if self.nxt != None else "<END>")

  def to_string(self):
    if self.first == None:
      return "empty-list"
    else:
      return self.first.to_string()
    
  def append(self, value):
    self.length += 1
    if self.first == None:
      self.first = self.Node(value, length)
    else:
      self.first.add_next(self.Node(value, length))

  def search(self, value):
    

  def insert(self, after, value):
    for i in reversed(range(self.length)):
      


def main():
  l = LinkedList()
  print(l.to_string())
  print(l.length)
  l.append("A")
  print(l.to_string())
  print(l.length)
  l.append("B")
  print(l.to_string())
  print(l.length)
  l.append("C")
  print(l.to_string())
  print(l.length)
  l.append("D")
  print(l.to_string())
  print(l.length)

if __name__ == "__main__":
  main()
