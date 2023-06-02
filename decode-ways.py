class Solution:
    def numDecodings(self, s: str) -> int:


        hashmap = {"A":'1',"B":'2',"C":'3',"D":'4','E':'5','F':'6','G':'7','H':'8',
        'I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17','R':'18',
        'S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'}

        n = len(s)
        memo = defaultdict(str)
        def back(string):

            if len(string) == 0:
    
                return 1

            if  string not in memo:
                count = 0
                
                for i in range(len(string)):
                    
                    tmp = string[:i+1]
                    tmp2 = string[i+1:]
                    if tmp in hashmap.values():
                          count += back(tmp2)

                memo[string] = count 

            return memo[string]   

        return back(s)