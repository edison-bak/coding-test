function solution(n, k) {
    var answer = [];
    for (var i=0; i<=n; i+=k){
        if (i==0){
            continue;
        }
        answer.push(i);
    }
    return answer;
}