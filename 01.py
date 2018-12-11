'''
定义一个学生类，用来描述学生
'''
# 定义一个空的类
class Students():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass
# 定义一个对象
mingyue = Students()


# 定义一个非空的类
class PythonStudents():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    # 需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认出一个self参数
    def doHomework(self):
        print("python学生在做作业" )
        # 在函数末尾推荐使用return语句
        return None
# 实例化一个叫xiaoming的学生
xiaoming =PythonStudents()
print(xiaoming.age)
print(xiaoming.name)
xiaoming.name = "xiaoming"
print(xiaoming.name)
xiaoming.doHomework()
# 对象的所有成员
print(xiaoming.__dict__)
# 类的所有成员
print(PythonStudents.__dict__)

# self非绑定类方法和绑定类方法
class Teacher():
    name = "nana"
    age = 18
    def say(self):
        print(self.name)
        print(self.age)
        # 获取类的属性
        print(__class__.name)

t =Teacher()
t.name = "lalal"
t.say()

class B():
    name = 'aaa'
    age = 20

t =Teacher()
# 此处默认将t 替换self
t.say()
# 此处t代替self
Teacher.say(t)
# 此处因B类中也有name和age属性，说以可以使用，称为鸭子模型
b =B()
Teacher.say(b)


class Person():
    # name是共有成员
    name = "xiaoli"
    # __age就是私有成员
    __age = 18


p = Person()
# 正常访问，有输出
print(p.name)
# 出错，没输出
# print(p.__age)
# 正常访问有输出
print(p._Person__age)

