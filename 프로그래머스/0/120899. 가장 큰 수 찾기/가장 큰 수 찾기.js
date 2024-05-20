function solution(array) {
    var answer = [0,0];
    var index=0;
    // 1. 가장 큰 수 구하고, 일치 하는애 찾는다.
    // 2. 돌아 가면서 실시간 큰수 대체 (Good)
    for (var i=1; i<array.length; i++) {
        if (array[i]>answer[0]){
            answer[0]=array[i]
            answer[1]=i
        }
    }
    return answer;
}