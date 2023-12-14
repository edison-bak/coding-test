def solution(a, b):
    answer = 0
    for a,b in zip(a,b):
        answer+=a*b
    return answer

'''
zip 함수의 기본적인 사용 예시입니다:

python
Copy code
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

print(list(zipped))
위의 코드는 numbers와 letters 두 개의 리스트를 zip 함수로 묶어줍니다. zip 함수는 첫 번째 요소인 1과 a를 묶고, 두 번째 요소인 2와 b를 묶으며, 세 번째 요소인 3과 c를 묶어 튜플로 반환합니다. list(zipped)를 통해 반환된 값을 리스트로 변환하여 출력하면 [(1, 'a'), (2, 'b'), (3, 'c')]와 같은 결과가 나옵니다.

zip 함수는 주로 여러 개의 리스트나 이터러블 객체를 병렬로 처리하거나 묶을 때 사용됩니다. 예를 들어, 두 개의 리스트에서 같은 인덱스에 위치한 요소들을 하나씩 가져와 처리하거나, 여러 개의 리스트를 동시에 반복하며 요소들을 조합하는 등의 용도로 활용할 수 있습니다.

zip을 쓰는게 효율적인 예
# 두 개의 리스트
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# 이름이 4글자 이상이고 나이가 30 이상인 사람들의 이름 리스트
filtered_names = [name for name, age in zip(names, ages) if len(name) >= 4 and age >= 30]

print(filtered_names)
'''