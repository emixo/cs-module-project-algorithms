'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    mnums = []
    increment = 0
    while increment < len(nums):
        window = nums[increment:k+increment]
        maxnum = window[0]
        if len(window) == k:
            for num in window:
                if num > maxnum:
                    maxnum = num
            mnums.append(maxnum)
        print(window)
        increment +=1
    return mnums



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
