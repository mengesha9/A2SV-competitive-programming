class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        q = deque()
        q.append(rooms[0])
        rooms[0]=0

        
        while q:
           
            arr = q.popleft()

            for key in arr:
                if rooms[key] !=0 :
                    q.append(rooms[key])
                    rooms[key] = 0
        print(rooms)         
        for i in rooms:
            if i != 0 :
                return False 
            
        return True