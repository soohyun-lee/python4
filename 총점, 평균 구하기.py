age = {'A':30, 'B':42, 'C':27, 'D':60}
A = {'국어': 83, '영어': 100, '수학': 37}
B = {'국어': 52, '영어': 56, '수학': 47}
C = {'국어': 40, '영어': 97, '수학': 89}
D = {'국어': 90, '영어': 79, '수학': 97}

#1. C의 총점과 평균


C_ = list(C.values())
print(sum(eval('C_')))
print(sum(eval('C_'))/4)


# 2. 나이의 합
print(sum(age.values()))

# 3.모든 점수 중 가장 낮은 점수
def num(x):
    ret = list(x.values())
    return ret

all_list = num(A) + num(B) + num(C) + num(D)
print(min(all_list))