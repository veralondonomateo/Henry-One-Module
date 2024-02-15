class Node:
    def __init__(self, val) -> None:
        self.data = val 
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,new):
        self.data = new
    
    def setNext(self,new_node):
        self.next = Node(new_node)