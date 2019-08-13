# 问答题
## 正则
1. 正则re.complie作用

    将正则表达式编译成一个对象，加快速度，加以复用

## 文件操作
1. 用python删除文件和用linux命令删除文件方法

    python: `os.remove`
    
    linux: `rm`
    
## 基础语法

1. range和xrange的区别？

    在Python2中range返回的是一个序列，而xrange是一个生成器，性能上xrange更好
    不过在python3中range已经取代了xrange，如果要选兼容代码，直接用range，不过要注意
    python3中range虽然是惰性的，但它并不是生成器，只是一个可迭代对象。
    
2. __repr__和__str__的区别

    repr是给python看的，更正式，包含详细信息，str是给人看的更直观，由str(), print()方法调用
    str缺省时，print会显示repr的值。

## 异常

1. IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常？

    IOError: 输入输出异常
    
    AttributeError: 试图访问一个类没有的属性
    
    ImportError: 无法导入模块和包
    
    IndentationError: 语法错误，没有正确对齐
    
    IndexError: 索引越界
    
    KeyError: 试图访问字典里不存在的键
    
    SyntaxError: 代码逻辑出错
    
    NameError: 使用一个还未赋予对象的变量
    
## 面向对象
1. 新式类和经典类有哪些区别

    - 新式类不用显示继承Object
    - 多继承新式类采用广度优先，根据MRO(方法解析顺序)，经典类采用深度优先。
        
        钻石继承问题

2. __new__和__init__的区别
    
    __new__是静态方法，用来返回一个创建的实例，接收一个cls参数来识别类
    
    __init__用来初始化实例的参数，它有一个self对象，就是__new__返回的实例
    
3. __new__的用处

    继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。    

    
## 设计
1. 什么是面向切面编程AOP？如何实现
    
    面向切面编程是指在运行、编译、类和方法加载时动态的将代码插入到类的指定方法指定位置处。
    这种思想就是面向切面编程。
    
    很容易联想到Python里可以用装饰器实现这种模式。

2. 什么是鸭子类型？
    
    是一种设计风格，一个对象的特征不需要由父类定义，而是通过方法实现的，比如迭代器，在像java这种语言中
    实现一个迭代器都要继承Iterator这个类，但Python有鸭子类型，所以只要你实现了__iter__，__next__这些方法
    都可以称之为迭代器。
    
    鸭子类型很灵活，但是缺点是依赖文档，清晰的代码和测试来保证正确使用，为了弥补这方面不足，Python3.6
    引入了类型注解，不过类型注解只起两个作用：
    1. 提高代码可读性
    2. 帮IDE识别类型，方便代码补全等功能的使用

3. 单例模式是什么？手写一个试试

    是一种设计模式，确保一个类只能有一个实例存在。常用的使用场景有，我们有一个类AppConfig
    用它来配置项目，在不同模块要创建很多AppConfig实例，这其实很浪费内存，只要一个实例就够了。
    
    实现方法有很多：
    
    1. 使用模块
        python的模块就是天然的单例模式，第一次生成时产生.pyc文件，第二次直接加载.pyc，不会
        再调用代码，因此我们只需要把类和实例放到一个模块供调用即可。
        ```python
        class Single:
           def foo(self):
               pass
        
        single_obj = Single()
        ```
        使用时在另一个模块导入
        ```python
        from singlemodule import single_obj
        single_obj.foo()
        ```
    2. 使用__new__创建
        将类和实例绑定
        ```python
        class Single(object):
           _instance = None
           
           def __new__(cls, *args, **kwargs):
               if not cls._instance:
                   cls._instance = super().__new__(cls, *args, **kwargs)
               return cls._instance
        
        sin1 = Single()
        sin2 = Single()
        
        print(id(sin1) == id(sin2))
        ```
    3. 使用装饰器
    
        函数装饰器：
        ```python
        from functools import wraps
    
        def single(cls):
           instance = {}
           @wraps(cls)
           def get_instance(*args, **kwargs):
               if cls not in instance:
                   instance[cls] = cls(*args, **kwargs)
               return instance[cls]
           return get_instance
    
        @single
        class Single:
           def foo(self):
               pass
        ```
    
        类装饰器：
        ```python
        class cls_single:
           def __init__(self, cls):
               self._cls = cls
               self._instance = {}
        
           def __call__(self, *args, **kwargs):
               if self._cls not in self._instance:
                   self._instance[self._cls] = self._cls(*args, **kwargs)
               return self._instance[self._cls]
         
        @cls_single
        class Single:
           def foo(self):
               pass
        ```
    4. 使用元类
    
        ```python
        class single(type):
           _instance = {}
           def __call__(cls, *args, **kwargs):
               if cls not in cls._instance:
                   cls._instance[cls] = cls(*args, **kwargs)
               return cls._instance[cls]
        
        class Single(metaclass=single):
           pass
        ```
4. Python里的垃圾回收机制

    python的垃圾回收机制主要采用引用计数跟踪和回收垃圾，在引用计数的基础上通过标记清除来解决循环引用问题，再通过分代复用以空间换时间提高垃圾回收效率。
    
    - 引用计数：当一个对象被引用时它的引用数+1，当引用删除时-1，引用计数为0时该对象结束生命
    
    - 循环引用：
    
        ```python
        a = A() # a 计数 1
        b = B() # b 计数 1
        b.a = a # a 计数 2
        a.b = b # b 计数为2 产生了循环引用
        del a  # 计数 1
        del b  # 计数 1
        # a, b 的计数不为0，单纯使用引用计数不能被回收
  
        ```
        
    - 标记清除：先按需分配，等到没有空闲时间时，遍历以对象为节点，引用为边的图，把所有可能访问到的对象打上，然后清扫内存空间，把没标记的对象释放
    
    - 分代技术：其思想是按内存的不同存活时间分为不同集合，没个集合称为一代，垃圾回收的频率随着代的增大而减小，存活时间通常由几次来及回收度量。

## 协程、进程和线程

1. 协程是什么？
    
    协程是一种类似轻量级的线程，省去了进程线程切换的开销，因为协程的切换是程序自身控制，在一个线程内切换
    在单线程内完成多个任务。

2. 什么是GIL锁？

    GIL是全局解释器锁，保证同一时刻只有一个线程能在解释器中运行，当遇到多线程任务时频繁的在各个线程间切换
    以保证并发执行。
    
    解决办法，CPU密集型用多进程代替多线程，或是采用协程。
    
    