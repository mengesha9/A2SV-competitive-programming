class MyCircularDeque:

    def __init__(self, k: int):
       
        self.deque=[None] * k
        self.k=k
        self.size =0
        self.head =0
        self.tail =0
               
        
    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.deque[self.head] = value
            self.size +=1
            return True
        
        elif not self.isFull():
            self.head = (self.head -1) % self.k
            self.deque[self.head] =value
            self.size += 1
            return True
        else:
            return False
   
                 
    def insertLast(self, value: int) -> bool:
        
        if self.isEmpty():
            self.deque[self.tail] = value
            self.size += 1
            return True
        elif not self.isFull():
            self.tail=(self.tail +1)% self.k
            self.deque[self.tail] = value
            self.size += 1
            return True
        else :
            return False
            
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.head] = None
            if self.size != 1:
                self.head = (self.head +1) % self.k
            self.size -= 1
            return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.tail]= None
            if self.size != 1:
                self.tail=(self.tail-1) % self.k
            self.size -= 1
            return True        

    def getFront(self) -> int:
        return self.deque[self.head] if not self.isEmpty() else -1
        

    def getRear(self) -> int:
        return self.deque[self.tail] if not self.isEmpty() else -1
    
    def isEmpty(self) -> bool:
        return  self.size == 0
         
    def isFull(self) -> bool:
        if self.size == self.k :
            return True
        return False
           


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()