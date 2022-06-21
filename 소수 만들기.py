from itertools import combinations as cb
def find_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    for k in cb(nums,3):
        if find_prime(sum(k)) == 1:
            answer += 1
    return answer
"""   answer = 0
    nums.sort()
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if find_prime(nums[i]+nums[j]+nums[k]) == 1:
                    answer += 1
"""
