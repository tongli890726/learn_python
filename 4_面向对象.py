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


'''
装饰器 @property
'''
class Student2(object):
	"""docstring for Student2"""
	
	# 加上@property就是将这个getter方法，可以利用属性去调用
	@property
	def name(self):
		print('get方法')
		return self._name
	# 这个是setter方法，有了这个装饰器，也可以利用属性调用
	@name.setter
	def name(self, value):
		print('setter方法')
		self._name = value


	# 如果只有@property，没有对应的@xxx.setter，那么这个属性就是一个只读的
	@property
	def age(self):
		return self._age
		


tempStu = Student2()
# 其实调用了name的setter方法，给属性_name绑定了数据
tempStu.name = 'tongli'
# 其实调用了name的getter方法
print(tempStu.name)

# 动态给_age属性绑定数据，
tempStu._age = '222'
# 调用了age的getter方法
print(tempStu.age)


'''
__slots__
'''

class Person(object):
	"""docstring for Person"""
	# 限定只能绑定这些属性，其他属性不允许
	__slots__ = ('_name', '_age', '_gender')

	def __init__(self, name, age):
		super(Person, self).__init__()
		self._name = name
		self._age = age

	@property
	def gender(self):
		return self._gender
	@gender.setter
	def gender(self, gender):
		self._gender = gender


		
person = Person('lisa', 28)
person.gender = '男'
print(person.gender)
# 由于限定了属性，所以isgay不能绑定
# person.isgay = True



'''
静态方法 类方法，以后再学

'''
class Triangle(object):
	"""docstring for Triangle"""
	def __init__(self, a, b, c):
		super(Triangle, self).__init__()
		self._a = a
		self._b = b
		self._c = c

	# 静态方法关键字
	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and b + c > a and a + c > b

	# 类方法，第一参数必须是cls,表示当前类相关的信息的对象 
	@classmethod
	def is_valid2(cls,a, b, c):
		return a + b > c and b + c > a and a + c > b


	# 周长
	def perimter(self):
		return self._a + self._b + self._c
	

a, b, c = 3, 4, 5
# 静态方法和类方法都是通过类直接调动
if Triangle.is_valid(a, b, c):
	t = Triangle(a, b, c)
	print('周长:',t.perimter())
else:
	print('无法构成三角形')




'''
继承.多态
'''
# 父类
class PensonClass(object):
	"""docstring for PensonClass"""
	def __init__(self, name, age):
		super(PensonClass, self).__init__()
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name
	@property
	def age(self):
		return self._age
		
	@age.setter
	def age(self, age):
		self._age = age

	def play(self):
		print('%s正在愉快的玩耍.'% self._name)

	def watch_movie(self):
		if self._age <= 18:
			print('%s在看熊出没'%self._name)
		else:
			print('%s想看什么看什么'%self._name)

# 子类
class Student3(PensonClass):
	"""docstring for Student3"""
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self._grade = grade

	@property
	def grade(self):
		return self._grade
	@grade.setter
	def grade(self, grade):
		self._grade = grade


	def study(self, course):
		print('%s的%s正在学习%s..'%(self._grade, self._name, course))


	def play(self):
		print('%s正在愉快的玩耍.（子类）'% self._name)




stu = Student3('王大锤', 15, '初三')
stu.study('数学')
# 调用了父类的方法
stu.watch_movie()

# 重写了子类的方法，就调用了子类的方法
stu.play()









