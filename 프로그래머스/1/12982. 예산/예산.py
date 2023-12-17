def solution(d, budget):
    answer = 0
    tem=0
    d.sort()
    for i in range(0,len(d)):
        tem+=d[i]
        if tem>budget:
            break
        answer +=1 
    return answer