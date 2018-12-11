"""
多继承实例
子类可以直接拥有父类得到属性和方法，私有属性和方法除外
"""
class Fish():
    def __init__(self,name):
        self.name = name

    def swim(self):
        print("I am Swimming....")

class Bird():
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("I am flying....")

class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("I am working....")

class SuperMan(Person,Bird,Fish):
    def __init__(self, name):
        self.name = name

s =SuperMan("xxxx")
s.fly()
s.swim()

#### 菱形继承问题

class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass


#####构造函数例子

class Person():
    # 对person类进行实例化时
    # 姓名需要确定
    # 年龄需要确定
    # 地址需要确定
    def __init__(self):
        self.name = "xxx"
        self.age = 18
        self.addr = "XXXXXXX"

p = Person()
print(p.name)



#####构造函数调用顺序
#####如果子类没有构造函数，自动向上找，直到找到位置

class A():
    pass
class B(A):
    def __init__(self):
        print("B")

class C(B):
    pass

# 此时先找C的构造函数
#如果没有，则按照MRO顺序查找父类的构造函数，直到找到为止
c = C()

# C类如果想扩展B类中的构造函数
# 即调用B的构造函数后再添加一些功能
# 有两种方法实现

# 第一种通过父类名是调用
def __init__(self,name):
    # 首先调用父类构造函数
    B.__init__(self,name)
    # 再实现自己的功能
    print("这是C的附加功能")

# 第二种，通过super调用
def __init__(self,name):
    # 首先调用父类构造函数
    super(C,self).__init__(name)
    # 再实现自己的功能
    print("这是C的附加功能")


####Mixin设计模式

class Person():
    name = "xxx"
    age = 28

    def eat(self):
        print("eat.....")

    def sleep(self):
        print("sleeping.....")

    def drink(self):
        print("drink.....")

class Teacher(Person):
    def work(self):
        print("work.....")

class Student(Person):
    def study(self):
        print("study.....")

class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

####上面代码Mixin的写法
print("=" * 20)
class TeacherMixin():
    def work(self):
        print("work.....")

class StudentMixin():
    def study(self):
        print("study.....")

class Tutor(TeacherMixin,StudentMixin):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

############     issubclass 检测一个类是否是另一个类的子类
class A():
    pass

class B(A):
    pass

class C():
    pass

print(issubclass(B,A))
print(issubclass(C,A))

############     isinstance  检测一个对象是否是另一个类的实例
class A():
    pass

a = A()
print(isinstance(a,A))
print(isinstance(A,A))

############     hasattr  检测一个对象是否有成员XXX
class A():
    name = "NoName"

a = A()
print(hasattr(a,"name"))
print(hasattr(a,"age"))

############     dir 获取成员对象列表
class A():
    pass

print(dir(A))