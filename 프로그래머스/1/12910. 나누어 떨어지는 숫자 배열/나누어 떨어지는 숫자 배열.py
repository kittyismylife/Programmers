def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer


# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]