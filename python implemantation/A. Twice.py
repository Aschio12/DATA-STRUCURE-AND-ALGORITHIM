from collections import Counter
test=int(input())
for _ in range(test):
    length=int(input())
    mail_box=list(map(int,input().split()))
    reps_counter=list(Counter(mail_box).values())
    answer=sum(reps//2 for reps in reps_counter)
    print(answer)