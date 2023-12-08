def solution(n):
    s=str(n)
    f_half=sum([int(x) for x in list(s[0:int(len(s)/2)])])
    s_half=sum([int(x) for x in list(s[int(len(s)/2):len(s)])])
    return f_half==s_half
