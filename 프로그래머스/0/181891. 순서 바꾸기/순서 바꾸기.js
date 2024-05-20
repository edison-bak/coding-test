function solution(num_list, n) {
    var answer = [];
    // num_list.length 번 만큼만 동작
    // n 이후 값 삽입
    // 처음으로 돌아감
    var start =n;
    var i=0;
    if (n==num_list.length){
        start =0;
    }
    while (i<num_list.length){
        answer.push(num_list[start]);
        i++;
        start++;
        if (start>=num_list.length && n!=0){
            start=0;
        }
        // console.log(i,start,num_list[start]);
    }
    return answer;
}