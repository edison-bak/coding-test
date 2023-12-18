def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x: (x*3), reverse=True)
    answer = ''.join(numbers)
    
    # 0으로만 이루어진 문자열 예외
    return str(int(answer))