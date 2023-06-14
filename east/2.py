def solution(queue):
    answer = [0, 0, 0]
    count = [0]*3
    left = 0 

    for num in queue:
        count[num-1] += 1
    
    while True:
        # 모든 요소의 개수가 같을시 종료
        if max(count) == min(count):
            break

        # 가장 적은 요소의 개수 할당
        minCount = min(count)

        for num in [1, 2, 3]:
            # 가장 적은 개수의 요소 탐색 후 추가
            if count[num-1] == minCount:
                queue.append(num)
                answer[num-1] += 1
                count[num-1] +=1
                break
        
        # 가장 왼쪽의 개수 감소
        count[queue[left]-1] -= 1
        left += 1
        
    return answer
