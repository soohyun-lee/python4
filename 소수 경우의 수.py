from random import shuffle
import itertools
def first(x):
    print(sum(x[i]))
n = int(input('생성 갯수를 입력하세요'))
i = []
listdata = []
var = [x + 1 for x in range(1001)]
for j in range(n):
        shuffle(var)
        num = var.pop()
        i.append(num)
print('생성된 난수:', i)
p = itertools.permutations(i,3) #n개의 숫자 중 3개의 숫자를 뽑는 순열
q = list(p)
print(q)
new_q = list(set([tuple(set(q)) for q in q])) # 튜플 중복값 제거
print(new_q)
# length = len(q)) # 튜플 갯수
for i in range(0,len(new_q)):
    first(new_q)