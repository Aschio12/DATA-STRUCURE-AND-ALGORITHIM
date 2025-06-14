t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    s_set = set()
    for a_val in a_list:
        for b_val in b_list:
            s_set.add(a_val + b_val)
            
    if len(s_set) >= 3:
        results.append("YES")
    else:
        results.append("NO")

for res in results:
    print(res)
    
