def solution(number, n, m):
    # 이렇게 하면 최소공배수의 오류에 걸림 (test case 2)
    # return int(not(number%(n*m)))
    
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0