def solution(num_list):
    total_mul = 1
    total_sum = 0
    
    for i in num_list:
        total_mul *= i
    for i in num_list:
        total_sum += i
        
    if total_mul < (total_sum ** 2):
        return 1
    else:
        return 0