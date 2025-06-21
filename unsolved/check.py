for _ in range(int(input())):
    m,a,b,c=map(int,input().split())
    max_to_seat=0
    if a<=m:
        max_to_seat+=a
    else:
        max_to_store+=m
    remaider_row_1=m-max_to_store
    if b<=m:
        to_seat=b
        max_to_seat+=to_seat
    else:
        to_seat=m
        max_to_store+=to_seat
    remainder_row_2=m-(to_seat)
    remainder_total=remaider_row_1+remainder_row_2
    if c<=remainder_total:
        max_to_store+=c
    else:
        max_to_store+=remainder_total
    print(max_to_store)