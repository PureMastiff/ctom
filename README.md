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

11-1. python是如何进行内存管理的 
    一，垃圾回收：
    python和C++java等语言不同，他们可以不用事先声明变量类型而直接对变量进行赋值。对python语言来讲，对象的类型和内存都是在运行时确定的。这也是为什么我们称python语言为动态类型的原因（这里我们把动态类型可以简单的归结为对变量内存地址的分配是在运行时自动判断变量类型并对变量进行赋值）
    二，引用计数
    Python采用了类似windows内核对象一样的方式来进行内存管理。每一个对象，都维护这一个对指向该对对象的引用的计数。当变量被绑定在一个对象上的时候，该变量的引用计数就1，系统会自动维护这些标签，并定时扫描，当某标签的引用计数为0的时候， 该对象就会被回收。

11-2. python多进程中共享内存Value和Array
    *https://www.cnblogs.com/gengyi/p/8661235.html*
    （1）共享内存是一种最为高效多进程间通信方式，进程可以直接读写内存，而不需要任何数据多拷贝。
    （2）为了在多个进程间交换信息，内核专门留出一块内存区，可以由需要访问的进程将其映射到自己的私有地址空间。进程就可以直接读写这一块内存而不需要进行数据的copy，从而大大提高了效率（文件映射）
    （3）由于多个进程共享一块内存， 因此也需要依靠某种同步机制。
    优缺点：
    优点：快速在进程间传递参数
    缺点：数据安全上存在风险，内存中的内容会被其他进程覆盖或更改
    ```
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

13. python读取大文件？限制内存
（1）. 利用生成器generator
（2）迭代器进行遍历： for line in file
14. 如何用python输出一个Fibonacci数列？
15. 介绍一个python中webbrowser的用法
16. 解释一下python的and-or语法
17. python 是如何进行类型转换的
18. python如何实现单例模式？其他23种设计python如何实现？
19. 如何用python来进行查询和替换一个文本字符串
20. 有没有一个工具可以帮助查找python的bug和进行静态的代码分析
21. 有两个序列a,b 大小都为n， 序列元素的值是任意整数值，无序，要求：通过交换a，b中的元素，使【序列a元素的和】与【序列b元素的和】之间的差最小
22. 两个整数组各有100亿条数据， 并已经排序，保存在磁盘上，内存10M
问：
（1）如何取得交集？时间和空间效率多少？python集合set（）操作方法
（2）如果其中一个数组只有100条数据，如何优化算法取得交集？时间和空间效率分别是多少
（3）用自己熟悉的语言实现第2个问题，要求可以正常运行，假设已经提供函数read_elt(array_name, index)
可以用来读取某个数组的第index个元素，元素个数分别用m=100和n=10^10表示。
23. 请用自己的算法， 按升序合并如下两个list，并去除重复的元素
list1 = [2,3,8,4,9,5,6]
list2 = [5,6,10,17,2] 
24. python 如何删除一个文件
os.remove()
25. python如何copy一个文件
26. python程序中输出文件如何解决  #写入log文件
27. 迭代器和生成器的区别
1. 迭代器是一个更抽象的概念，任何对象，如果它的类有next方法和iter方法返回自己本身。对于string，list，dict，tuple等这类容器对象，使用for循环
遍历是很方便的。在后台for语句对容器对象调用iter（）函数，iter（）是python内置函数。iter()会返回一个定义了next()方法的迭代器对象，在容器中逐个
访问容器元素，next()也是python的内置函数。在没有后续元素时， next()会抛出一个stopiteration异常
2. 生成器（generator）是创建迭代器简单而强大的工具，yeild关键字。它们写起来就像正规的函数，只是在需要返回数据的时候用yeild语句。在每次next
()被调用时，生成器会返回它脱离的文职。
区别：生成器能做到迭代器能做的所有事，而且因为自动创建了_iter__()和next()方法， 生成器显得特别简洁，而且生成器是高效的，使用生成器取代列表解析可以
同时节省内存，除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出stopiteration异常
28. python代码得到列表的list的交集和差集
29. 写一个简单的python socket编程。  server端 client端
30. python如何捕获异常，如何创建自己的异常，如何传递异常try except else   try except finaly的用法
or 介绍一下python的异常处理机制和自己开发过程中的体会
31. 在python中 list tuple dict set有什么区别 主要应用在什么样的场景？
32. 类的静态函数函数（@staticmethod），类函数(@classmethod)， 类成员函数的区别
or python类中self的含义
33. a=1, b=2 不用中间变量交换a和的值
34.  b,a = a,b
35. 写一个函数，输入一个字符串，返回倒序排列的结果 如 string_reverse(‘abcdefg’)输出为gfedcba
36. 说一下下面的代码片段存在的问题
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
1. __init__中 用pass
2.用object关键字命名实例化对象
3.@classmethod 类函数与成员函数区分开用cls
4. 使用new新建一个对象
37. 解释一下WSGI和FAstCGI的关系
38. 解释一下Django和torando关系， 差别
39. 解释一下Django使用redis缓存服务器
40. 如何进行Django单元测试
41. 分别简述OO，OOA
42. 简述正则表达式中？p的含义
43. 请写出python的常用内置函数（至少3个），并描述它们的具体含义
44. 可以用python进行post数据提交，可以加载什么模块进行操作？在操作之前需要对数据进行什么操作？
45. 说出python中间件 Sqlalchemy的具体申明方式？以及模块与mysqldb之间的区别？
46. 描述3个常用的python框架，并简要描述这些框架的优缺点？
flask tornado Django
47. recator是什么？有什么作用？ 请简要描述
48. 请描述2种不同语言间数据流转通用格式
49. 简述我们使用多线程编程时，锁与信号量之间的关系
50. 有100个磁盘组成的存储系统， 当有3个磁盘同时损坏时，才会发生数据丢失
。如何1个损坏率是p，请问整个存储系统丢失数据的概率是多少？
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
54. python是解释型的还是编译型的？
55. 现在有一个dict对象adist，里面有一百万个对象，查找其中的某个元素的平均需要多少次比较？一千万个元素呢？
56. 现在有一个list对象alist，里面所有元素都是字符串，编写一个函数对它实现一个大小写无关的排序
57. 有一个排好序的list对象alist 查找其中是否有某元素a（尽可能的使用标准库函数）
58. 实现一个stack
59. 编写一个简单的ini文件解释器
60. 现有N个纯文本格式的英文文件，实现一种检索方案，即做一个小店搜索引擎
61. nginx的正向代理与反向代理？
正向代理 是一个位于客户端和原始服务器（origin server）之间的服务器，为了从原始服务器取得内容，客户端向代理发送一个请求并指定目标（原始服务器），然后代理向原始服务器转交请求并将获得的内容返回给客户端。客户端必须要进行一些特别的设置才能使用正向代理。
反向代理正好相反，对于客户端而言它就像原始服务器，并且客户端不需要进行任何特别的设置。客户端向反向代理的命名空间中的内容发送普通请求，接着反向代理将判断向何处（原始服务器）转交请求，并将获取的内容返回给客户端，就像这些内容原本就是它自己的一样。

网络知识
1. 解释下http协议
2. 解释下http请求头和常见的状态相应码
3. 
Linux知识：
1. 常用的linux命令
ps, ls, mkdir, touch, cp, scp, rm, top, virt-what, help, mv, ifconfig, telnet, cat, tail, grep, find, tcpdump, awk, tar, pwd, more, su, date


某公司大厂：
1. python和redis的c语言低层实现
2. 有一个数组，里面只有一个值是唯一的， 其余都是重复成对出现的。请设计一个算法，在o1的空间复杂度和on的时间复杂度内，找出这个值
3. 请实现二叉树的广度遍历
