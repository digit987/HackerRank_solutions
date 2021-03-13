'''
https://www.hackerrank.com/challenges/birthday-cake-candles/
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import os
def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    candles_count = 1
    max_candle = candles[0]
    for i in candles[1:]:
        if i == max_candle:
            candles_count += 1
        else:
            return candles_count
    return candles_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(raw_input().strip())
    candles = map(int, raw_input().rstrip().split())
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()
