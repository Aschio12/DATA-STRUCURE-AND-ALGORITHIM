test=int(input())
for _ in range(test):
    number=list(map(int,input().split()))
    number.sort()
    print(number[1])