def solution(N):
    # 숫자를 문자열로 변환하여 각 자릿수를 분리하고 합을 구합니다.
    digit_sum = sum(int(digit) for digit in str(N))
    return digit_sum
