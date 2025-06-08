dorm,no_recieving_rooms=map(int,input().split())
rooms=list(map(int,input().split()))
recieving_rooms=list(map(int,input().split()))
total_rooms=sum(rooms)
ans=[]
i,k=0,0
current_room=rooms[k]
while i<no_recieving_rooms:
    if recieving_rooms[i]<=current_room:
        if k==0:
            ans.append(f"{k+1} {recieving_rooms[i]}")
        else:
            ans.append(f"{k+1} {abs(current_room-rooms[k]-recieving_rooms[i])}")
        i+=1
    else:
        k+=1
        current_room+=rooms[k]
for i in ans:
    print(i)