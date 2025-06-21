t = int(input())
for _ in range(t):
    s = input().strip()
    if s == "abc":
        print("YES")
        continue
    # Check all possible single swaps directly
    if (s[1] + s[0] + s[2] == "abc" or  # swap 0 and 1
        s[2] + s[1] + s[0] == "abc" or  # swap 0 and 2
        s[0] + s[2] + s[1] == "abc"):   # swap 1 and 2
        print("YES")
    else:
        print("NO")