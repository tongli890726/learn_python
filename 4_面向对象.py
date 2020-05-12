# 创建类
class Student(object):

	# __init__ 创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
	def __init__(self, name, age, score): # 第一个参数self是默认的，不用管
		self.name = name
		self.age = age
		# 双下划线 代表 私有属性。不可访问
		self.__score = score

	# 定义方法
	def study(self, course_name): # 同样self是默认的，不用管
		print('%s正在学习%s'%(self.name, course_name))

	def watch_movie(self):
		if self.age < 18:
			print('%s只能观看《熊出没》.' % self.name)
		else:
			print('%s想看什么看什么.'% self.name)
	# 私有方法，不可调用
	def __look_score(self):
		print(self.__score)


# 创建实例，并指定属性
stu = Student('lisa', 30, 100)
stu.study('python程序设计')
print(stu.age)
# 修改属性
stu.age = 31
print(stu.age)

stu2 = Student('王大锤',16, 99)
stu2.watch_movie()


