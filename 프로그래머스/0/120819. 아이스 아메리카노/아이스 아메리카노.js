function solution(money) {
    var answer = [0,0];
    var moneyS = String(money);
    var num = parseInt(moneyS.replace(/\D/g, ''));
    // num을 5500으로 나눈 몫을 answer[0]에 저장
    answer[0] = Math.floor(num / 5500);
    
    // num을 5500으로 나눈 나머지를 answer[1]에 저장
    answer[1] = num % 5500;
    
    return answer;
}