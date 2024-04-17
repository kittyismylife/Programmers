# def solution(a, b):
#     case1 = int(str(a)+str(b))
#     case2 = int(str(b)+str(a))
    
#     if case1 < case2:
#         return case2

#     else:
#         return case1


def solution(a, b):
    return (max(int(f"{a}{b}"),int(f"{b}{a}")))
