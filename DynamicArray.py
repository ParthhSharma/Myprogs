#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = []
    for _ in range(n):
        seqList.append([])
    # print(seqList)
    result = []
    for query in queries:
        if query[0] == 1:
            ndx = ((query[1]^lastAnswer)%n)
            seqList[ndx].append(query[2])
        else:
            ndx = ((query[1]^lastAnswer)%n)
            ndx2 = query[2]%(len(seqList[ndx]))
            lastAnswer = seqList[ndx][ndx2]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
