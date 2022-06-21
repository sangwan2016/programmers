def solution(numbers):
    answer = 0
    a = set(range(10))
    numbers = set(numbers)
    answer = sum(a-numbers)
    return answer
