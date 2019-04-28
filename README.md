### python 题宗


https://zhuanlan.zhihu.com/p/21856569
https://www.cnblogs.com/chongdongxiaoyu/p/9054847.html

图像处理
https://mp.weixin.qq.com/s?__biz=MzU2MDAyNzk5MA==&mid=2247483801&idx=1&sn=b56f02e8e425c1f60c4fde0bb1913a1f&chksm=fc0f01a0cb7888b6ad87946efed59b372cfa6fd45c771e3a0159e5ab8380da41c99a32c4a214#rd

1. 什么是GIL 谈谈你对GIL的理解？
    
    python代码的执行是由python虚拟机（也叫解释器主循环mCPython版本）来控制，python在设计之初就考虑到在解释器的主循环中，同时只有一个线程在执行，即在任意时刻，只有一个线程在解释器中运行。对python虚拟机的访问由全局解释器锁（GIL）来控制，正是这个锁能保证同一时刻只有一个线程在运行。
   在多线程环境中，python虚拟机按以下方式执行：
      1. 设置GIL
      2. 切换到一个线程去执行
      3. 运行：
        a.执行数量的字节码指令，或者 b. 线程主动让出控制（可以调用time.sleep(0)）
      4. 把线程设置为睡眠状态
      5. 解锁GIL
      6. 再次重复以上所有步骤

   在调用外部代码（如C/C++扩展函数）的时候，GIL将会被锁定，直到这个函数结束为止（由于在这期间没有python字节码被运行，所以不会做线程切换）
   
2. 什么是元类？

    元类创建对象 是类的类， type函数实际上就是一个元类

3. 说说decorator的用法和它的应用场景， 可以的话，写一个decorator
    
    所谓装饰器就是把函数包装一下， 为函数添加一些附加功能， 不改变原函数的代码，装饰器就是一个函数，参数为被包装的函数，返回包装后的函数， 使用时使用@修饰符
    ```python
    def newfoo(func):
        def inner():
            print("before func")
            func()
            print("after func")
        return inner
        
    @newfoo
    def foo():
        print("running")
        
    foo()
    
    #输出结果
    before func
    running
    after func
    
    ```

4. 为什么要用函数装饰器？请举例

   装饰器的作用和功能：
   1. 引入日志
   2. 函数进行时间统计
   3. 执行函数执行前的预处理（改变函数的入参）
   4. 执行函数后的清理功能
   5. 权限校验等场景
   6. 缓存

5. 是否遇到过python模块间循环引用的问题，如何避免它？

   导入模块的实质是要将被导入模块所有的顶格代码都执行一遍，遇到函数和类的定义会作申明
   解1:
   直接导入模块名，通过模块调用其中的函数
   ```python
   #modeleA
   import moduleB
   
   def a():
      print 'aaaa'
      moduleB.b()
   
   def c():
      print 'cccc'
   
   if __name__ == "__main__":
      a()
      
   
   #moduleB
   
   def b():
      print 'bbbb'
      moduleA.c()
   
   ```
   解2:使用延迟导入（lazy import）在需要用的函数内部导入，或是在底部导入
   ```python
   #moduleB
   def b():
      print 'bbbbb'
      c()
   from moduleA import C
   
   #或者
   def b():
       from moduleA import c
       print 'bbbb'
       c()
   ```

   解法3：重新设计代码结构，将代码合并或者分离

6. 有用过with statement吗？ 它的好处是什么？

   1. with语句 其实是上下文管理器， 其内置了__enter__()方法和__exit__()方法，在with语句中，如果用as指定一个目标，会将__enter__()方法的返回值赋予这个目标。
   2. 运行中如果发生了异常，那么将会把异常的类型，值和追踪传递给__exit__()方法。如果__exit__()方法返回值为ture，则这个异常会被抑制，否则这个异常将会被重新抛出。
   3. 如果没有发生异常，也会调用__exit__()方法，但是传入的参数为None，None，通常执行文件流／会话的关闭等操作。
   在开发时， with as语句等效于try do except finally
   ```python
   with open('a.txt', 'a+', encoding='utf-8') as f:
      data = f.read()
   
   #等效于
   try: 
      f = open('a.txt')
   except:
      print 'fail to open'
      exit(-1)
   finaly:
      f.close()
   ```

7. 对比一下dict中的items与iteritems

   dict中 items 方法作用：是将字典中的所有项，以列表的方式返回。因为字典是无序的，所以用items方法返回字典的所有项 也是没有顺序的
   字典中iteritems方法作用：与items方法作用大致相同。不iteritems返回的不是列表 而是迭代器，不占用额外的内存
   ```
   #python3
   dict={'key1':'value1','key2':'value2'}
   >>> for i,j in dict_s.items():
   ...     print(i, j)
   ...
   key1 value1
   key2 value2
   
   ```
   python3 中已经取消了iteritems属性，用items代替, 因为dict 返回的不再是列表啦 而是dict_items类 可以用for 遍历

8. inspect模块有什么用

    1. 对是否是模块、框架、函数进行类型检查
    2. 获取源码
    3. 获取类或者函数的参数信息
    4. 解析堆栈

9. 写一个类，并让它尽可能的支持操作符

    ```python
    class Array(object):
        __list = []
        
        def __init__(self):
            print("constructor")
           
        def __del__(self):
            print("del constructor")
           
        def __str__(self):
            return ("this is self_defined array class")
            
        def __getitem__(self, key):
            return self.__list[key]
           
        def __len__(self):
            return len(self.__list)
            
        def Add(self, value):
            self.__list.append(value)
           
        def Remove(self, index):
            del self.__list[index]
            
        def Displayitems(self):
            print("show all items---")
            for item in self.__list:
                print(item)
           
           
    if __name__ == "__main__":
        arr = Array()
        print(arr)
        print(len(arr))

        arr.Add(1)
        arr.Add(2)
        print(len(arr))
        print(arr[0])

        arr.Displayitems()
    ```

10. python下多线程的限制以及多进程中传递参数的方式
    
    python多线程有个全局解释器锁（GIL global interpreter lock），这个锁的意思是任一时间只能有一个线程使用解释器，和单个cpu跑多个程序，大家都是轮着使用解释器。这叫“并发”不叫“不行”
    多进程间共享数据，传递参数。可以使用 multiprocessing.Value, multiprocessing.Array
    多进程间应该避免使用共享资源。在多线程中，比较容易共享资源，比如使用全局变量或者传递参数。在多进程情况下， 由于每个进程有自己独立的内存空间，以上方法并不合适。此时我们通过共享内存和manager的方法来共享资源。但这样做提高了程序的复杂度， 并因为同步的需要而降低了效率


11.1. python是如何进行内存管理的

    一，垃圾回收：
    python和C++java等语言不同，它可以不用事先声明变量类型而直接对变量进行赋值。对python语言来讲，对象的类型和内存都是在运行时确定的。这也是为什么我们称python语言为动态类型的原因（这里我们把动态类型可以简单的归结为对变量内存地址的分配是在运行时自动判断变量类型并对变量进行赋值）
    二，引用计数
    Python采用了类似windows内核对象一样的方式来进行内存管理。每一个对象，都维护这一个对指向该对对象的引用的计数。当变量被绑定在一个对象上的时候，该变量的引用计数就1，系统会自动维护这些标签，并定时扫描，当某标签的引用计数为0的时候， 该对象就会被回收。

11.2. python多进程中共享内存Value和Array

    *https://www.cnblogs.com/gengyi/p/8661235.html*
    （1）共享内存是一种最为高效多进程间通信方式，进程可以直接读写内存，而不需要任何数据多拷贝。
    （2）为了在多个进程间交换信息，内核专门留出一块内存区，可以由需要访问的进程将其映射到自己的私有地址空间。进程就可以直接读写这一块内存而不需要进行数据的copy，从而大大提高了效率（文件映射）
    （3）由于多个进程共享一块内存， 因此也需要依靠某种同步机制。
    优缺点：
    优点：快速在进程间传递参数
    缺点：数据安全上存在风险，内存中的内容会被其他进程覆盖或更改
 ```python
from multiprocessing import Process, Value
import time
import random

def save_money(money):
    for i in range(10):
        time.sleep(0.1)
        money.value += random.randint(1, 200)

def take_money(money):  
    for i in range(10):
        time.sleep(0.1)
        money.value -= random.randint(1, 200)

# money为共享内存对象,给他一个初始值2000，类型为正型“i”
# 相当于开辟了一个空间，同时绑定值2000
money = Value('i', 2000)

d = Process(target=save_money, args=(money,))#这里面money是全局的，不写也可
d.start()

w = Process(target=take_money, args=(money,))#这里面money是全局的，不写也可
w.start()

d.join()
w.join()

print (money.value)
 ```

12. 什么是lambda函数？它有什么好处？

    lamba函数一个可以接收一个或者多个参数（包括可选参数）并且返回单个表达式值的函数。（lambda函数不能包含命令，它所包含的表达式不能超过一个）
    lambda函数返回的是一个匿名函数

    使用lambda函数有什么好处？
    1. lambda函数比较轻便，即用即扔，很适合需要完成某一项简单功能，但是这个简单的功能只能在此一处使用。
    2. lambda是匿名函数，一般用来给filter，map，reduce这样的函数式编程服务
    3. 作为回调函数，可以传递给某些应用， 比如消息处理等
    ```
    >>> g = lambda x: x*2
    >>> g(5)
    10
    >>> (lambda x: x*x)(5)
    25
    >>> map(lambda x: x*2,[1,2,3,4,5])
    [2, 4, 6, 8, 10]
    >>> map( lambda x: x*x, [y for y in range(10)] )
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

13. python读取大文件？限制内存
（1）. 利用生成器generator

    也就是分块读取思想
    ```

    filepath = '/Users/guogx/Downloads/local-monitor/collector.log'

    def read_in_chunks(filepath, chunk_size=1024*10):
        f = open(filepath)
        while True:
            chunk_data = f.read(chunk_size)
            if not chunk_data:
                break
            yield chunk_data

    if __name__ == '__main__':
        chunks = read_in_chunks(filepath)
        for chunk in chunks:
            print(chunk)
    ```
（2）迭代器进行遍历： for line in file
    
（3）  使用 with语句打开和关闭文件，包括抛出一个内部快异常。 for line in f文件对象f视为一个迭代器，会自动的采用缓存IO和内存管理，所以不必担心大文件
    with open(bigfile.txt) as f:
        for line in f:
            print(line)

14. 如何用python输出一个Fibonacci数列？

    ```
    >>> a,b = 0,1
    >>> while b<100:
    ...     print(b)
    ...     a,b = b, a+b
    ...
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    ```

15. 介绍一个python中webbrowser的用法

16. 解释一下python的and-or语法

    ```
    >>> a = "first"
    >>> b = "second"
    >>> 1 and a or b
    'first'
    >>> 0 and a or b
    'second'
    ```
    和C语言中的 双目运算符  bool ？a ：b相似 
    第一部分计算为真  则返回a， 若第一部分计算为假，则返回b
    
    注意： 当c为空串时, and or会失败， 想要用的话  就用列表 [""] 永远不为假
    ```
    >>> c = ""
    >>> 1 and c or b
    'second'
    >>> 1 and [c] or b
    ['']
    ```

17. python 是如何进行类型转换的

    python 提供了将变量或值从一种类型转换成另一种类型的内置函数 
    ```
    >>> int('123')  #字符串转整数
    123
    >>> str(123)
    '123'
    >>> float('123')
    123.0
    >>> float(123)
    123.0
    ```

18. python如何实现单例模式？其他23种设计python如何实现？

    方1: 使用__metaclass__(元类)的高级python用法   python2 中可用 python3 不可用
    ```python
    class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


    class Myclass(object):
        __metaclass__ = Singleton


    one = Myclass()
    two = Myclass()

    two.a = 3
    print(two.a)
    print(one.a)

    print (id(one))
    print (id(two))
    # python 2 执行结果为：
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% python fileout.py
    3
    3
    4359780624
    4359780624
    
    #python3 为one.a属性， 注释后执行结果为：
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% /Users/guogx/anaconda3/bin/python fileout.py
    3
    4314905288
    4314905232
    ```
    方2:使用装饰器（decorator）, 这是一种更pythonic的方法
    单利类本身不知道自己是单例的 因为它本身（自己的代码）并不是单例的
    
    ```
    
    def singleton(cls, *args, **kwargs):
        instances = {}
        def _singleton():
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]
        return _singleton

    @singleton
    class Myclass4(object):
        a = 1
        def __init__(self, x=0):
            self.x = x

    one = Myclass4()
    two = Myclass4()

    two.a = 3
    print(two.a)
    print(one.a)

    print (id(one))
    print (id(two))
    #执行结果
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% python fileout.py
    3
    3
    4380547600
    4380547600
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% 
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% 
    guogx@guogxdeMacBook-Pro:~/git/Bee/daemon_s% /Users/guogx/anaconda3/bin/python fileout.py
    3
    3
    4520997160
    4520997160
    ```

19. 如何用python来进行查询和替换一个文本字符串
    
    可以使用sub()方法进行查询和替换， sub方法的格式为sub(replacement, string, [count=0])
    replacement是被替换成的文本， string为待替换的字符串， count是一个可选参数，指最大被替换的数量
    ```python
    import re


    string = "blue socks and red socks"
    p = re.compile('blue|red')
    replace = 'colour'


    newstring = p.sub(replace, string)

    newstring1 = p.sub(replace, string, count=1)

    print(newstring)
    print(newstring1)

    #执行结果
    #colour socks and colour socks
    #colour socks and red socks
    ```

20. 有没有一个工具可以帮助查找python的bug和进行静态的代码分析
    
    PyChecker是一个python代码的静态分析工具，它可以帮助查找python代码的bug，会对代码的复杂度和格式提出警告
    Pylint是另外一个工具可以进行codestandard检查

21. 有两个序列a,b 大小都为n， 序列元素的值是任意整数值，无序，要求：通过交换a，b中的元素，使【序列a元素的和】与【序列b元素的和】之间的差最小

    
    a = [100, 99, 98, 1, 2, 3]

    b = [1, 2, 30, 4, 5, 40]
    ```python
    def mean(sorted_list):
        if not sorted_list:
            return ([], [])
        big = sorted_list[-1]
        small = sorted_list[-2]
        big_list, small_list = mean(sorted_list[:-2])


        big_list.append(small)
        small_list.append(big)


        big_list_sum = sum(big_list)
        small_list_sum = sum(small_list)

        if big_list_sum > small_list_sum:
            return ((big_list, small_list))
        else:
            return ((small_list, big_list))




        a = [100, 99, 98, 1, 2, 3]

        b = [1, 2, 30, 4, 5, 40]

        b.extend(a)
        b.sort()

        b1, b2 = mean(b)
        print(b1, b2)
        print(sum(b1)-sum(b2))

    ```

22. 两个整数数组各有100亿条数据， 并已经排序，保存在磁盘上，内存10M
问：
（1）如何取得交集？时间和空间效率多少？python集合set（）操作方法
（2）如果其中一个数组只有100条数据，如何优化算法取得交集？时间和空间效率分别是多少
（3）用自己熟悉的语言实现第2个问题，要求可以正常运行，假设已经提供函数read_elt(array_name, index)
可以用来读取某个数组的第index个元素，元素个数分别用m=100和n=10^10表示。

23. 请用自己的算法， 按升序合并如下两个list，并去除重复的元素

    l1 = [2,3,8,4,9,5,6]
    l2 = [5,6,10,17,2] 
    ```
    l2.extend(l1)
    list(set(l2))
    >>> list1 = [2,3,8,4,9,5,6]
    >>> list2 = [5,6,10,17,2]
    >>> list2.extend(list1)
    >>> list1
    [2, 3, 8, 4, 9, 5, 6]
    >>> list2
    [5, 6, 10, 17, 2, 2, 3, 8, 4, 9, 5, 6]
    >>> set(list2)
    {2, 3, 4, 5, 6, 8, 9, 10, 17}
    >>> list(set(list2))
    [2, 3, 4, 5, 6, 8, 9, 10, 17]

    #方1： set()方法  返回即是有序列表

    #方2: 遍历去重
    list1 = [5, 6, 10, 17, 2, 2, 3, 8, 4, 9, 5, 6]
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)

    #方3，列表推导
    list1 = [5, 6, 10, 17, 2, 2, 3, 8, 4, 9, 5, 6]
    list2 = []
    [list2.append(i) for i in list1 if not i in list2]

    ```

24. python 如何删除一个文件

    os.remove(path) #path是文件的路径
    os.rmdir(path) 文件夹为空才能被删除

25. python如何copy一个文件

    python 复制文件方法有9种
    * shutil copy()  copy(source_file, [destination_file or dest_dir])   类似与unix命令cp
    * shutil copyfile()   copyfile(source_file, destination_file)
    * shutil copyfileobj()   
    * shutil copy2()
    * os.popen    os.popen('cp 1.txt 2.txt')
    * os.system
    * threadig Thread() 方法
    * subprocess call() 方法
    * subprocess check_output() 方法

26. python程序中文输出文件如何解决 

    在文件中注释中文问题，采用在文件的第一行 # coding=UTF-8
    使用encoding 和 decoding
    
    例如：
    ```python
    name = "中国"
    name_s = name.encoding("utf-8")
    name_d = name_s.decode('utf-8')
    print(name_d)
    ````
    
27. 迭代器和生成器的区别

    1. 迭代器是一个更抽象的概念，任何对象，如果它的类有next方法和iter方法返回自己本身。对于string，list，dict，tuple等这类容器对象，使用for循环遍历是很方便的。在后台for语句对容器对象调用iter（）函数，iter（）是python内置函数。iter()会返回一个定义了next()方法的迭代器对象，在容器中逐个访问容器元素，next()也是python的内置函数。在没有后续元素时， next()会抛出一个stopiteration异常
    2. 生成器（generator）是创建迭代器简单而强大的工具，yeild关键字。它们写起来就像正规的函数，只是在需要返回数据的时候用yeild语句。在每次next()被调用时，生成器会返回它脱离的文职。
    区别：生成器能做到迭代器能做的所有事，而且因为自动创建了_iter__()和next()方法， 生成器显得特别简洁，而且生成器是高效的，使用生成器取代列表解析可以同时节省内存，除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出stopiteration异常

28. python代码得到列表的list的交集和差集

    ```
    a = [1, 2, 3]
    b = [2, 3, 4]
    
    #交集
    c = [val for val in a if val in b]
    print(c)
    #[2, 3]
    
    #差集
    d = [val for val in a if val not in b]
    print(d)
    #[1, 4]
    
    ```

29. 写一个简单的python socket编程。  server端 client端

    server端
    ```
    import socket
    import sys


    def start_tcp_server(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        sock.bind(server_address)

        try:
            sock.listen(5)
        except socket.error:
            sys.exit(1)

        while True:
            print("waiting for connection")

            connection, addr = sock.accept()
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('welcome to server!')
            else:
                connection.send('Please go out!')

            connection.close()


    if __name__ == '__main__':
        start_tcp_server("127.0.0.1", 8008)
    ```
    
    client端
    ```
    import socket


    def start_tcp_client(host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        sock.send("2")
        print(sock.recv(1024))
        sock.close()


    if __name__ == '__main__':
        start_tcp_client("127.0.0.1", 8008)
    
    ```


30. python如何捕获异常，如何创建自己的异常，如何传递异常try except else   try except finaly的用法 or 介绍一下python的异常处理机制和自己开发过程中的体会
    
    python的异常处理机制：
    try：尝试抛出异常
    raise：引发异常
    except：处理异常
    finally： 是否发生异常都是需要做的事
    创建新的异常类， 需要继承Exception类，可以定义类的属性，便于处理异常
    
    开发体会：
    异常主要用于处理读取文件，也可以使用with的方法读取文件，还可以用于网络连接， 异常可以包含大量的错误信息，进行错误处理
    
    捕获异常，又再次触发异常， 使用raise关键字
    使用try和except语句来捕获异常
    ```
    try:
        block
    except [exception, [data ...]]:
        block
        
    try:
        block
    except [exception, [data ...]]:
        block
    else:
        block
        
    try:
        block
    except [exception, [data ...]]:
        block
    finaly:
        block
    ```
    用raise语句传递异常或者引发一个异常：
    ```
    try:
        raise MyError #自己定义一个异常
    except MyError:
        print('a error')
        raise ValueError, 'invalid argument'
    ```

31. 在python中 list tuple dict set有什么区别 主要应用在什么样的场景？

    list 列表，有序的 ，通过索引来进行查找 使用方括号 ‘[]'
    tuple 元组， 元组将多样的对象集合到一起， 不能修改， 通过索引进行查找， 使用括号“（）“
    dict 字典， 字典是一组键值对(key,value)的组合，通过key进行查找， 没有顺序， 使用大括号‘{}’
    ser 集合， 无序， 元素只出现一次， 自动去重， 使用“set([])”
    
    应用场景：
    list 简单的数据集合， 可以使用索引
    tuple 把一些数据当做一个整体去使用，不能修改
    dict 使用键和值进行关联的数据
    set 数据只出现一次 只关系数据是否出现  不关心其位置
    
    ```
    >>> a = [1, 2, 3]
    >>> a[0]
    1
    >>> a[1]
    2
    >>>
    >>> b = (1, 2 ,3)
    >>> b[1]
    2
    >>> c = {'name': "China", "age": 300}
    >>> c["name"]
    'China'
    >>> c["age"]
    300
    >>> for i in a:
    ...     print(i)
    ...
    1
    2
    3
    >>> for i in b:
    ...     print(i)
    ...
    1
    2
    3
    ```

32. 类的静态函数函数（@staticmethod），类函数(@classmethod)， 类成员函数的区别 or python类中self的含义

    #http://www.cnblogs.com/Wang-Wenhui/p/8909320.html
    静态函数（@staticmethod）:静态方法，主要处理与这个类的逻辑关联， 不可以访问实例变量或类变量的
    类函数（@classmethod）：类方法，只能访问类变量，不能访问实例变量
    成员函数： 实例的方法，只能通过实例进行调用，若需通过类名调用，则应申明为类方法。
    属性函数（@property）：把一个方法通过@property变成一个静态属性
    
    具体应用：
    通过类的方法（@classmethod）进行数据转换，传入参数cls
    通过类的静态方法：进行数据验证

33. a=1, b=2 不用中间变量交换a和的值
    
    方1:
    b, a = a, b
    
    方2:
    a = a + b
    b = a - b
    a = a - b
    
    方3: ^ 异或运算符
    a = a^b
    b = a^b
    a = a^b
    

35. 写一个函数，输入一个字符串，返回倒序排列的结果 如 string_reverse(‘abcdefg’)输出为gfedcba
    #https://www.jianshu.com/p/d282155d96e8
    
    #方1:使用字符串本身的翻转
    def string_reverse(text='abcdefg')
        return text[::-1]
        
    #方2:将字符串变为列表  用列表的reverse函数
    def string_to_list(text='abcdefg')
        new_text = list(text)
        new_text.reverse()
        return ''.join(new_text)
        
    #方3: 递归
    def string_reverse（text='abcde'):
        if len(text)<=1:
            return text
        else:
            return string_reverse(text[1:]+text[0])
        
    

36. 说一下下面的代码片段存在的问题

    ```python
    from amodule import * # amodule is an exist module  

    class dummyclass(object):  
        def __init__(self):  
            self.is_d = True  
            pass  

    class childdummyclass(dummyclass):  
        def __init__(self, isman):  
            self.isman = isman  

        @classmethod  
        def can_speak(self): return True  

        @property  
        def man(self): return self.isman  

    if __name__ == "__main__":  
        object = new childdummyclass(True)  
        print object.can_speak()  
        print object.man()  
        print object.is_d
    ```

        1. __init__中 用pass
        2. 用object关键字命名实例化对象， object不应该被重新定义
        3. @classmethod 类函数与成员函数区分开用cls
        4. 使用new新建一个对象
        5. 类名尽量大写

37. 解释一下WSGI和FAstCGI的关系

38. 解释一下Django和torando关系， 差别

39. 解释一下Django使用redis缓存服务器

40. 如何进行Django单元测试

41. 分别简述OO，OOA

    OO: object-oriented,面向对象，基于对象的概念，以对象为中心，以类和继承为构造机制，来认识，理解，刻画客观世界和设计，构建相应的软件系统的一种方法， 本意是模拟人类的思维方法   使开发维护修改更加容易
    OOA：object-oriented-analysis 面向对象分析，强调的是系统调查资料的基础上，针对OO方法所需的素材进行的归类分析和整理，不是对管理业务现状和方法的分析，其实就是进一步对OO进行细化，初步得出OO的方法，或者理解为：在得出的文档中对接口进行粗略定义
    OOD：object-oriented-design, 面向对象设计，主要作为是对ooA分析的结果进一步的规范和整理，以便能够被OOP直接接受--整理和定义OO的属性和方法
    OOP：object-oriented-progarmming 把组件的实现和接口分开，并且让组件具有多态性--（抽象 封装 继承 多态）面向接口编程

42. 简述正则表达式中？p的含义

43. 请写出python的常用内置函数（至少3个），并描述它们的具体含义

    abs() 求绝对值
    all() 判断元素中所有元素是否为真值
    any() 判断元素中是否有元素为真
    next(）返回可迭代对象的下一个值
    int(), str(), list(), tuple(), dict(), set()
    enumerate() 根据可迭代对象创建枚举对象
    range() 根据传入的参数创建一个新的range对象
    slice() 进行切片函数
    sorted() 进行排序
    isintance() 判断是否int类型 是返回True
    zip() 聚合传入的每个迭代器中相同位置的元素，返回一个新的元组类型迭代器
    help(), dir(), id(）， type()
    format() 格式化显示值
    getattr() 获得对象的属性值
    setattr() 设置对象的属性值
    ...

44. 可以用python进行post数据提交，可以加载什么模块进行操作？在操作之前需要对数据进行什么操作？

    requests模块
    对数据进行json格式化 json.dump

45. 说出python中间件 Sqlalchemy的具体申明方式？以及模块与mysqldb之间的区别？

46. 描述3个常用的python框架，并简要描述这些框架的优缺点？
flask tornado Django

47. reactor是什么？有什么作用？ 请简要描述

48. 请描述2种不同语言间数据流转通用格式

    json: json是一种轻量级的数据交换格式；
    json的优点 
    * 易于人阅读和编写。同时易于机器解析和生成
    * 同xml和html片段相比，json提供了更好的简单性和灵活性
    * 非常适合服务器和javascript的交互
    
    xml： xml是当前编程中最为流行的数据交换格式，拥有跨平台，跨语言的优势。
    
    yaml：yaml是一种直观的能够被电脑识别的数据数据序列化格式
         换种说法，yaml是一种很简单的类似与xml的数据描述语言，语法比xml简单很多
    yaml优点：
    * 可读性好
    * 和其它脚本语言的交互性好哦
    * 使用实现语言的数据类型
    * 提供了一个一致的信息模型
    * 可以基于流来处理
    * 表达能力强，扩展性好
    * 易于实现
    
49. 简述我们使用多线程编程时，锁与信号量之间的关系

50. 有100个磁盘组成的存储系统， 当有3个磁盘同时损坏时，才会发生数据丢失。如何1个损坏率是p，请问整个存储系统丢失数据的概率是多少？

51. 假设fd是一个socket， read(fd,buf,1024)
    问：可能返回哪些值？其代表什么含义

52. 假设网络会丢失消息，进程可能意外终止， 磁盘可靠（写入数据后不会丢失）
    问：
    如何构建一个可靠的分布式key-value存储系统？
    答题要求如下：
    1. 客户端向系统发送1条写入请求（例如：key=x，value=1），系统返回’成功’，
    客户端一定可以正确读取到key=y的值
    2.在你设计的系统中，要满足上面一条，并有一定的容错能力
    3.如果要尽可能提高写入或读写成功率， 如何改进系统设计？分别会有哪些问题？

53. python语言有哪些缺陷
    
    优点：
    1. python的定位是“优雅”，‘明确’，‘简单’ 所以python简单易懂
    2. 开发效率非常高， 有着强大的第三方库，大大降低开发周期，避免重复造轮子
    3. 高级语言 无须考虑管理你程序中使用的内存
    4. 可移植性 python可以在多平台上运行
    5. 可扩展性 支持C／C++代码的扩展
    6. 可嵌入性 可以把python代码嵌入在c／c++程序中，从而向你的程序用户提供脚本功能
    缺点：
    1. 速度慢 python的运行速度比c语言慢很多 ，和java比也慢一些。对速度要求高的 建议与c／c++来编写
    2. 代码不能加密 因为python是解释型语言，它的源码都是明文形式存放 如果项目要求源代码必须是加密，那一开始就不应该用python来去实现
    3. 线程不能利用多cpu问题。 GIl全局解释器锁的存在，是python解释器同步线程的工具。一个python解释器进程内一个主线程，以及多条用户程序的执行线程。

54. python是解释型的还是编译型的？
    
    计算机不能够识别高级语言  所以当我们运行一个高级语言程序的时候， 就需要一个'翻译机'来从事把高级语言变成计算机能读懂的机器语言的过程。这个过程分为两类：第一种是编译，第二种是解释
    编译型语言在程序执行之前，先会通过编译器对程序执行一个编译的过程，把程序转变成集齐语言，运行时不需要再编译，而直接执行就可以啦，典型的就是C语言
    解释型语言没有这个编译过程，而是在程序运行的时候，通过解释器对程序逐行做出解释，然后直接运行 比如python
    python 是解释型的

55. 现在有一个dict对象adict，里面有一百万个对象，查找其中的某个元素的平均需要多少次比较？一千万个元素呢？
    
    O(1) 哈希字典， 快速查找，  字典键值映射， 键唯一

56. 现在有一个list对象alist，里面所有元素都是字符串，编写一个函数对它实现一个大小写无关的排序

    使用lambda表达式
    ```
    >>> words = ["I", "am", "Chinese"]
    >>> words
    ['I', 'am', 'Chinese']
    >>> words.sort()
    >>> words
    ['Chinese', 'I', 'am']
    >>> words.sort(key=lambda x:x.lower())
    >>> words
    ['am', 'Chinese', 'I']
    >>>
    ```

57. 有一个排好序的list对象alist 查找其中是否有某元素a（尽可能的使用标准库函数）
    
    ```python
    words = ["I", "am", "Chinese"]
    try:
        words.index('I')
        print("find it")
    except ValueError:
        print('Not Found')
        
    >>> words.index('I')
    2
    >>> words.index('i')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 'i' is not in list
    ```
    
58. 实现一个stack

    ```
    class Stack:
    def __init__(self):
        self.__items = []

    def isempty(self):
        return len(self)==0

    def __len__(self):
        return len(self.__items)

    def peek(self):
        assert not self.isempty()
        return self.__items[-1]

    def push(self, value):
        self.__items.append(value)

    def pop(self):
        assert not self.isempty()
        return self.__items.pop()


    s = Stack()
    print(s.isempty())
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.peek())
    ```

59. 编写一个简单的ini文件解释器

60. 现有N个纯文本格式的英文文件，实现一种检索方案，即做一个小店搜索引擎

61. nginx的正向代理与反向代理？

    正向代理 是一个位于客户端和原始服务器（origin server）之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标（原始服务器），然后代理向原始服务器转交请求并将获得的内容返回给客户端。客户端必须要进行一些特别的设置才能使用正向代理。
    反向代理正好相反，对于客户端而言它就像原始服务器，并且客户端不需要进行任何特别的设置。客户端向反向代理的命名空间中的内容发送普通请求，接着反向代理将判断向何处（原始服务器）转交请求，并将获取的内容返回给客户端，就像这些内容原本就是它自己的一样。
     
62. python is 和 ==的区别

    is 是判读两个对象标识符是否相等 对象的id（是否相等）
    == 判读两个对象的值是否相等
    ```
    a = 'hello'
    b = 'hello' 
    a is b True
    a == b True
    a = 'hel lo'
    b = 'hel lo'
    a is b False
    a == b True
    ```
    当对象中只含有字母含大小写，数字，下划线时 python会维护一张字典使这些字符串全局唯一，也就是intern机制
    
63. 闭包

    闭包可以实现先将一个参数传递给一个函数，而并不立即执行，以达到延迟求值的目的。满足以下三个条件：
    1. 必须有一个内嵌函数
    2. 内嵌函数必须引用外部函数中变量
    3. 外部函数返回值必须是内嵌函数
    ```
    def delay_fun(x, y):
        def caculator():
            return x+y
        return caculator
        
    msum = delay_fun(2, 3) 
    print(msum())
     
    ```

64. \*args和\*\*kwargs
    
    这两个都是python的可变参数，用于接受参数的传递。\*args表示任何多个无名参数，它是一个元组，\*\*kwargs表示关键字参数，它是一个字典。同时使用这两个参数时， args必须在kwargs前面
    
65. python中断言方法举例
    
    assert()方法，断言成功， 程序继续执行，断言失败，则程序报错抛出异常
    ```
    a = 3
    assert (a>2)
    print('ddddd')

    b = 5

    assert (a>6)
    print('pppppp')
    
    #执行结果
    ddddd
    Traceback (most recent call last):
      File "test.py", line 7, in <module>
        assert (a>6)
    AssertionError
    guogx@guogxdeMacBook-Pro:~/git/Bee/obt% python test.py
    ddddd
    Traceback (most recent call last):
      File "test.py", line 7, in <module>
        assert (a>6)
    AssertionError

    ```
        
66. 提高python运行效率的方法
    
    1. 使用生成器，因为可以节约大量内存
    2. 循环代码优化， 避免过多重复代码的执行
    3. 核心模块采用cpython pypy等，提供效率
    4. 多进程，多线程，协程
    5. 多个if elif条件判断，可以把最有可能发生的条件放到前面写，这样可以减少判断的次数，提高效率

67. 简述redis 和 mysql的区别
    
    redis：内存型 非关系数据库，数据保存在内存中，速度快
    mysql：关系型数据库 数据保存在硬盘中， 检索的话 会有一定的IO操作 访问速度相对慢
    
68. 简述下 cookie和session的区别
    
    1. session在服务端，cookie在客户端
    2. session的运行依赖session id 而sessionid在cookie中，也就是说，如果浏览器禁用了cookie 同时session也会失效，存储session时，键与cookie中的sessionid相同，值是开发人员设置的键值对信息，进行lbase64编码， 过期时间由开发人员设置
    3. cookie的安全型比session差

69. python中什么元素为假？
    0 空字符串 空列表 空字典 空元组 None False
 
70. 简述乐观锁和悲观锁
    https://zhuanlan.zhihu.com/p/54430650
    悲观锁，就是很悲观，每次去拿数据的时候都认为别人会修改，所以每次拿数据的时候都会上锁，这样别人想拿这个数据就会block直到它拿到锁。传统的关系型数据库里边就用到了很多这种锁机制，比如行锁，表锁等 读锁 写锁等 都是在操作之前上锁
    乐观锁，就是很乐观，每次去拿数据的时候都认为别人不会修改，所以不会上锁，但是在更新的时候会判断一下在次期间别人有没有去更新这个数据，可以使用版本好机制，乐观锁适用于多读的应用类型，这样可以提高吞吐量。

    
### 算法

1. 快排

    ```
    def qsort(seq):
        if seq==[]:
            return []
        else:
            pivot=seq[0]
            lesser = qsort([x for x in seq[1:] if x < pivot])
            greater = qsort([x for x in seq[1:] if x >= pivot])
        return lesser+[pivot]+greater

    seq = [5,6,78,9,0,-1,2,3,-65,12]
    print(qsort(seq))

    #运行结果
    [-65, -1, 0, 2, 3, 5, 6, 9, 12, 78]

    ```
    



### 网络知识

1. 解释下http协议
   
   http协议是Hyper Text Transfer Protocol(超文本传输协议)的缩写，http协议和TCP/IP协议簇内的其他众多的协议相同，用于客户端和服务端之间的通信。请求访问文本或图像的等资源的一端称为客户端，而提供相应的一端称为服务端
   
   

2. 解释下http请求头和常见的状态相应码
    
    请求方法
    HTTP1.0 定义了三种请求方法：GET POST HEAD方法
    HTTP1.1 新增了五种请求方法：OPTIONS PUT DELETE TRACE 和 CONNECT方法
    GET：用于请求访问已经被URL（统一资源标识符）识别的资源，可以通过URL传参给服务器
    POST：用于传输信息给服务器，主要功能与get方法类似，但是一般推荐post方法
    PUT：传输文件，报文主体中包含文件内容，保存到相应URL位置
    HEAD：获取报文首部，与get方法类似，只是返回的不是报文主体，一般用于验证URL是否有效
    DELETE：删除文件，与put方法相反，删除对应URL位置的文件
    OPRTIONS：查询相应URL支持的Http方法
    

    常见的状态响应码：
    * 1XX：指示信息-表示请求已接收，继续处理
    * 2XX：成功-表示请求已被成功接收、理解、接受
    * 3XX：重定向-要完成请求必须进行更进一步的操作
    * 4XX：客户端错误-请求有语法错误或请求无法实现
    * 5XX：服务端错误-服务器未能实现合法的请求

    * 200 OK 客户段请求成功
    * 301 永久重定向
    * 302 临时性重定向
    * 400 bad request
    * 401 Unauthorized
    * 403 Forbidden
    * 404 Not Found
    * 500 Internal Server Error
    * 503 Server Unavailable
    
3. 解释一下tcp／udp协议

    OSI Open System Interconnection 开放系统互联
    网络协议
    网络分层，有三种模型
    1. osi七层模型：应用层 表示层 会话层 传输层 数据链路层 网络层 物理层
    2. 因特而五层模型：比OSI少了表示层和会话层
    3. TCP（传输控制协议）／ IP（因特网协议）模型。TCP和ip都是两个协议，只是因为这在网络协议中比叫重要，因此来命名的。该模型就是实现两台电脑互联的遵守的协议。这协议分为3层：传输层 网络层 网络接口层
    
    TCP／UDP的区别
    * tcp是面向连接的 udp是面向无连接的
    * udp程序结构简单
    * tcp是面向字节流 udp是面向数据报
    * tcp保证数据正确性，udp可能丢包
    * tcp保证数据顺序，udp不保证
    
    为啥tcp是安全的
    建立连接时 ： tcp的三次握手 四次分手
    

### Linux知识：

1. 常用的linux命令
ps, ls, mkdir, touch, cp, scp, rm, top, virt-what, help, mv, ifconfig, telnet, cat, tail, grep, find, tcpdump, awk, tar, pwd, more, su, date


### 某公司大厂：

1. python和redis的c语言低层实现

2. 有一个数组，里面只有一个值是唯一的， 其余都是重复成对出现的。请设计一个算法，在o1的空间复杂度和on的时间复杂度内，找出这个值
    
    ```
    x = [1, 2, 3, 4, 5, 4, 3, 2, 1, 5, 33333]

    num = len(x)

    a = 0
    for i in range(num):
        a ^= x[i]

    print(a)
    
    # result:
    33333
    ```

3. 请实现二叉树的广度遍历

### 数据库 
    
    MYSQL基本语法
    1. 增加：创建数据库表
        use database
        create table test(id int(2), name varchar(20))
    2. 删
        alter table 表名(test) drop s属性名(int); #删除字段
        drop table 表名(test); #删除表
    3. 改
        alter table 旧表名 rename 新表名; #修改表，名
        alter table 表名 modify   属性名 数据类型; #修改字段数据类型
    4. 查
        select * from 表名;
        select * from 表名 where id=1; 条件查询
        select * from 表名 where 字段名 between 条件1 and 条件2； 范围查询
        select count(*) from 表名；#查询表共有多少条记录
    5. 触发器
        是由insert，update，delete等事件来触发某种特定操作，满足触发条件时，数据库系统会执行触发器中定义的语句，这样可以保证某些操作之间的一致性
    
    登录数据库  mysql -u root -p
    1. 数据库操作：
        #新建一个数据库 
        mysql> create database company charset=utf8;
        Query OK, 1 row affected (0.02 sec)
        
        mysql> show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | company            |
        | mysql              |
        | performance_schema |
        | profile            |
        | sys                |
        +--------------------+
        6 rows in set (0.00 sec)

        mysql> use company;
        Database changed
        # 
        mysql> create table yuangong(name varchar(20), id int(4));
        Query OK, 0 rows affected (0.00 sec)

        mysql> show tables;
        +-------------------+
        | Tables_in_company |
        +-------------------+
        | yuangong          |
        +-------------------+
        
        #删除数据库
        mysql> drop database company;
        Query OK, 1 row affected (0.02 sec)

        mysql> show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |
        | performance_schema |
        | profile            |
        | sys                |
        +--------------------+
        
    2. 查看数据库中的所有库
        show databases;
        mysql> show databases;
        +--------------------+
        | Database           |
        +--------------------+
        | information_schema |
        | mysql              |  
        | performance_schema |
        | profile            |
        | sys                |
        +--------------------+
    3. 进入profile数据库
        mysql> use profile;
        Reading table information for completion of table and column names
        You can turn off this feature to get a quicker startup with -A

        Database changed
        #查看数据库中的所有表
        show tables;
        mysql> show tables;
        +-------------------+
        | Tables_in_profile |
        +-------------------+
        | name              |
        +-------------------+
        1 row in set (0.00 sec)

        # 重命名表名
        mysql> rename table name to students;
        Query OK, 0 rows affected (0.03 sec)

        mysql> show tables;
        +-------------------+
        | Tables_in_profile |
        +-------------------+
        | students          |
        +-------------------+
        1 row in set (0.00 sec)
        #查看表的结构 desc students;
        mysql> desc students;
        +-------+---------+------+-----+---------+----------------+
        | Field | Type    | Null | Key | Default | Extra          |
        +-------+---------+------+-----+---------+----------------+
        | id    | int(3)  | NO   | PRI | NULL    | auto_increment |
        | xm    | char(8) | YES  |     | NULL    |                |
        | xb    | char(2) | YES  |     | NULL    |                |
        | csny  | date    | YES  |     | NULL    |                |
        +-------+---------+------+-----+---------+----------------+
        #查看表中所有的内容 select * from students;
        mysql> select * from students;
        +----+--------+------+------------+
        | id | xm     | xb   | csny       |
        +----+--------+------+------------+
        |  1 | guogx  | M    | 1990-06-06 |
        |  2 | Lina   | W    | 2001-07-28 |
        |  4 | ee     | W    | 2018-08-09 |
        |  5 | diudiu | z    | 2018-08-09 |
        |  6 | ff     | W    | 1933-02-01 |
        +----+--------+------+------------+
        5 rows in set (0.00 sec)

        # 带条件查找
        mysql> select * from students where xm='guogx';
        +----+-------+------+------------+
        | id | xm    | xb   | csny       |
        +----+-------+------+------------+
        |  1 | guogx | M    | 1990-06-06 |
        +----+-------+------+------------+
        1 row in set (0.00 sec)
        
        # 增加表中的内容
        mysql> insert into students values(100, 'zhuzhu', 'W', '2019.01.01');
        Query OK, 1 row affected (0.00 sec)

        mysql> select * from students;
        +-----+--------+------+------------+
        | id  | xm     | xb   | csny       |
        +-----+--------+------+------------+
        |   1 | guogx  | M    | 1990-06-06 |
        |   2 | Lina   | W    | 2001-07-28 |
        |   4 | ee     | W    | 2018-08-09 |
        |   5 | diudiu | z    | 2018-08-09 |
        |   6 | ff     | W    | 1933-02-01 |
        | 100 | zhuzhu | W    | 2019-01-01 |
        +-----+--------+------+------------+
        # 修改表中的内容
        mysql> update students set xm='mimi',xb='x' where id=6;
        Query OK, 1 row affected (0.00 sec)
        Rows matched: 1  Changed: 1  Warnings: 0

        mysql> select * from students;
        +-----+--------+------+------------+
        | id  | xm     | xb   | csny       |
        +-----+--------+------+------------+
        |   1 | guogx  | M    | 1990-06-06 |
        |   2 | Lina   | W    | 2001-07-28 |
        |   4 | ee     | W    | 2018-08-09 |
        |   5 | diudiu | z    | 2018-08-09 |
        |   6 | mimi   | x    | 1933-02-01 |
        | 100 | zhuzhu | W    | 2019-01-01 |
        +-----+--------+------+------------+
        # 删除表中的内容
        mysql> delete from students where id=4;
        Query OK, 1 row affected (0.00 sec)

        mysql> select * from students;
        +-----+--------+------+------------+
        | id  | xm     | xb   | csny       |
        +-----+--------+------+------------+
        |   1 | guogx  | M    | 1990-06-06 |
        |   2 | Lina   | W    | 2001-07-28 |
        |   5 | diudiu | z    | 2018-08-09 |
        |   6 | mimi   | x    | 1933-02-01 |
        | 100 | zhuzhu | W    | 2019-01-01 |
        +-----+--------+------+------------+
       
       # 新建数据库表
        mysql> create table flowers(name varchar(20), color int(1));
        Query OK, 0 rows affected (0.01 sec)

        mysql> show tables;
        +-------------------+
        | Tables_in_profile |
        +-------------------+
        | flowers           |
        | students          |
        +-------------------+
        2 rows in set (0.00 sec)

        mysql> desc flowers;
        +-------+-------------+------+-----+---------+-------+
        | Field | Type        | Null | Key | Default | Extra |
        +-------+-------------+------+-----+---------+-------+
        | name  | varchar(20) | YES  |     | NULL    |       |
        | color | int(1)      | YES  |     | NULL    |       |
        +-------+-------------+------+-----+---------+-------+
        
        # 删除数据库表 drop table 表名
        mysql> drop table flowers;
        Query OK, 0 rows affected (0.02 sec)
        
        mysql> show tables;
        +-------------------+
        | Tables_in_profile |
        +-------------------+
        | students          |
        +-------------------+
