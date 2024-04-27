def solution(n):
    sorted_str = ''.join(sorted(str(n), reverse=True))
    return int(sorted_str)