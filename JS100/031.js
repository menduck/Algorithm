/*
다음 배열 내장함수의 시간 복잡도가 O(1)이 아닌 것을 모두 고르시오.

1)  arr[i]
2)  arr.push(5)
3)  arr.slice()
4)  arr.pop()
5)  arr.includes(5)

3. arr.slice() 

begin부터 end(end 미포함)까지 복사본을 새로운 배열 객체로 반환한다.
그렇기 때문에 배열의 길이에 따라 실행 시간이 길어지기 때문에 시간 복잡도는 O(n)이다.O

5. arr.includes(5)
includes() 메서드는 배열이 특정 요소를 포함하고 있는지 판별한다.
includes(5)는 arr의 배열 요소를 처음부터 5가 나올때까지 실행 만일 5가 배열의 끝에 있다면 배열의 길이만큼 실행 시간이 길어지기 때문에 시간 복잡도는 O(n)이다.

*/
