import heapq

def solution(n, info):
    answer = -1
    heap = []
    distance = [100000*n]*(n+1)
    for inf in info:
        if inf[0] == 1:
            heapq.heappush(heap, (inf[1], inf[2]))
    
    while heap:
        goal, time = heapq.heappop(heap)
        if goal == n:
            if answer == -1:
                answer = time
            else:
                answer = min(answer, time)

        for inf in info:
            if inf[0] == goal:
                if time % (inf[2]*2) == 0:
                    if time + inf[2] < distance[inf[1]]:
                        heapq.heappush(heap, (inf[1], time + inf[2])) 
                        distance[inf[1]] = time + inf[2]
                else:
                    if time + inf[2] + (inf[2]*2-time % (inf[2]*2)) < distance[inf[1]]:
                        heapq.heappush(heap, (inf[1], time + inf[2] + (inf[2]*2-time % (inf[2]*2)))) 
                        distance[inf[1]] = time + inf[2] + (inf[2]*2-time % (inf[2]*2))
            elif inf[1] == goal:
                if time % inf[2] == 0:
                    if time + inf[2] < distance[inf[0]]:
                        heapq.heappush(heap, (inf[0], time + inf[2])) 
                        distance[inf[0]] = time + inf[2]
                else:
                    if time + inf[2] + (inf[2]*2-time % (inf[2]*2) - inf[2]) < distance[inf[0]]:
                        heapq.heappush(heap, (inf[0], time + inf[2] + (inf[2]*2-time % (inf[2]*2) - inf[2]))) 
                        distance[inf[0]] = time + inf[2] + (inf[2]*2-time % (inf[2]*2) - inf[2])
    return answer
    