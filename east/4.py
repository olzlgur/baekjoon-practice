def find_next_alarm(alarm_ban, alarm_time):
    # 알람 금지 시간을 분 단위로 변환
    ban_ranges = []
    for ban in alarm_ban:
        start, end = ban.split('~')
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))

        start_minutes = start_hour * 60 + start_minute
        end_minutes = (end_hour + 24) * 60 + end_minute if end_hour < start_hour else end_hour * 60 + end_minute

        ban_ranges.append((start_minutes, end_minutes))

    # 알람을 보내고 싶은 시간을 분 단위로 변환
    hour, minute = map(int, alarm_time.split(':'))
    alarm_minutes = hour * 60 + minute

    # 알람을 보낼 수 있는 가장 빠른 시간 찾기
    next_alarm = alarm_minutes
    while True:
        overlapping = False
        for start, end in ban_ranges:
            if start <= next_alarm <= end:
                overlapping = True
                next_alarm = end

                # 알람 금지 시간이 자정을 넘어가는 경우
                if next_alarm >= 24 * 60:
                    next_alarm -= 24 * 60
                break

        if not overlapping:
            break

    # 24시간을 초과할 경우 00:00으로 변환
    next_hour = next_alarm // 60
    next_minute = next_alarm % 60
    if next_hour >= 24:
        next_hour -= 24

    next_alarm_time = f"{next_hour:02d}:{next_minute:02d}"

    # 알람을 아예 보낼 수 없는 경우 판별
    if next_alarm_time == alarm_time and all(next_alarm_time in ban for ban in alarm_ban):
        return "Cannot set alarm"

    return next_alarm_time

print(1)
print(find_next_alarm(["22:30~23:40", "23:05~00:45"], "23:00"))
print(2)