#진수 변환
#2진수

b = []
n = int(input('10진수:'))
while n != 0:
    b.append(n%2)
    n = n//2
b.reverse()
print('0b' + ''.join(map(str,b)))

#8진수

b = []
n = int(input('10진수:'))
while n != 0:
    b.append(n%8)
    n = n//8
b.reverse()
print('0o' + ''.join(map(str,b)))

# 16진수
b = []
n = int(input('10진수:'))
alpha = {10:'A', 11:'B', 12:'C',13:'D', 14:'E', 15:'F'}

while n != 0:
    k = n%16
    if k in alpha:
        k = alpha[k]
        b.append(k)
    else:
        b.append(n%16)
    n = n//16

b.reverse()
print(''.join(map(str,b)))