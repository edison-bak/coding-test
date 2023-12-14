#format 응용 ,2진수 변환과 빈공간 채우기

def solution(n, arr1, arr2):
    answer = []
    tem=[]
    tem2=''
    
    for i in range(len(arr1)):
        # 0이 최대 n자리 들어있는 이진수로 변환 후 연산
        tem.append(format(arr1[i] | arr2[i],'0{0}b'.format(n)))
        for j in range(n):
            if tem[i][j]=='1':
                tem2 +='#'
            else:
                tem2 +=' '
        answer.append(tem2)
        tem2=''
    return answer