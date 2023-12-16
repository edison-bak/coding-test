def solution(a, b, n):
    tem=0
    while n>=a:
        tem+=(n//a)*b
        n=(n//a)*b+n%a
    return tem