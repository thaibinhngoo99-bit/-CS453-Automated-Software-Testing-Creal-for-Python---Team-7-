def picking_number(n, arr):
    max_combinations = 0
    for i in range(n):
        combination = arr.count(arr[i]) + arr.count(arr[i] + 1)
        if combination > max_combinations:
            max_combinations = combination
    return max_combinations