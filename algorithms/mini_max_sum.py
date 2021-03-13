'''
https://www.hackerrank.com/challenges/mini-max-sum
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def minMaxSum(arr):
    arr.sort()
    print sum(arr[0:4]),
    print sum(arr[-1:-5:-1])
if __name__ == '__main__':
    arr = []
    strip = raw_input().strip().split()
    for i in strip:
        arr += [int(i)]
    minMaxSum(arr)
