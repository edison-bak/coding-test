function solution(numbers, n) {
    var answer = 0;
    
    for (var i=0; i<numbers.length;i++){
        if (answer>n){
            return answer;
        }
        answer+=numbers[i]
    }
    return answer;
}