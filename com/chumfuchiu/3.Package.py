# 1.使用import关键字可以向当前文件导入一个python文件，访问被导入文件的内容时需要加上前缀
# 前缀：import 关键字之后的标志符

import pack.PublicConstants
print(pack.PublicConstants.Bilibili)
for it in pack.PublicConstants.links:
    if it == pack.PublicConstants.Bilibili:
        print(it)

# 2.另一种导入Python文件的方式
from pack import PublicConstants
print(PublicConstants.Bilibili)

# 3.导入某个Python文件的特定成员；在当前Python文件就可以不需要前缀直接访问该成员,但是无法访问别的成员
from pack.PublicConstants import Bilibili
print(Bilibili)

# 4.导入某个Python文件的所有成员；在当前Python文件就可以不需要前缀直接访问该成员
print('****************************')
from pack.PublicConstants import *
for it in links:
    print(it)

# 当一个python文件被其他文件import时，会执行被import文件的内容分。    
