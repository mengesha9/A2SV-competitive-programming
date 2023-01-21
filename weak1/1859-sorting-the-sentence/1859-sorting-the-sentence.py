class Solution:
    def sortSentence(self, s: str) -> str:
        y=s.split()
        print(y)
        y.sort(key= lambda x: x[-1] )
        print(y)
        h=''
        for i in range(len(y)):
            if i!=0:
                h += ' '
            h+=(y[i][:len(y[i])-1])
        print(h)
        return h     
