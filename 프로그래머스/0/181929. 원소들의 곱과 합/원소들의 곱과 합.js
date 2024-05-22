function solution(num_list) {
    var mul=1;
    var sum=0;
    for (var i=0; i<num_list.length;i++){
        mul*=num_list[i];
        sum+=num_list[i];
    }
    sum=sum**2
    if (mul<sum){
        return 1;    
    }
    else if (mul>sum){
        return 0;  
    }
}