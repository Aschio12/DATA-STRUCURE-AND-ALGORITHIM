for _ in range(int(input())):
    n, sh, sm = map(int, input().split())  
    min_minutes = 24 * 60  
    for _ in range(n):
        ah, am = map(int, input().split())  
        current_minutes = sh * 60 + sm
        alarm_minutes = ah * 60 + am

        if alarm_minutes < current_minutes:
            alarm_minutes += 24 * 60

        wait_minutes = alarm_minutes - current_minutes

        min_minutes = min(min_minutes, wait_minutes)

    hours = min_minutes // 60
    minutes = min_minutes % 60
    print(f"{hours} {minutes}")
