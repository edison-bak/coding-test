function solution(my_string, is_prefix) {
    var answer = '';
    for (var i=0; i<my_string.length; i++){
        answer+=my_string[i];
        if (answer==is_prefix){
            return 1;
        }
    }
    return 0;
}