# _*_ coding:utf-8 _*_
""" This is for excercises 4.1-2.
    Use a brute-force method which run in Θ(n2) time
"""
def max_subarray(A):
    (max_left, max_right, max_s) = (0, 0, -float("inf"))
    for i in range(len(A)-1):
        s = A[i]
        for j in range(i+1, len(A)):
            s += A[j]
            if s > max_s:
                max_s = s
                max_left = i
                max_right = j
    return [max_left, max_right, max_s]

# test
A = [1, -3, 2, 4, -5, 6, 1]
print max_subarray(A)

