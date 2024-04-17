# def solution(str1, str2):
#     mix1 = list(str1)
#     mix2 = list(str2)
#     mix3 = list(str1 + str2)
#     answer = []
    
#     min_length = min(len(mix1), len(mix2))
#     for i in range(min_length):
#         answer.append(mix1[i])
#         answer.append(mix2[i])
    
#     return ''.join(answer)


def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer