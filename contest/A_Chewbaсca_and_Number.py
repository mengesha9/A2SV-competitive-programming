x = input()
string = list(str(x))

min_val = int(string[0])
arr = []
for n in string :
    min_val = min ( min_val, int(n))
    arr .append(int(n))

min_number =''
for i in range(len(arr)):
    if arr[i] != min_val:
        min_number += str(9-arr[i])
    else:
        min_number += str(arr[i]) 
i=0
while min_number[i] == '0':
    i+=1
answer = min_number[i:]
print(int(answer))




    

