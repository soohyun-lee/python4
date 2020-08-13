a = ""
print('카드번호를 입력하세요:')
while True:
    a = input('')
    if a[4] == '-':
        b = list(a)
        for i in range(len(b)-14, len(b)-5):
            if b[i] != '-':
                b[i] = '*'
        print('카드번호는 :',''.join(b))
        break
    else:
        print('카드번호 사이에 하이푼을 입력하세요')