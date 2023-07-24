class LockingTree:

    def __init__(self, parent: List[int]):

        self.locks = defaultdict(int)
        self.desc = defaultdict(list)
        self.ances = defaultdict(list) 

        for i in range(len(parent)):
          
                self.desc[parent[i]].append(i)
                self.ances[i].append(parent[i])

    def lock(self, num: int, user: int) -> bool:
      
        if num not in self.locks :
            self.locks[num] = user
            return True  

        else:
            return False       

    def unlock(self, num: int, user: int) -> bool:
        if  num in self.locks and self.locks[num] == user:
            del self.locks[num]
            return True
        else:
            return False     

    def upgrade(self, num: int, user: int) -> bool:

        def ance(node):
           
            if node in self.locks:
                return False
            
            for n in self.ances[node]:
                if  not ance(n):
                    return False 

            return True    

        tmp = self.des(num)
        # print(tmp)
        # print(ance(num))
        if num not in self.locks and len(tmp) >= 1 and ance(num):
            while tmp:
               del self.locks[tmp.pop()]
            self.locks[num] = user 

            return True
 
        else:
            return False 


    def des(self, num: int) -> list :
        order = [] 
        que = deque()
        que.append(num)


        while que:
            n = que.popleft()
            if n in self.locks:
               order.append(n)

            for node in self.desc[n]:
                que.append(node)   

        return order 


        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)