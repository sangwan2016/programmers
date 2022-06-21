def solution(new_id):
    rem = ['-','_','.']
    for i in range(len(new_id)):
        if new_id[i].isupper() == True:
            new_id = new_id[:i] + new_id[i].lower() + new_id[i+1:]
    """
    new_id2 = ''
    for x in new_id:
        if x in rem or x.isalpha() == True:
            new_id2 = new_id2 + x
    """
    new_id = ''.join(x for x in new_id if x in rem or x.isalnum() == True)
    while new_id.find("..") != -1:
        new_id = new_id.replace("..",'.')
    new_id = new_id.strip('.')

    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        while len(new_id) < 3:
            #new_id = new_id[:] + new_id[len(new_id)-1]
            new_id = new_id + new_id[-1]
        return new_id
    answer = new_id
    return answer
