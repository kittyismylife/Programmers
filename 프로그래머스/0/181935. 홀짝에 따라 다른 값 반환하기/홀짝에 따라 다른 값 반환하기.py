def solution(n):
    total = 0
    # 홀수이면 모든 양의 정수의 합을 리턴
#     if n % 2 == 1:
#         for i in range(1, n+1, 2): 
#             total += i
#         return total

#     # 짝수이면 모든 양의 정수의 제곱의 합을 리턴
#     else:
#         for i in range(2, n+1, 2): 
#             total += i**2
#         return total
    
    if n % 2:
        return sum(range(1, n+1, 2))
    return sum([i*i for i in range(2, n+1, 2)])