# 점프와 순간이동

# 문제풀이
'''
- 2의 제곱수들은 사용량이 1이다.
    - 한 칸 점프하고 한 칸 순간이동하면 (현재까지 온 거리:2) n까지 계속 순간이동으로 갈 수 있다.

- 2로 나누어 떨어지지 않을때까지 n을 2로 나누고 n을 재할당한다.
    - 사용량 1을 더해주고 (1칸을 움직이기 위해서)
    - n-1의 사용량을 구한다.
- 위 과정들을 반복해서 사용량을 더해 반환한다.

'''
# solution - 성공/ 재귀함수
def solution(n):
    while n%2 == 0:
        n = n//2
    ans = 0
    if n == 1:
        return 1
    else:
        ans += 1
        return solution(n-1) + ans 
        
# solution2  - 재귀X
def solution(n):
    jump = 0 # 점프 횟수
    while n:
        if n % 2 == 0: # n이 짝수이면
            n //= 2 # 2로 나눈 몫을 할당한다.
        else: # n이 홀수이면
            jump += 1 # 무조건 한칸은 점프해야한다.
            n -= 1
    return jump