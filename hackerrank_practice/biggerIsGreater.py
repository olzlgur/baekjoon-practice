#!/bin/python3

import math
import os
import random
import re
import sys
import heapq, copy

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.

def biggerIsGreater(w):
    heap = []
    heap2 = []
    answer = []
    word = list(w)
    
    heapq.heappush(heap, word[len(word)-1])
    maxStr = word[len(word)-1]

    for i in range(len(word)-2, -1, -1):
        if word[i] < maxStr:
            while heap:
                v = heapq.heappop(heap)
                if word[i] < v:
                    heapq.heappush(heap2, word[i])
                    answer = copy.deepcopy(word[:i])
                    answer.append(v)
                    while heap:
                        heapq.heappush(heap2, heapq.heappop(heap))
                    while heap2:
                        v = heapq.heappop(heap2)
                        answer.append(v)
                    return "".join(answer)
                else:
                    heapq.heappush(heap2, v)
        heapq.heappush(heap, word[i])
        # print(maxStr)
        maxStr = max(maxStr, word[i])
    return "no answer"
    # Write your code here

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
        # fptr.write(result + '\n')

    # fptr.close()