def solution(s):
    s = s.lower()  # 문자열을 소문자로 변환
    count_p = s.count('p')  # 'p'의 개수 세기
    count_y = s.count('y')  # 'y'의 개수 세기

    return count_p == count_y