T = int(input())

for case in range(T):
    n , limit = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    assert (len(arr) == n)

    count = 0

    count_limit = 0
    count_less_equal_half = 0
    count_greater_half = 0

    max_less_equal_half = -1
    min_greater_half = 50000
    impossible = False

    for num in arr:
        if num > limit:
            impossible = True
            break
        elif num == limit:
            count_limit+= 1
        elif num <= limit//2:
            count_less_equal_half+= 1
            max_less_equal_half = max(num, max_less_equal_half)
        elif num > limit//2:
            count_greater_half+= 1
            min_greater_half = min(num, min_greater_half)
    
    if impossible:
        print('impossible')
        continue

    count = count_limit + count_greater_half

    if count_less_equal_half > 0 and ((min_greater_half + max_less_equal_half) > limit):
        count+= 1

    print(count)
