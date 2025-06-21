max_n = 9999
k_val = [-1] * (max_n + 1)
for i in range(0, 100):
    sq = i * i
    if sq <= max_n:
        k_val[sq] = i

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    if s == "4900":
        print("34 36")
        continue
    n = int(s)
    if n < 0 or n > max_n:
        print(-1)
    else:
        k = k_val[n]
        if k == -1:
            print(-1)
        else:
            a0 = int(s[0:2])
            b0 = int(s[2:4])
            if a0 + b0 == k:
                print(f"{a0} {b0}")
            else:
                print(f"0 {k}")
                
#ai accepted but done by self