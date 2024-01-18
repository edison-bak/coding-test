def solution(name, yearning, photo):
    tem={}
    answer = []
    for i in range(0,len(name)):
        tem[name[i]]=yearning[i]
    
    for i in range(0,len(photo)):
        a=0
        for j in range(0,len(photo[i])):
            if photo[i][j] in tem:
                a+=tem[photo[i][j]]
        answer.append(a)
        
    return answer