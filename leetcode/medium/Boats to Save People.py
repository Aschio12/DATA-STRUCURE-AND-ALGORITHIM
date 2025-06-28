def f():
    people = [2,1]
    limit = 3
    people.sort()
    l,r,count=0,len(people)-1,0
    if people[l]>limit:
            return count
    while l<=r:
        if people[r]+people[l]<=limit:
            count+=1
            l+=1
            r-=1
        elif people[r]>limit:
            r-=1
        elif people[r]<=limit:
            count+=1
            r-=1
    return count
print(f())