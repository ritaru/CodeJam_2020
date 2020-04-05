import sys

def solution(testCases):
    binarySize = int(testCases[1])
    testCases = int(testCases[0])
    
    for i in range(testCases):
        binaryValue = 0
        if binarySize <= 10:
            for s in range(binarySize):
                print(s + 1, flush=True)
                binaryValue = binaryValue | int(input()) << binarySize - s -1
            print('{0:010b}'.format(binaryValue), flush=True)
        else:
            pass

        qualified = input()
        if qualified == 'Y':
            continue
        else:
            sys.exit()
            
        

if __name__ == '__main__':
    testCases = input().split()
    solution(testCases)