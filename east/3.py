def solution(noti_time, do_not_disturb):
    answer = [0, 0]

    hour, minute = map(int, noti_time.split(":"))
    alarm = hour * 60 + minute
    disturbTime = []

    # 방해 금지 시간 정수 변환 수 리스트 생성
    for disturb in do_not_disturb:
        startDis, endDis = disturb.split("~")
        startHour, startMinute = map(int, startDis.split(":"))
        start = startHour * 60 + startMinute
        
        endHour, endMinute = map(int, endDis.split(":"))
        
        # 종료 시간이 시작 시간보다 작은 경우 00시를 넘어간 것에 대한 처리 진행
        if endHour < startHour or (startHour == endHour and endMinute < startMinute):
            endHour += 24

        end = endHour * 60 + endMinute
        disturbTime.append((start, end))
    
    count = 0
    while True:
        flag = False

        for start, end in disturbTime:

            # start, end 범위에 포함되거나 00시를 넘어간 end보다 작은 경우
            if start <= alarm < end or (24*60 <= end and alarm < (end - 24*60)) :
                alarm = end
                
                # 방해 금지 시간에 걸린 것에 대한 플래그 체크
                flag = True

                # 변경된 시간이 24시간을 넘어가는 경우
                if alarm >= 24 * 60:
                    alarm -= 24 * 60
                break

        count += 1

        # 방해 금지 시간에 걸리지 않으면 종료
        if flag == False:
            break

        # 방해 금지 시간에 방해 금지 리스트의 길이 이상으로 걸린 경우 impossible 반환
        if len(do_not_disturb) < count:
            return "impossible"

    alarmHour, alarmMin = (alarm // 60), (alarm % 60)
    if alarmHour >= 24:
        alarmHour -= 24

    return f"{alarmHour:02d}:{alarmMin:02d}"
