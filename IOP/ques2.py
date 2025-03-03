def max_subarray_sum(arr):
    if not arr:
        return 0
        
    current_max = global_max = arr[0]
    
    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        global_max = max(global_max, current_max)
        
    return global_max

arr = [3,3,-8,7,-1,2,3]
print(max_subarray_sum(arr))