#作業2:反轉串列
data=[100,80,90,70,59,30,21,35]
ss=[]
for i in range(8):
    s = data.pop()
    ss.append(s)
print(ss)
#作業1:串列由小到大/由大到小
#大~小
data=[100,80,90,70,59,30,21,35]
ss=[]
for i in range(8):
    if i == 0:
        s = data.pop(-8)
        ss.append(s)
    elif i == 1 or i == 2:
        s = data.pop(-6)
        ss.append(s)
    elif i == 3:
        s = data.pop(-5)
        ss.append(s)
    elif i == 4:
        s = data.pop(-4)
        ss.append(s)
    elif i == 5 or i == 7:
        s = data.pop(-1)
        ss.append(s)
    else:
        s = data.pop(-2)
        ss.append(s)
print(ss)
#小~大
data=[100,80,90,70,59,30,21,35]
ss=[]
for i in range(8):
    if i == 0 or i == 1 or i == 5:
        s = data.pop(-2)
        ss.append(s)
    else:
        s = data.pop(-1)
        ss.append(s)
print(ss)
#作業3:
list1=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]
A=''
for i in list1:
    for j in i:
        A += str(j)+' '
    print('{:^14}'.format(A),end='')
    A =''
    print()
