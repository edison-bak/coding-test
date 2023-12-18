def solution(A, B):
    answer = 0
    
    # 곱이 최소가 되려면?
    # 0이 없으니.. 정렬, 역정렬하고 곱하면?
    A.sort()
    B.sort(reverse=True)
    
    for i in range(0,len(A)):
        answer+=A[i]*B[i]
        
    return answer