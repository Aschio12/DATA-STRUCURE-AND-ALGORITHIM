k=int(input())
month_len=list(map(int,input().split()))
month_len.sort(reverse=True)
count,grow,i=0,0,0
while grow<k and  i < len(month_len):
    grow+=month_len[i]
    count+=1
    i+=1
print(count if grow>=k else -1)
     