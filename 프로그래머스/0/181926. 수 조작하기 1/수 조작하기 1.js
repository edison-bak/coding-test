function solution(n, control) {
    for (var i=0; i<control.length; i++){
        if (control[i]=='w'){
            n+=1;
        }
        else if(control[i]=='a'){
            n-=10;
        }
        else if(control[i]=='s'){
            n-=1;
        }
        else {
            n+=10;
        }
    }
    return n;
}