n=int(input())
s=list(map(int,input().split()))
score1, score2 = 0, 0
i, j = 0, len(s)-1
counter=0
while(i<=j):
    if counter%2==0:
        if(s[j] > s[i]):
            score1+= s[j]
            j-=1
        else:
            score1 += s[i]
            i+=1
    else:
        if(s[j] > s[i]):
            score2+=s[j]
            j-=1
        else:
            score2 += s[i]
            i+=1

    counter+=1
print(f"{score1} {score2}")        
    
    




