# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120

def climbingLeaderboard(ranked, player):
    answer = []
    rank = list(set(ranked))
    rank.sort(reverse=True)
    # print(rank)
    for score in player:
        left, right = 0, len(rank)-1
        if score < rank[right]:
            answer.append(right+2)
        else:
            while left <= right:
                mid = (left+right) // 2
                # print(left, right, mid)
                if rank[mid] < score:
                    right = mid-1 
                elif rank[mid] > score:
                    left = mid+1
                else:
                    break
            if score < rank[mid]:
                answer.append(mid+2)
            else:
                answer.append(mid+1)
    # print(answer)


    return answer

ranked_count = int(input().strip())

ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)

print(result)