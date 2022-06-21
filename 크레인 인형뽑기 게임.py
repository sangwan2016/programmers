def solution(board, moves):
    answer = 0
    stack = []
    #2차원 리스트를 전치함
    list1 = list(map(list, zip(*board)))
    #각 리스트를 0을 제거하고 역순으로 배열한후 map에 맞게 배치 
    for i in range(len(list1)):
        num_zero = list1[i].count(0)
        for j in range(num_zero):
            list1[i].remove(0)
        list1[i].reverse()
    #인형뽑기
    for n in moves:
        print(answer)
        if len(list1[n-1]) != 0:
            stack.append(list1[n-1].pop())
            while len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                else:
                    break
    return answer
