from collections import deque

def appendLeftParenthesis(times, target):
    return target + '(' * times


def appendRightParenthesis(times, target):
    return target + ')' * times


def appendValue(value, target):
    return target + str(value)


def solution(testCases):
    answer = []
    
    for i in range(testCases):
        stack = deque()
        depths = deque(map(lambda x: int(x), list(input())))
        depths.reverse()

        currentDepth = 0
        answerString = ''

        while depths:
            stack.append(depths.pop())
            
            if stack[-1] == 0 and currentDepth == 0:
                answerString = appendValue(stack.pop(), answerString)

            elif stack[-1] > currentDepth:
                answerString = appendLeftParenthesis(stack[-1] - currentDepth, answerString)
                answerString = appendValue(stack[-1], answerString)
                currentDepth = stack.pop()

            else:
                answerString = appendRightParenthesis(currentDepth - stack[-1], answerString)
                answerString = appendValue(stack[-1], answerString)
                currentDepth = stack.pop()
        
        while currentDepth > 0:
            answerString = appendRightParenthesis(currentDepth, answerString)
            currentDepth = 0
        answer.append(answerString)

    return answer


if __name__ == '__main__':
    testCases = int(input())
    
    values = solution(testCases)

    for index, value in enumerate(values):
        print('Case #{}: {}'.format(index + 1, value))