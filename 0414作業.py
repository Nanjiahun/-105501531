#作業1:
import random
number=random.randint(1,100)
guess=-2
start=1
end=100

while True:
    guess= int(input('輸入1~100之間的數字來猜數:'))
    if guess == number:
        print('你猜對了 數字是',number)
        break
    elif guess < number:
        start=guess
        print('請猜',start,'~',end,'之間')
    else:
        end=guess
        print('請猜',start,'~',end,'之間')

#作業5:
for i in range(1,9,2): #[1,3,5,7]
    for j in range(3): 
        if i==7 or i==3 or i==5:
            break
        print(' ',end='')
    for j in range(2):
        if i==7 or i==5 or i==1:
            break
        print(' ',end='')
    for j in range(1):
        if i==7 or i==1 or i==3:
            break
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()
for t in range(5,0,-2):
    for k in range(3): 
        if t==3 or t==5:
            break
        print(' ',end='')
    for k in range(2):
        if  t==5 or t==1:
            break
        print(' ',end='')
    for k in range(1):
        if t==1 or t==3:
            break
        print(' ',end='')
    for k in range(t):
        print('*',end='')
    print()

#作業3:
for i in range(1,5): #[1,2,3,4]
    for j in range(1,5):
        if i != j:
            for k in range(1,5):
                if k != i and k != j:
                    print(i,j,k,sep='',end=' ')
    print()
print('共可以組成 24 種數字互不相同的三位數')

#作業2:
def f(n):
    if n<3:
        return 1
    return f(n-1)+f(n-2)
'''
實在想不到for-巢狀迴圈的斐波那契的數列如何表示
所以自己定義斐波那契的數列的函式
'''
B=0
for n in range(3,23):
    A=f(n)/f(n-1)
    B += A
    print(f(n),'/',f(n-1),sep='',end=' ')

print('數列前',n-2,'項的合:',B)

