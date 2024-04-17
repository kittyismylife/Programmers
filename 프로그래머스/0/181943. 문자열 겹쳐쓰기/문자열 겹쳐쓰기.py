def solution(my_string, overwrite_string, s):
    # 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼다.
    my_string = list(my_string)
    for i in range(len(overwrite_string)):
        my_string[s + i] = overwrite_string[i]
    
    return ''.join(my_string)

