# 문제 접근
# - n을 10으로 나눈 몫이 서비스 받은 음료수의 개수임으로
# - k개에서 그 수를 빼주고 음료수 값을 계산한다.
# - 양꼬치 값과 음료수 값의 총합을 반환한다.

# solution
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)