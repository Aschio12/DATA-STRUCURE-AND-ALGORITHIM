for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))
    dict={}
    n = []
    key="a0"
    counter=0  
    dict[key]=[arr[0]]
    for i in range(1, k):
        if arr[i] > arr[i-1] + 1:
            counter+=1
            key=f"a{counter}"
            dict[key]=[arr[i]]
        else:
            dict[key].append(arr[i])
    print(dict)
