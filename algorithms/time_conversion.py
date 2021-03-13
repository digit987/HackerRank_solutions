'''
https://www.hackerrank.com/challenges/time-conversion/
                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import os
def timeConversion(s):
    if s[-1:-3:-1] == 'MA' and s[0:2] == '12':
        return '00' + s[2:-2]
    if s[-1:-3:-1] == 'MP'and s[0:2] != '12':
        return str(int(s[0:2]) + 12) + s[2:-2]
    return s

#print(timeConversion('01:00:00PM'))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    f.write(result+'\n')
    f.close()
