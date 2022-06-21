def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    """dic = {}
    for name in participant:
        dic[name] = 0
    for name in completion:
        dic[name] = 1
    for k in dic.keys():
        if dic[k] == 0:
            return k
    """
