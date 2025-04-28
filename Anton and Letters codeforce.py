sett = input()
sett = sett.replace("{", "").replace("}", "").replace(",", " ").replace(" ","")
ans=set(sett)
print(len(ans))