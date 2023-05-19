
def organizingContainers(container):
    count = len(container)
    check = [0]*count
    check2 = []
    answer = [0]*count

    for c in container:
        for i in range(count):
            check[i] += c[i]

    for i in range(count):
        for j in range(count):
            if j not in check2 and sum(container[j]) == check[i]:
                answer[i] += 1
                check2.append(j)
    if count == sum(answer):
        return "Possible"
    return "Impossible"


q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    container = []

    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))

    result = organizingContainers(container)
    print(result)