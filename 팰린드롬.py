def palindrome(n):
    for i in range(0,len(n)//2):
        if n[i] == n[-i-1]:
            return True
        if n[i] != n[-i-1]:
            return False


n = input('단어를 입력하세요:')
print(palindrome(n))

# 수정
def palindrome(n):
    for i in range(0,len(n)//2):
        if n[i] != n[-i-1]:
            return False
    return True


n = input('단어를 입력하세요:')
print(palindrome(n))