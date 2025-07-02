for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    left=0
    right=0
    max_=float("-inf")
    sore=[]
    while right<len(arr):
        if arr[left]<0:
            while arr[right]<0:
                max_=max(max_,arr[right])
                right+=1
                if right==len(arr):
                    break
            left=right
            sore.append(max_)
            max_=float("-inf")
        else:
            while arr[right]>0:
                max_=max(max_,arr[right])
                right+=1
                if right==len(arr):
                    break
            left=right
            sore.append(max_)
            max_=float("-inf")
    print(sum(sore))
            