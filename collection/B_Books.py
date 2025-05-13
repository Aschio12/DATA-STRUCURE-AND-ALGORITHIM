n, k = map(int, input().split())
arr = list(map(int, input().split()))
time = 0
l = r = 0
count = 0

while r < len(arr):
    time += arr[r]
    while time > k:
        time -= arr[l]
        l += 1
    count = max(count, r - l + 1)
    r += 1

print(count)
