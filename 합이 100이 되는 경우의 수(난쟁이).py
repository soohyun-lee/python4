#합이 100이 되는 경우의 수는 많음
# 수정전
from itertools import combinations
n = ""
new = []

print('9난쟁 키를 입력해주세요. 키를 다 입력하면 "0"를 눌러주세요:')
while n != 0:
    n = int(input(''))
    new.append(n)
new.remove(0)
print(new) # 9난쟁 키 리스트 출력
seven = list(combinations(new, 7)) #7개씩 조합 출력
print(seven)
for i in range(len(seven)):
    if sum(seven[i]) == 100:
        print(seven[i])
        break
    else:
        print('합이 100이 되는 경우의 수가 되는 경우는 없습니다')

# 수정========
from itertools import combinations
n = ""
new = []

print('9난쟁 키를 입력해주세요. 키를 다 입력하면 "0"를 눌러주세요:')
while n != 0:
    n = int(input(''))
    new.append(n)
new.remove(0)
print(new) # 9난쟁 키 리스트 출력
seven = list(combinations(new, 7)) #7개씩 조합 출력
print(seven)
n = True
for i in range(len(seven)):
    if sum(seven[i]) == 100:
        n = False
        print("합이 100이 되는 경우의 수는: ", seven[i])
        break
if n:
  print('합이 100이 되는 경우의 수가 되는 경우는 없습니다')