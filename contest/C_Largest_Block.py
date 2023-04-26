number_testcases=int(input())

for i in range(number_testcases):
    n= int(input())
    num_blocks =int(input())  
    j=0
    while j<n:
        while num_blocks[j]>num_blocks[0]:
            num_blocks[0]+=1
            num_blocks[j]-=1
        j+=1
    print(num_blocks[0])   






