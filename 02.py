class Person():
    name = "NoName"
    age = 18
    _petname = "xiaoming"
    __score = 20

    def work(self):
        print("Work For Money")

class Teacher(Person):
    name = "xixi"
    age = 20
    def make_test(self):
        print("attention")
    def work(self):
        #Person.work(self)
        super().work()
        self.make_test()

t = Teacher()
print(t.work()) # 此处打印了一个none？？？
print(t.name)
print(t.age)
print(t._petname)


##### 构造函数
##### 实例化时自动调用
class Dog():
    def __init__(self):
        print("init a dog")

## 实例化时，括号内的参数需要与构造参数匹配
d = Dog()


#####继承中的构造函数
class Animal():
    def __init__(self):
        print("init a Animal")
class PxAnimal(Animal):
    def __init__(self,name):
        print("init a PxAnimal")


class Dog(PxAnimal):
    def __init__(self):
        print("init a dog")
##实例化时，自动调用了Dog的构造函数
## 因为找到了自身的构造函数，则不再查找父类构造函数
maoqiu = Dog()

class Cat(PxAnimal):
    pass
## 猫没有构造函数，自动调用父类的构造函数
## 但是当父类构造函数中有多个参数时，需要补齐对应的参数，否则报错
##总而言之，如果自己没有构造函数，就一直往上找
cat =Cat("aa")