# ver1
n = [1, 2, 3, 4, 5]
m = map(lambda x: x * x, n)
m
# mamp at 0X~~~~>
#  map 클래스에서 생산된 객체는 반복자로 실제 실행된 객체가 아님
# 리스트로 변환하려면 대괄호 안에 이 객체를 넣고 별표 붙이기
print([*m])
# [1,4,9,16,25]

# ===== 컴프리헨션=====
n = [x * x for x in n]
print(n)
> [1, 4, 9, 16, 25]
# ======================================================
# ver2
lh = [1, 4, 9, 16, 25]
f = filter(lambda x: x % 2 == 0, lh]
# f              #filter 클래스의 객체가 생성
# filter at 0x50~~~~
print([*f])  # 원소를 나열하려면 대괄호에 넣고 별표 붙여서 원소 꺼내기
# [4,16]
# ===== 컴프리헨션=====
ll = [1, 2, 3, 4, 5]
lhl = [x * x for x in ll if x % 2 == 0]
# 필터는 for문 다음에 if문을 사용해서 정의
print(lhl)
# [4,16]

# 딕셔너리 컴프리헨션
# ====== 딕셔너리 컴프리헨션 사용x ========
n = [('a', 1), ('b', 2)]  # 2개의 원소를 가진 튜플이 있음


def t(x):
    x = list(x)  # 튜플 리스트로 변환
    x[1] = x[1] * x[1]  # 첫번째 원소를 곱해서 첫번째 원소에 할당
    x = tupel(x)
    return x


d = map(lambda x: t(x), n)
print([*d])
> [('a', 1), ('b', 4)]

# ===== 딕셔너리 컴프리헨션 사용========
n = [('a', 1), ('b', 2)]
k = {x: y * y for x, y in n}
print(k)
> {'a': 1, 'b': 4}