for _ in range(int(input())):
    def f():
        results = []
        n = int(input())
        arr = list(map(int, input().split()))
        if n == 1:
            return("YES")
        else:
            occ = set()
            occ.add(arr[0])
            valid = True
            for i in range(1, n):
                s = arr[i]
                if (s - 1) in occ or (s + 1) in occ:
                    occ.add(s)
                else:
                    valid = False
                    break
            return("YES" if valid else "NO")

    print(f())