'''
函数
参数带有*的是可变参数
'''
def add(num1, num2, *count):
	return num1 + num2

print(add(1, 2))

# nums是可变参数，参数个数不定
def add2(*nums):
	total = 0
	for num in nums:
		total = total + num
	return total

print(add2(1, 2, 3))
print(add2(1, 2))


'''
python中，一个.py文件就是一个模块
'''

