for _ in range(int(input())):
    l = int(input())
    p = list(input())

    letters = []
    digits = []

    for ch in p:
        if ch.isdigit():
            digits.append(int(ch))
        else:
            if not ch.islower():
                print("NO")
                break
            letters.append(ch)
    else:
        if letters != sorted(letters) or digits != sorted(digits):
            print("NO")
            continue

        found_digit = False
        valid = True
        for ch in p:
            if ch.isdigit():
                found_digit = True
            elif found_digit and ch.isalpha():
                valid = False
                break

        print("YES" if valid else "NO")
