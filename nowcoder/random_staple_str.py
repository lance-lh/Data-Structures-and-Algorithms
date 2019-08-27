'''
生成一个长度为8的随机字符串
'''
import random
import string

# 从a-z A-Z 0-9生成指定数量的随机字符：
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
