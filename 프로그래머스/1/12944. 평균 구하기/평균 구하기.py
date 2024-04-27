def solution(arr):
    i_sum = 0
    for i in arr:
        i_sum += i
        
    answer = i_sum / len(arr)
    return answer