def solution(code):
    mode = 0  # 초기 mode는 0
    ret = ""  # 반환할 문자열 ret 초기화

    for idx in range(len(code)):
        if mode == 0:  # mode가 0일 때
            if code[idx] != "1":  # code[idx]가 "1"이 아닌 경우
                if idx % 2 == 0:  # idx가 짝수일 때만 ret에 추가
                    ret += code[idx]
            else:  # code[idx]가 "1"인 경우
                mode = 1  # mode를 0에서 1로 변경
        else:  # mode가 1일 때
            if code[idx] != "1":  # code[idx]가 "1"이 아닌 경우
                if idx % 2 == 1:  # idx가 홀수일 때만 ret에 추가
                    ret += code[idx]
            else:  # code[idx]가 "1"인 경우
                mode = 0  # mode를 1에서 0으로 변경
    
    if ret == "":  # ret가 빈 문자열인 경우
        return "EMPTY"
    else:
        return ret