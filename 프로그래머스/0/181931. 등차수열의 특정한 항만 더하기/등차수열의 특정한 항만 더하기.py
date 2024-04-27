def solution(a, d, included):
    total = 0
    
    for i in range(len(included)):
        if included[i] == True:
            total += a + (d * i)            
    return total

