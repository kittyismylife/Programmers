def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    
    total_sum = sum(range(start, end + 1))
    return total_sum

