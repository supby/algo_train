'''
1. Having a non-empty array of non-negative integers of length N, you need to return the maximum sum of subset of array elements such that you never take any two adjacent elements.

1 <= N <= 10^9

Example 1: input - [1,2,3,1], output - 4. You take 1st and 3rd elements

Example 2: input - [2,7,9,3,1], output - 12. You take 1st, 3rd and 5th elements
'''

def get_sum(arr: []) -> int:
    len_arr = len(arr)

    if len_arr == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    if len_arr == 3:
        return arr[0] + arr[2] if arr[0] + arr[2] > arr[1] else arr[1]

    i = 0 if arr[0] + arr[2] > arr[1] + arr[3] else 1

    cur_sum = arr[i]

    while i < len_arr:
        next_i = i + 2

        if next_i >= len_arr:
            break    

        if next_i+1 < len_arr and cur_sum + arr[next_i+1] > cur_sum + arr[next_i]:
            next_i += 1

        cur_sum = cur_sum + arr[next_i]
        i = next_i

    return cur_sum


print(get_sum([1,2,3,1])) # res: 4
print(get_sum([2,7,9,3,1])) # res: 12
print(get_sum([2,7,9,31,1])) # res: 38
print(get_sum([2,7,9,31,1, 2,7,9,311,1])) # res: 356
    

    


    
        
