# _*_ coding: utf-8 _*_

""" Use divide-and-conquer algorithm to solve maximum-subarray proble
    The algorithm can be found on page 72 in the 4th chapter of CLRS
    This algorithm is Θ(nlgn) """

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -float("inf")
    s = 0
    for i in range(mid,low-1, -1):
        s = s + A[i]
        if s > left_sum:
            left_sum = s
            max_left = i
    right_sum = -float("inf")
    s = 0
    for i in range(mid+1, high+1):
        s = s + A[i]
        if s > right_sum:
            right_sum = s
            max_right = i
    return [max_left, max_right, left_sum + right_sum]

def find_maximum_subarray(A, low, high):
    if low == high:
        return [low, high, A[low]]
    else:
        mid = (low + high) / 2
        [left_low, left_high, left_sum] = find_maximum_subarray(A, low, mid)
        [right_low, right_high, right_sum] = find_maximum_subarray(A, mid+1, high)
        [cross_low, cross_high, cross_sum] = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return [left_low, left_high, left_sum]
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return [right_low, right_high, right_sum]
        else:
            return [cross_low, cross_high, cross_sum]

#print find_max_crossing_subarray([1, -1, 2, 3, -5], 0, 2, 4)
print find_maximum_subarray([1, -3, 2, 4, -5, 6, 1], 0, 6)
