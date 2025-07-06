t = int(input())
for _ in range(t):
    n = int(input())
    found = False
    current = n

    for move in range(10):
        if move % 2 == 0:  # Vanya's turn
            if current % 3 == 0:
                found = True
                break
            else:
                # Choose the better move: try to move toward multiple of 3
                if (current + 1) % 3 == 0:
                    current += 1
                else:
                    current -= 1
        else:  # Vova's turn
            # Vova tries to prevent Vanya from hitting multiple of 3
            if (current + 1) % 3 != 0:
                current += 1
            else:
                current -= 1

    print("First" if found else "Second")
def main():
    dp = [[False] * 11 for _ in range(3)]
    
    for d in range(10, -1, -1):
        for r in range(3):
            if d == 10:
                dp[r][d] = False
            else:
                s1 = (r + 1) % 3
                s2 = (r + 2) % 3
                if d % 2 == 0:
                    if s1 == 0 or s2 == 0:
                        dp[r][d] = True
                    else:
                        if dp[s1][d+1] or dp[s2][d+1]:
                            dp[r][d] = True
                        else:
                            dp[r][d] = False
                else:
                    if dp[s1][d+1] and dp[s2][d+1]:
                        dp[r][d] = True
                    else:
                        dp[r][d] = False
                        
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        r_initial = n % 3
        if dp[r_initial][0]:
            results.append("First")
        else:
            results.append("Second")
            
    for res in results:
        print(res)

if __name__ == "__main__":
    main()