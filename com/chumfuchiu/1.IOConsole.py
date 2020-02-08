# 这是一段用于演示从控制台中读取用户名密码并作出相应响应的演示Python代码

userName = 'ChumFuchiu'
passWord = 'wonderfulLife'

print('请输入用户名')
curName = input()

print('请输入密码')
curPass = input()

if curName == userName and passWord == curPass :
    print('登录成功')
else :
    print('登录失败')