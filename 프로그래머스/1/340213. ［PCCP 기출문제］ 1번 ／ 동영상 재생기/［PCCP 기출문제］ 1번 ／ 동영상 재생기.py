# 입력되는 시간을 모두 초로 변환 (길이의 대소를 판단하기 위함)
def toSeconds(time):
    minutes, seconds = map(int, time.split(":"))
    return minutes * 60 + seconds
    
# 초로 입력된 시간을 00:00 형식으로 변환 (최종값 출력)
def toMinSec(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = toSeconds(video_len)
    pos_sec = toSeconds(pos)
    op_start_sec = toSeconds(op_start)
    op_end_sec = toSeconds(op_end)
    
    for i in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
        if i == 'prev':
            pos_sec = max(0,pos_sec - 10 )
        elif i == 'next':
            pos_sec = min(video_len_sec, pos_sec + 10)
            
    if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
            
    return toMinSec(pos_sec)