def solution(s):
    digit = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in digit.keys():
        s = s.replace(k, digit[k])
    answer = int(s)
    return answer
