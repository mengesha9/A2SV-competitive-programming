class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        x = 0
        y = 0
        L = {"north" : "west", "west":"south","south":"east" , "east":"north"}
        R = {"north" : "east", "west":"north","south":"west" , "east":"south"}
        di = "north"
        for n in instructions:
            if n == 'G' and di == "south":
                y -= 1
            if n == "G" and di == "north":
                y += 1
            if n == "G" and di == "west":
                x -= 1
            if n == "G" and di == "east":
                x += 1
            if n == "L":
                di = L[di]
            if n == "R" :
                di = R[di]

        if (x,y)==(0,0):
            return True
        elif di != "north":
            return True
        else:
            return False                


                   


            
