def f():
    skill = [3,2,5,1,3,4]
    skill.sort()
    left=1
    right=len(skill)-2
    chem=skill[0]*skill[-1]
    tot=skill[0]+skill[-1]
    if skill:
        while left<right:
            if skill[left]+skill[right]==tot:
                chem+=skill[left]*skill[right]
            else:
                return -1
            left+=1
            right-=1
        return chem
    else:
        return -1
print(f())
        