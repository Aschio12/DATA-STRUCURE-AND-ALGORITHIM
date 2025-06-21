t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    rev = s[::-1]
    if s < rev:
        print("YES")
    else:
        if k == 0:
            print("NO")
        else:
            if len(set(s)) == 1:
                print("NO")
            else:
                print("YES")