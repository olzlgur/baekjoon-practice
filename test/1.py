def solution(histogram):
    answer = 1
    case = [[0, 0] for _ in range(len(histogram[0]))]

    for y in range(len(histogram)):
        for x in range(len(histogram[0])):
            # 채워진 칸이 등장한적 없는 경우
            if case[x][1] != 1:
                if histogram[y][x] == 0:
                    # 비워진 칸이 나오면 case 초기화
                    case[x] = [0, 0]
                elif histogram[y][x] == 1:
                    # 채워진 칸이 나온 경우
                    case[x][1] = 1
                    if case[x][0] == 0:
                        # 이전에 손상된 칸이 나온적 없으면 경우의 수 1로 마무리
                        case[x][0] = 1
                    else:
                        # 손상된 칸이 나온적 있으면 경우의 수 +1
                        case[x][0] += 1
                else:
                    # 손상된 칸이 나온경우 경우의 수 +1
                    case[x][0] += 1
    for li in case:
        if li[0] != 0:
            if li[1] == 0:
                # 손상된 칸만 경우의 수에 포함된 경우
                answer *= (li[0]+1)
            else:
                answer *= li[0]      

    return answer

