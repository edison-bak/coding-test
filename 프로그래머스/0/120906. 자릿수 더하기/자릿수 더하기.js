function solution(n) {
    var answer = 0;
    var st=String(n);
    // console.log(typeof st);
    for (var i=0; i<st.length; i++){
        answer+=parseInt(st[i]);
    }
    return answer;
}