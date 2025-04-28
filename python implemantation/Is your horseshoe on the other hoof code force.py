from collections import Counter
shoes=list(map(int,input().split()))
pure_shoes=set(shoes)
print(4-len(pure_shoes))