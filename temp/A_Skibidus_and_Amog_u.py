for _ in range(int(input())):
    s=input()
    if len(s)>2:
        print(s[:-2]+"i")
    elif s=="us":
        print("i")
    else:
        print(s+"i")