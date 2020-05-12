# 字符串
s1 = 'hello word'
print(s1)

# 字符串运算符
s1 = 'hello' * 3 # 重复
print(s1)
s2 = 'world'
print(s1+ s2) # 用+进行字符串拼接

print('hello' in s1) # in 判断字符串是否在其中

print(s1[3]) # 可通过下表进行访问和切片
print(s1[:2]) # 切片是 起始位置：终止位置：步长
print(s1[::2]) # 步长为2

# 字符串处理
str1 = 'hello, world!'
print(len(str1)) # 字符串长度
print(str1.capitalize()) # 首字母大写
print(str1.title())  # 每个单词的首字母大写
print(str1.upper())  # 全部字符大写

print(str1.find('or')) # find 从字符串中查找子串所在位置.找不到的返回 -1
print(str1.index('or')) # index 与 find类似，但是找不到子串会引发异常

print(str1.startswith('he')) # startswith 以什么开头
print(str1.endswith('d!')) # endswith 以什么结尾

print(str1.center(20, '*')) # 以str1为中心，前后填充*，直到长度是20
print(str1.ljust(20, '*'))  # 在str1居左，右边填充*，直到长度是20
print(str1.rjust(20, '*'))  # 在str1居右，左边填充*，直到长度是20

str2 = 'abc123456'
print(str2.isdigit())  # isdigit判断是否全部由数字组成
print(str2.isalpha())  # isalpha判断是否全部由字母组成
print(str2.isalnum())  # isalnum判断是否只由数字和字母组成

str3 = '  jackfrued@126.com '
print(str3.strip()) # 修剪左右两侧空格

# 格式化输出
a, b = 5, 10
print('%d * %d = %d' % (a, b, a*b))
print('{0} * {1} = {2}'.format(a, b, a*b)) # {0}{1}{2}..代表后面的参数编号
print(f'{a} * {b} = {a*b}') # 语法糖的形式，即前面加个f即可。括号内就是参数


'''
列表list

'''
list1 = [1, 3, 5, 7, 100]
print(list1)
print(list1 *3) # 列表元素重复
print(len(list1)) # 列表长度

print(list1[3]) # 列表通过下标进行访问和切片
print(list1[:2]) # 切片是 起始位置：终止位置：步长
print(list1[::2]) # 步长为2

# enumerate处理后，遍历可以同时获得元素索引和值
for index, i in enumerate(list1):
	print(index ,i)

list1.append(200) # 末尾添加
print(list1)
list1.insert(1, 300) # 插入，在位置1中插入元素300
print(list1)

list1.remove(3) # 删除元素
list1.pop(1) # 删除对应位置的元素，删除位置1的元素


list1 += [1000, 2000] # 利用+号对两个list进行合并，
print(list1)


print(1000 in list1) # 是否在list中
print(list1)

list1.clear() # 清空所有元素
print(list1)

# list排序
list2 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# sorted排序，不影响原list
list3 = sorted(list2) # 排序
list4 = sorted(list2, reverse=True) # 倒叙排列
list5 = sorted(list2, key=len) # 通过关键字排序，这里是通过长度排序 
print(list3)
print(list4)
print(list5)

list2.sort() #sort是在原list上进行排序，注意和sorted区别
print(list2)

# 生成式和生成器
# 列表生成式，即通过循环后，然后进行计算生成列表
f = [x*x for x in range(10)]  #循环的每个元素，在自乘，组成列表
print(f)
f1 = [a+b for a in 'abc' for b in '12345'] # 每一个a和每一个b,进行加法运算，组成列表
print(f1)



