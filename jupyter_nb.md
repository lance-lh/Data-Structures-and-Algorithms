start jupyter:

1. `cd` 到指定目录
2. `jupyter notebook`

重新标号：

1. Kernel -> Restart
2. Cell -> Run All

***

Jupyter在顶部菜单提供了一个快捷键列表：Help > Keyboard Shortcuts 。每次更新Jupyter的时候，一定要看看这个列表，因为不断地有新的快捷键加进来。另外一个方法是使用Cmd + Shift + P (  Linux 和 Windows下 Ctrl + Shift + P亦可)调出命令面板。这个对话框可以让你通过名称来运行任何命令——当你不知道某个操作的快捷键，或者那个操作没有快捷键的时候尤其有用。这个功能与苹果电脑上的Spotlight搜索很像，一旦开始使用，你会欲罢不能。

- Esc + F 在代码中查找、替换，忽略输出。
-  Esc + O 在cell和输出结果间切换。
-  选择多个cell: 
  -  Shift + J 或 Shift + Down 选择下一个cell。
  -  Shift + K 或 Shift + Up 选择上一个cell。
  -  一旦选定cell，可以批量删除/拷贝/剪切/粘贴/运行。当你需要移动notebook的一部分时这个很有用。
-  Shift + M 合并cell. 

***

Jupyter Notebook包含两种模式。一种是命令模式，按ESC键进入，这时边框是蓝色的；另一种是编辑模式，按Enter键进入，边框是绿色的。

**MODE|KEY|COLOR**

**C|Esc|B**

**E|Enter|G**

使用到的快捷键会随时补充。

- 命令模式：
   shift + enter  : 运行当前单元后，选中下一单元
   ctrl + enter ：只运行当前单元
   Y  ： 切换code状态  
   M ： 切换Markdown状态
   A ：在上方插入单元格
   B ：在下方插入单元格
   连按两次D ：删除当前单元格
   连按两次 I ： 中断内核运行
   C ：复制当前单元格
   shift + v ：粘贴单元格
   L：显示代码框中每行的数字标识
   shift + L ：显示全部代码框中每行的数字标识

   shift + Tab：查看当前函数的说明（光标要在函数的位置内如下图所示）

  ![img](https:////upload-images.jianshu.io/upload_images/2759738-5d6e644e44ac6a2c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000/format/webp)

  

- 编辑模式：
   *编辑模式暂时用的不多，用到的时候再补充*
   shift + enter  : 运行当前单元后，选中下一单元
   ctrl + enter ：只运行当前单元

链接：https://www.jianshu.com/p/ccf71af2d050

***

Elementary matrix  初等矩阵

***

In this code:

```python
class A(object):
    def __init__(self):
        self.x = 'Hello'

    def method_a(self, foo):
        print self.x + ' ' + foo
```

... the `self` variable represents the instance of the object itself. Most object-oriented languages pass this as a hidden parameter to the methods defined on an object; Python does not. **You have to declare it explicitly**. When you create an instance of the `A` class and call its methods, it will be passed automatically, as in ...

```python
a = A()               # We do not pass any argument to the __init__ method
a.method_a('Sailor!') # We only pass a single argument
```

The `__init__` method is roughly what represents a constructor in Python. When you call `A()`Python creates an object for you, and passes it as the first parameter to the `__init__` method. Any additional parameters (e.g., `A(24, 'Hello')`) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.



**self :**

self represents the instance of the class. By using the "*self*" keyword we can access the *attributes* and *methods* of the class in python.

**__init__ :**

"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.



self指代类的实例，类似于c++中的this指针，区别在于c++中this是隐式给出的，而python需要显式给出。总之，self可以访问类的属性和方法。



init顾名思义为初始化，类似于c++的constructor，也就是说是一个构造函数，当实例化对象时就会调用init，从而完成初始化。



ref: [Understanding self and __init__ method in python Class.](https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/)

***

