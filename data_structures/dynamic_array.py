'''
https://www.hackerrank.com/challenges/dynamic-array/
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import os

def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    result = []
    lastAnswer = seq = 0
    for q in queries:
        seq = (q[1] ^ lastAnswer) % n
        if q[0] == 1:
            seqList[seq].append(q[2])
        else:
            lastAnswer = seqList[seq][q[2]%len(seqList[seq])]
            result.append(lastAnswer)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = raw_input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    queries = []
    for _ in range(q):
        queries.append(list(map(int, raw_input().rstrip().split())))
    result = dynamicArray(n, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
