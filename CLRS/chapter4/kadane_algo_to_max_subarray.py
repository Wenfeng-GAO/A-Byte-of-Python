# coding: utf-8
""" Kadane's algorithm consists of a scan through the array values, computing at each position the maximum(positive sum) subarray ending at that position. It's Θ(n). """

# return an array [left-index, right-index, max-sum]
def max_subarray_with_index(A):
    max_sum = latest_sum = 0
    for i in range(len(A)):
        s = latest_sum + A[i]
        if s > 0 and latest_sum == 0:
            latest_sum = s
            latest_left = latest_right = i
        elif s > 0 and latest_sum > 0:
            latest_sum = s
            latest_right = latest_right + 1
        else:
            latest_sum = 0
        if max_sum < latest_sum:
            max_sum = latest_sum
            max_left = latest_left
            max_right = latest_right
    return [max_left, max_right, max_sum]

""" if only return maximum sum, code is clearer """
# return a value
def max_subarray(A):
    max_sum = latest_sum = 0
    for a in A:
        latest_sum = max(0, latest_sum + a)
        max_sum = max(max_sum, latest_sum)
    return max_sum

# test
A = [1, -3, 2, 4, -5, 6, 1]
print max_subarray_with_index(A)
print max_subarray(A)
