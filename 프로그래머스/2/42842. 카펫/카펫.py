def solution(brown, yellow):
    total = brown + yellow
    
    for i in range(1, int(total**0.5) + 1):
        #약수일경우 and 빨간색타일 격자수 일치
        if total % i == 0 and (i-2) * (total//i-2) == yellow:
            #큰쪽을 가로, 작은쪽을 세로로한다.
            return [max(i, total//i), min(i, total//i)]
    
#     # 기본 컨셉 : 가로와 높이가 늘어나는 규칙을 본다.
#     # 높이는 3부터시작 yellow이 4 9 16 자연수의 제곱마다 +1(높이)
#     # 가로는 3부터시작 brown이 10 12 14 2씩늘어날때마다. +1(가로)
#     # brown, yellow 값 정해졌으니 이를 이용, 높이가 늘어나는경우
#     # 가로가 늘어나는 경우를 나눈다. for문으로 가로랑 높이를 +해준다.
#     answer = [3,3]
    
#     # 카펫 최소의 8개 1개의 경우 3,3 반환
#     if brown==8 and yellow==1:
#         return answer
    
#     # yellow가 자연수의 제곱일때 높이가 +1씩 늘어남 
#     for i in range(2,yellow+1):
#         if i**(1/2)==int(i**(1/2)):
#             answer[1]+=1
    
#     # brown가 2 증가시마다 가로가 1씩 늘어남
#     for i in range(10,brown+1,2):
#         answer[0]+=1
    
#     # 높이가 늘어나는 경우는 가로가 증가하지 않아서 마지막에 빼줌, 3은 기본높이
#     answer[0]-=answer[1]-3
#     return answer