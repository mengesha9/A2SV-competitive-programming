from collections import defaultdict

def winner(s, e, arr, k):
    if s == e:
        return [[arr[s],s]]
    
    mid = s + (e-s)//2
    left = winner(s, mid, arr, k)
    right = winner(mid+1, e, arr,k)
    freq = defaultdict(int)
    answer = []
    for i in range(len(left)):
        for j in range(len(right)):
            if  abs(left[i][0] - right[j][0]) <= k:

                if left[i][1] not in freq:
                    answer.append(left[i])
                    freq[left[i][1]] = True
                if right[j][1] not in freq:
                    answer.append([right[j][0],right[j][1]])
                    freq[right[j][1]] = True
            elif left[i][0] > right[j][0] + k:
                if left[i][1] not in freq:
                    answer.append([left[i][0],left[i][1]])
                    freq[left[i][1]] = True
            elif right[j][0] > right[i][0] + k:
                if left[i][1] not in freq:
                    answer.append([right[j][0],right[j][1]])
                    freq[right[j][1]] = True
    return answer



n ,k = map(int, input().split())
arr = list(map(int,input().split()))

res = winner(0,len(arr)-1,arr,k)
result = []
for i in range(len(res)):
    result.append(res[i][1] + 1)

print(*result)







