# 基础While循环演示
END_NUMBER = 10
x = 0
while x <10:
    print(x)
    x+=1
    if x == 3:
        break
else:
    print('End While')

# 基础for循环演示：在Python中for循环主要用于遍历序列
FRUIT = ['apple','banana','watermelon']
for it in FRUIT:
    print(it)
else:
    pass #Python中的占位语句，由于Python是通过缩进来区分语句的，要求语句必须是完整的，因此占位语句就出现了：保证语句的完整性。

# 模仿Java中的for循环
for it in range(0,10,1):
    print(it)

for it in range(10,0,-1):
    print(it)

# Python中的循环相比与其他语言多了一个else分支，当该层循环没有调用break结束循环时会调用else分支