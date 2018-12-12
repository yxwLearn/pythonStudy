"""
属性案例
创建Student类，描述学生类
学生具有Student.name属性
但是name格式不统一
"""
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

        self.setname(name)
    def des(self):
        print("Hi!My name is {0}".format(self.name))

    def setname(self,name):
        self.name = name.upper()

s1 = Student("wang dajiao",20)
s2 = Student("liu xiaohua",17)
s1.des()
s2.des()

#######             property案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写保存
# 年龄，我们希望统一都用整数保存
# property（fget，fset，fdel，doc）
class Person():
    # 函数名称随意
    def fget(self):
        return self._name * 2

    def fset(self,name):
        # 所有输入姓名全部大写保存
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget,fset,fdel,"对name进行操作")
p = Person()
p.name = "Abc"
print(p.name)


class user():
    """
    1.在用户输入年龄时，可以输入整数，小数，浮点数
    2.但内部为了数据清洁，我们统一保存整数，直接舍去小数点
    """
    def fget(self):
        return self._age

    def fset(self,age):
        self._age = int(age)

    def fdel(self):
        self._name = 0

    age = property(fget,fset,fdel,"")

u = user()
u.age = 12.8
print(u.age)

##  类的内置属性举例
print(user.__dict__)
print(user.__doc__)
print(user.__name__)
print(user.__bases__)


####             __call__举例
class A():
    def __init__(self,name = 0):
        print("我被调用了")
    def __call__(self):
        print("我又被调用了")

a = A()
a()


####             __str__举例
class A():
    def __init__(self,name = 0):
        print("我被调用了")
    def __call__(self):
        print("我又被调用了")

    def __str__(self):
        return "啦啦啦啦"

a = A()
print(a)


####          __getattr__
class A():
    name = "NoName"

    def __getattr__(self,item):
        print("没找到啊")
        print(item)

a = A()
print(a.name)
print(a.age)

#########          __setattr__案例
class Person():
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        print("设置属性{0}".format(key))
        #下面语句会导致死循环
        #self.key = value
        #此种情况，为了避免死循环，规定统一使用调用父类魔法函数
        super().__setattr__(key,value)

p = Person()
print(p.__dict__)
p.age = 18
print(p.age)


#######    __gt__
class Student():
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return self._name

    def __gt__(self, obj):
        print("{0}比{1}大吗？".format(self,obj))
        return self._name > obj._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1>stu2)


########### 类和对象的三种方法案例
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print("我是实例方法")

    #   类方法
    # 类方法的第一个参数一般命名为cls，区别于self，可以任意取
    @classmethod
    def play(cls):
        print(cls)
        print("我是类方法")

    # 静态方法没有参数，可以自己加参数
    @staticmethod
    def swim(item):
        print("我是静态方法{0}".format(item))

p = Person()
p.eat()
Person.play()
p.play()
#静态方法
Person.swim(1)
p.swim(1)