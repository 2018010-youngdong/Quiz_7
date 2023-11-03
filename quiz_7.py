a=int(input('크리스마스 트리의 높이를 입력하세요: '))
def tree(a):
    for i in range(1,a+1):
        gap=' '*(a-i)
        star='*'*(2*i-1)
        print(gap+star)
tree(a)

