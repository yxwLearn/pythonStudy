#### Python的oop思想（面向对象）
- python的面向对象
- 面向对想编程
   - 基础
   - 公有私有
   - 继承
   - 组合，Mixin
- 魔法函数
   - 魔法函数概述
   - 构造类魔法函数
   - 运算类魔法函数
##### 1.面向对像概述
- OOP思想
   - 接触到任意一个任务，首先想到的是这个任务有哪些模型构成，这些模型就是对象
- 几个名词
   - OO：面向对象
   - OOA：面向对象的分析
   - OOD：面向对象的设计
   - OOI：面向对象的实现
   - OOP：面向对象的编程
   - OOA->OOD->OOI:面向对象的实现过程
- 类和对象的概念
   - 类：抽象名词，代表某一类拥有共性的事物
   - 对象：类的具体化，类中的某一个个体，称之为对象
   - 类和对象的关系：
       - 一个具象，代表一个类的摸一个个体
       - 一个抽象，代表的是一大类事物
 - 类中的内容，具体有两个内容
   - 表明事物的特征，叫做属性（变量）
   - 表明事物的功能或动作，称为成员方法（函数）
##### 2.类的基本实现
- 类的命名
   - 遵守变量命名规范
   - 大驼峰（每个单词首字母大写）
   - 避开关键字等
- 如何声明一个类
   - 必须使用class关键字
   - 类由属性和方法构成，其他不允许出现
   - 成员属性可以直接使用变量赋值，如果没有值，允许使用None
   - 案例 01.py(位于PythonStudy项目下)
- 实例化类

          对象名 = 类名() #实例化了一个对象
- 访问对象成员
   - 使用点操作符
   
           obj.成员属性名称
           obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
   - 对象所有成员检查(检查的是当前对象独有的成员，而不包括类中的成员属性)
   
           # dict前后各有两个下划线
           obj.__dict__
   - 类的所有成员
   
           # dict前后各有两个下划线
           class_name.__dict__
           
##### 3.类和对象的成员属性分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的相同成员，如果对象中有该成员，则一定访问对象中的该成员(注意：类实例的属性和其对象的属性在不对对象属性重新赋值的情况下指向同一地址，可用id方法进行类实例和对象实例测试)
- 创建对象的时候，类中的成员不会放入对象中，而是得到一个空对象，没有成员(通过__dict__去验证)
- 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员

##### 4.关于self
- self在对象方法中代表对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中(self不是关键字，可随意替换，只是为了语义好理解而已)
- 方法中有self形参的方法称为非绑定类的方法，可通过对象访问，没有self的是绑定类的方法，只能通过类访问
##### 5.面对对象的三大特性
- 封装
  - 封装就是对对象的成员进行访问限制
  - 封装的三个级别：公开,public;受保护的，protected;私有的，private
  - public,private,protected不是关键字
  - 判断对象的位置：对象内部，对象外部，子类中
  - 私有：私有成员是最高级别的风转化，只能在当前类或对象中访问，在成员前面添加两个下划线即可
  
	        例子：
	        class Person():
	        	# name是共有成员
	              name = "xiaoli"
	            # __age就是私有成员
	              __age = 18
	        p = Person()
	        # 正常访问，有输出
	        print(p.name)
	        # 出错，没输出
	        print(p.__age)
	        # 正常访问有输出
	        print(p._Person__age)
   - Python的私有不是真的私有，是一种称为name mangling的改名策略，可以使用对象._classname__attributename访问。
   
   - 受保护的封装：protected，就是将对象进行一定级别的封装，然后，在类或者子类中都可以进行访问，但是在外部不可以;封装得方法是：在成员名称前添加一个下划线即可。
   - 公开的：public，公共的封装实际对成员没有任何操作，任何地方都可以访问。
   
- 继承
   - 继承就是一个类可以获得另一个类的成员属性和成员方法
   - 作用：减少冗余的代码，增加代码的复用性，同时可以设置类与类之间的关系。
   - 继承与被继承：被继承的类称为父类，也称为父类或者超类，用于继承的类称为子类或者派生类,两者一定存在一个is-a关系。
   - 任何一个类都有一个共同的父类Object
   - 语法:
   
	         class Person():
	         	name = "NoName"
	            age = 0
	            def sleep():
	           		print("Sleeping.......")
	         # 父类写在括号里面
	         class Teacher(Personal):
	         	pass;
	         # 输出NoName
	         t =Teacher()
	         print(t.name)
	         print(Teacher.name)
   - 继承的特征:所有的类都继承自object类，即所有的类都是object的子类;子类一旦继承父类,则可以使用父类中除私有成员的所有内容;子类继承父类之后并没有将父类成员完全赋值到子类中,而是通过引用关系访问调用;子类可以定义独有的成员属性和方法;子类中定义的成员和父类如果相同，优先使用子类成员;子类如果想扩充父类的方法,可以在定义新方法的同时访问父类成员来进行代码重用,可以使用   【父类名.父类成员】 的格式来调用父类成员,也可以使用【super().父类成员】的格式来调用。
   - 继承变量函数的查找顺序问题：优先查找自己的变量，没有则查找父类，构造函数如果本类中没有定义，则自动查找调用父类构造函数，如果本类中有，则不继续向上查找
   -构造函数：是一类特殊的函数，再类进行实例化之前进行调用;如果定义了自己的构造函数，则实例化时使用自己的构造函数，不查找父类的构造函数;如果没有定义，则自动查找父类的构造函数;如果子类没有定义，父类的构造函数带参数，则构造对象时的参数也需要带上对应的参数。
   - super：不是关键字，而是一个类;作用是获取MRO(MethondResolutionOrder)列表中的第一个类;super与父类没有任何实质性关系，但通过super可以调用到父类;super使用两个方法，参见 【继承的特征】。
   - 单继承：每个类只能继承一个类，传承有序逻辑清晰语法简单隐患少，缺点是功能不能无线扩展，只能在当前唯一的继承链中扩展。
   - 多继承：每个类允许继承多个类，优点是类的功能扩展方便，缺点是继承关系混乱。(不推荐使用！！)
   
   - 菱形继承和钻石继承问题：多个子类继承同一个父类，这些子类又被同一个子类继承，于是继承关系图形成一个菱形图谱,MRO就是多继承中用于保存继承顺序的一个列表，python中本身采用C3算法来对多继承的菱形继承进行计算的结果，MRO列表的计算原则：子类永远在父类前面，如果多个父类则按照继承语法中括号内类的书写顺序存放，如果多个类继承了同一个父类，孙子类中只会选择继承语法括号中第一个父类的父类。
 	
- 多态：就是同一对象再不同情况下有不同的状态出现，同一事物的多种形态。多态不是语法，是一种设计思想；多态性：一种调用方式，不同的执行结果。[多态和多态性](https://www.cnblogs.com/luchuangao/p/6739557.html)

- Mixin设计模式
	- 主要采用多继承方式对类的功能进行扩展
    - [Mixin概念](https://www.cnblogs.com/aademeng/articles/7262520.html)
    - [MRO 和 Mixin](https://blog.csdn.net/robinjwong/article/details/48375833)
    - 使用多继承语法实现Mixin需要非常小心：首先他必须是表示某一单一功能，而不是某个物品；职责必须单一，如果需要多个功能，则写多个Mixin；Mixin不能依赖于子类的实现；子类即使没有继承这个Mixin这个类，也能照样工作，只是少了某个功能而已。
    - 优点：可以在不对类进行任何修改的情况下，扩充功能；可以方便的组织和维护不同功能组件的划分；可以根据需要任意调整功能类的组合；可以避免创建很多新的类，导致类的继承混乱。
    
##### 6.相关函数
- issubclass：检测一个类是否是另一个类的子类
- isinstance：检测一个对象是否是另一个类的实例
- hasatrr：检测一个对象是否有成员XXX
- getattr：get attribute
- setattr：set attribute
- delattr：delete attribute
- dir： 获取对象的成员列表

##### 7.类的成员描述符（属性）
- 类的成员描述是为了在类中对类的成员属性进行相关操作而创建的一种方式
    - get：获取属性的操作
    - set：修改或添加属性操作
    - delete：删除属性的操作
- 如果想是使用类的成员描述符，大概有三种方法
	- 使用类实现描述器
	- 使用属性修饰符
	- 使用property函数
		- property函数很简单
		- property（fget，fset，fdel，doc）
	- 案例参考[04.py]()
- 无论哪种修饰符都是为了对成员属性进行相应的控制
	- 类的方式：适合多个类中的多个共用一个描述符
	- property方式：适用当前类中使用，可以控制一个类中多个属性
	- 属性修饰符：适用于当前类中使用，可以控制一个类中单个属性
	
##### 8.类的内置属性

			__dict__:以字典形式显示成员组成

			__doc__:获取类的文档信息

			__name__:获取类的名称，如果在模块中使用，获取模块的名称

			__bases__:获取某个类的所有父类，以元祖的方式显示

##### 9.类的常用魔术方法

-   魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
-   魔术方法的统一的特征，方法名被前后两个下划线包裹
-   操作类
	-   __init__:构造函数
	-   __new__:对象实例化方法，此函数比较特殊，一般不需要使用
	-   __call__:对象当函数使用的时候触发
	-	__str__:当对象被当做字符串使用的时候调用
	-   __repr__:返回字符串，和__str__具体区别百度即可
-   描述符相关
	-	"__set__"
	-	"__get__"
	-	"__delete__"
-	属性操作相关
	-	"__getattr__":访问一个不存在的属性触发
	-	"__setattr__":对成员属性进行设置的时候触发
		-	参数：
			-	self用来获取当前对象
			-	被设置属性的名称，以字符串形式出现
			-	需要对属性名称设置的值
		-	作用：进行属性设置的时候进行验证或者修改
		-	注意：在该方法中不能对属性直接进行复制操作，否则进入死循环
-	运算类相关魔术方法
	-	'__gt__':进行大于判断的时候触发的函数
		-	参数:
			-	self
			-	第二个参数是第二个对象
			-	返回值可以是任意值，推荐返回布尔值

##### 10.类和对象的三种方法

- 实例方法

    -  需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成

- 静态方法

	-  不需要实例化，通过类直接访问


- 类方法

  - 不需要实例化