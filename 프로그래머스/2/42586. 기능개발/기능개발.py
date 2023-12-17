import math

def solution(progresses, speeds):
    answer = []
    max=0    

    for i in range(0,len(progresses)):
        if max>=math.ceil((100 - progresses[i]) / speeds[i]):
            answer[-1]+=1
        else:
            max=math.ceil((100 - progresses[i]) / speeds[i])
            answer.append(1)
    return answer