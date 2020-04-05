from collections import deque

def solution(testCases):
    activityTimeline = deque()
    answer = []

    for i in range(testCases):
        activityCount = int(input())
        activities = []

        for s in range(activityCount):
            activities.append(tuple(map(lambda x: int(x), input().split())) + tuple([s]))
        activities.sort()
        activityTimeline.append(activities)

    for test in activityTimeline:
        cameron = deque()
        jamie = deque()
        parentSchedule = []

        for item in test:
            if not cameron:
                parentSchedule.append(tuple(['C', item[-1]]))
                cameron.append(item)
            elif not jamie:
                parentSchedule.append(tuple(['J', item[-1]]))
                jamie.append(item)
            elif item[0] >= cameron[-1][1]:
                parentSchedule.append(tuple(['C', item[-1]]))
                cameron.append(item)
            elif item[0] >= jamie[-1][1]:
                parentSchedule.append(tuple(['J', item[-1]]))
                jamie.append(item)
            else:
                parentSchedule.clear()
                parentSchedule.append('IMPOSSIBLE')
                break

        parentSchedule.sort(key=lambda x: x[1])
        if parentSchedule[0] == 'IMPOSSIBLE':
            answer.append('IMPOSSIBLE')
        else:
            answer.append(''.join([schedule[0] for schedule in parentSchedule]))

    return answer

    


if __name__ == '__main__':
    testCases = int(input())
    values = solution(testCases)

    for index, answer in enumerate(values):
        print('Case #{}: {}'.format(index + 1, answer))