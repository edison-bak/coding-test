function solution(my_string, is_suffix) {
    var answer = '';
    my_string=my_string.split('').reverse().join('');
    is_suffix=is_suffix.split('').reverse().join('');
    for (var i=0; i<my_string.length; i++){
        answer+=my_string[i];
        if (answer==is_suffix){
            return 1;
        }
    }
    return 0;
}