from collections import defaultdict
for _ in range(int(input())):
    n,m=map(int,input().split())
    row_one=defaultdict(list)
    col_one=defaultdict(list)
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input())))
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                col_one[j].append(arr[i][j])
                row_one[i].append(arr[i][j])
    count_odd_row=0
    for key in row_one:
        odd_cheack=sum(row_one[key])
        if odd_cheack%2!=0:
            count_odd_row+=1
    count_odd_col=0
    for key in col_one:
        if sum(col_one[key])%2!=0:
            count_odd_col+=1
    print(max(count_odd_col,count_odd_row))