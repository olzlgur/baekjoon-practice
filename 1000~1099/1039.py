# 문제
# 0으로 시작하지 않는 정수 N이 주어진다. 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

# 1 ≤ i < j ≤ M인 i와 j를 고른다. 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 이때, 바꾼 수가 0으로 시작하면 안 된다.
# 위의 연산을 K번 했을 때, 나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N과 K가 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, K는 10보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 문제에 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력한다. 만약 연산을 K번 할 수 없으면 -1을 출력한다.

# 예제 입력 1  복사
# 16375 1
# 예제 출력 1  복사
# 76315
# 예제 입력 2  복사
# 132 3
# 예제 출력 2  복사
# 312
# 예제 입력 3  복사
# 432 1
# 예제 출력 3  복사
# 423
# 예제 입력 4  복사
# 90 4
# 예제 출력 4  복사
# -1
# 예제 입력 5  복사
# 5 2
# 예제 출력 5  복사
# -1
# 예제 입력 6  복사
# 436659 2
# 예제 출력 6  복사
# 966354

import sys, copy

input = sys.stdin.readline

N, K = map(int, input().split())

NL = list(map(int, str(N)))

Nlen = len(NL)
heap = []
answer = 0

heap.append((NL, 0, 0))

cnt = 0
left = 0

if Nlen == 1:
    print(-1)
elif Nlen == 2 and NL[-1] == 0:
    print(-1)
else:
    while heap:
        TL, left, cnt = heap.pop(0)

        if left < Nlen-1:
            heap.append((TL, left+1, cnt))
        
        if left < Nlen-2 and cnt != K:
            mL = []
            maxNum = 0

            for i in range(Nlen-1, left, -1):
                if TL[left] <= TL[i]:
                    if maxNum < TL[i]:
                        mL = []
                        mL.append(i)
                        maxNum = TL[i]
                    elif maxNum == TL[i]:
                        mL.append(i)
                
            if len(mL) != 0:
                for index in mL:
                    TL2 = copy.deepcopy(TL)
                    temp = TL2[left]
                    TL2[left] = TL2[index]
                    TL2[index] = temp
                    heap.append((copy.deepcopy(TL2), left+1, cnt+1))

        if cnt == K:
            answer = max(answer, int("".join(map(str, TL))))
        elif left == Nlen -1:
            if (K - cnt) % 2 == 0:
                answer = max(answer, int("".join(map(str, TL))))
            else:
                temp = TL[-1]
                TL[-1] = TL[-2]
                TL[-2] = temp
                answer = max(answer, int("".join(map(str, TL))))
            
    print(answer)

