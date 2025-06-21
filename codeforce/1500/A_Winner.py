from collections import defaultdict

def main():
    n = int(input().strip())
    scores = defaultdict(int)
    history = []
    
    for _ in range(n):
        data = input().split()
        name = data[0]
        score = int(data[1])
        scores[name] += score
        history.append((name, scores[name]))
    
    max_score = max(scores.values())
    candidates = {player for player, total in scores.items() if total == max_score}
    
    for name, total in history:
        if name in candidates and total >= max_score:
            return(name)
print(main())