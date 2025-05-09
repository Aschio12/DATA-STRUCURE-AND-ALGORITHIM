nums = [3, 3]
target = 6

temp = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: x[0])

l, r = 0, len(temp) - 1

while l < r:
    current_sum = temp[l][0] + temp[r][0]
    if current_sum == target:
        # Return the original indices from the tuples
        print([temp[l][1], temp[r][1]])
        break
    elif current_sum > target:
        r -= 1
    else:
        l += 1