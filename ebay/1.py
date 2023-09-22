from collections import deque
def solution(noti_time, do_not_disturb):
    answer = ''
    q = deque()
    visited = [0]*len(do_not_disturb)
    notiHour, notiMin = map(int, noti_time.split(":"))
    q.append((notiHour, notiMin))
    flag = 0
    while q:
        hour, minute = q.popleft()

        for idx in range(len(do_not_disturb)):
            startTime, endTime = do_not_disturb[idx].split("~")
            startHour, startMin = map(int, startTime.split(":"))
            endHour, endMin = map(int, endTime.split(":"))
            if visited[idx] == 0 and endHour < startHour or (endHour == startHour and endMin < startMin):
                if startHour < hour or (startHour == hour and startMin <= minute) or hour < endHour or (hour == endHour and minute < endMin):
                    q.append((endHour, endMin))
                    visited[idx] = 1
            elif visited[idx] == 0 and (startHour < hour or (startHour == hour and startMin <= minute)) and  (hour < endHour or (endHour == hour and minute < endMin)):
                visited[idx] = 1
                q.append((endHour, endMin))

    for idx in range(len(do_not_disturb)):
        startTime, endTime = do_not_disturb[idx].split("~")
        startHour, startMin = map(int, startTime.split(":"))
        endHour, endMin = map(int, endTime.split(":"))
        if endHour < startHour or (endHour == startHour and endMin < startMin):
            if startHour < hour or (startHour == hour and startMin <= minute) or hour < endHour or (hour == endHour and minute < endMin):
                flag = 1 
                break
        elif (startHour < hour or (startHour == hour and startMin <= minute)) and  (hour < endHour or (endHour == hour and minute < endMin)):
            flag = 1
            break
    if flag == 1:
        return "impossible"
    
    return ("0"+str(hour))[-2:]+":"+("0"+str(minute))[-2:]