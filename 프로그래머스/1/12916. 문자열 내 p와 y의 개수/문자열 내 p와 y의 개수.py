def solution(s):
    s = s.lower()  # 소문자와 대문자를 구별하지 않음
    count_p = s.count('p')
    count_y = s.count('y')

    return count_p == count_y
