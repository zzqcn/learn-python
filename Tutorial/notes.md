# 1 课前甜点

本语言的命名源自 BBC 的 “Monty Python 飞行马戏团”，与爬行动物无关（Python 原义为“蟒蛇”）。


# 2 使用 Python 的解释器

## 2.2 解释器的运行环境

默认情况下，Python 源码文件的编码是 UTF-8。

如果不使用默认编码，则要声明文件的编码，文件的 第一 行要写成特殊注释。句法如下：
```
# -*- coding: encoding -*-
```

第一行 的规则也有一种例外情况，源码以 UNIX "shebang" 行 开头。此时，编码声明要写在文件的第二行。例如：

```
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```


# 3 Python 速览

## 3.1 Python 用作计算器

### 3.1.1 数字

计算乘方的运算符是 `**`, 如:
```python
>>> 5 ** 2  # 5 的平方
25
>>> 2 ** 7  # 2 的 7 次方
128
```

交互模式下，上次输出的表达式会赋给变量 _。把 Python 当作计算器时，用该变量实现下一步计算更简单, 如:
```python
>>> 2 + 3
5
>>> 8 + _
13
```

## 3.1.2 文本

在交互式命令行中使用变量名直接输出字符串, 和通过 `print()` 函数输出字符串, 会有所不同.
后者会省略标示用的引号, 并打印经过转义的字符, 如:
```python
>>> s = 'First line.\nSecond line.'  # \n 表示换行符
>>> s  # 不用 print()，特殊字符将包括在字符串中
'First line.\nSecond line.'
>>> print(s)  # 用 print()，特殊字符会被转写，因此 \n 将产生一个新行
First line.
Second line.
```

如果不希望前置 `\` 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 `r` 即可：
```python
>>> print('C:\some\name')  # 这里 \n 表示换行符！
C:\some
ame
>>> print(r'C:\some\name')  # 请注意引号前的 r
C:\some\name
```

字符串字面值可以跨越多行。 一种做法是使用三重引号: `"""..."""` 或 `'''...'''`。 行结束符会自动包括在字符串中，
但可以通过在行尾添加 `\` 来避免此行为。 在下面的例子中，开头的换行符将不会被包括:
```python
>>> print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>>
```

字符串可以用 `*` 重复：
```python
>>> 3 * 'abc'
'abcabcabc'
```

相邻的两个或多个字符串字面值（引号标注的字符）会自动合并：
```python
>>> 'Py' 'thon'
'Python'
```

这项功能只能用于两个字面值，不能用于变量或表达式：
```python
>>> prefix = 'Py'
>>> prefix 'thon'  # 不能拼接变量和字符串字面值
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

合并多个变量，或合并变量与字面值，要用 +：
```python
>>> prefix + 'thon'
'Python'
```

字符串支持 索引 （下标访问），第一个字符的索引是 0。索引还支持负数，用负数索引时，从右边开始计数：
```python
>>> word = 'Python'
word[-1]  # 最后一个字符
'n'
>>> word[-2]  # 倒数第二个字符
'o'
>>> word[-6]
'P'
```

注意，-0 和 0 一样，因此，负数索引从 -1 开始。

除了索引操作，还支持*切片*。 索引用来获取单个字符，而切片允许你获取子字符串:
```python
>>> word[0:2]  # 从 0 号位 (含) 到 2 号位 (不含) 的字符
'Py'
>>> word[2:5]  # 从 2 号位 (含) 到 5 号位 (不含) 的字符
'tho'
```

切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾：
```python
>>> word[:2]   # 从开头到 2 号位 (不含) 的字符
'Py'
>>> word[4:]   # 从 4 号位 (含) 到末尾
'on'
>>> word[-2:]  # 从倒数第二个 (含) 到末尾
'on'
```

注意，输出结果包含切片开始，但不包含切片结束。因此，`s[:i] + s[i:]` 总是等于 `s`：
```python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```

还可以这样理解切片，索引指向的是字符之间 ，第一个字符的左侧标为 0，最后一个字符的右侧标为 n ，
n 是字符串长度。例如：
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

第一行数字是字符串中索引 0...6 的位置，第二行数字是对应的负数索引位置。i 到 j 的切片由 i 和 j 
之间所有对应的字符组成。

Python 字符串不能修改，是 **immutable** 的。因此，为字符串中某个索引位置赋值会报错：
```python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

要生成不同的字符串，应新建一个字符串.

### 3.1.3 列表

与 immutable 字符串不同, 列表是 mutable 类型，其内容可以改变：
```python
>>> cubes = [1, 8, 27, 65, 125]  # 这里有点问题
>>> 4 ** 3  # 4 的立方是 64，不是 65！
64
>>> cubes[3] = 64  # 替换错误的值
>>> cubes
[1, 8, 27, 64, 125]
```

Python 中的简单赋值绝不会复制数据。 当你将一个列表赋值给一个变量时，该变量将引用*现有的列表*。
你通过一个变量对列表所做的任何更改都会被引用它的所有其他变量看到。
```python
>>> rgb = ["Red", "Green", "Blue"]
>>> rgba = rgb
>>> id(rgb) == id(rgba)  # 它们指向同一个对象
True
>>> rgba.append("Alpha")
>>> rgb
["Red", "Green", "Blue", "Alpha"]
```

列表支持嵌套(创建包含其他列表的列表):
```python
>>> a = ['a', 'b', 'c']
>>> b = [1, 2, 3]
>>> x = [a, b]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```

# 4 更多控制流工具

## 4.6 pass 语句

`pass` 语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句。例如：
```python
>>> while True:
        pass  # 无限等待键盘中断 (Ctrl+C)
```

这常用于创建一个最小的类：
```python
>>> class MyEmptyClass:
        pass
```

pass 还可用作函数或条件语句体的占位符，让你保持在更抽象的层次进行思考。pass 会被默默地忽略：
```python
>>> def initlog(*args):
        pass   # 记得实现这个！
```

对于这后一种情况，许多人会使用省略符字面值 ... 而不是 pass。 这种用法在 Python 中没有特殊含义，
也不是语言定义的一部分（这里你可以使用任意常量表达式），但 ... 在传统上也被用作占位符号。

## 4.7 match 语句

`match` 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。这表面上像 C、Java 
或 JavaScript（以及许多其他程序设计语言）中的 switch 语句，但其实它更像 Rust 或 Haskell 中的模式匹配。
只有第一个匹配的模式会被执行，并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量。
如果没有匹配的 case，则不执行任何分支。

最简单的形式是将一个主语值与一个或多个字面值进行比较：
```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

注意最后一个代码块：变量名 `_` 被作为 通配符 并必定会匹配成功。

你可以用 `|` (或)将多个字面值组合到一个模式中：
```python
case 401 | 403 | 404:
    return "Not allowed"
```

> *match* 语句还有很多高级用法, 目前这里先省略.


## 4.9 函数定义详解

### 4.9.2 关键字参数

当存在形式为 `**name` 最后一个形参时，它将接受一个字典 (见 映射类型 --- dict)，其中包含与正式形参
对应的参数以外的所有关键字参数。 它可以与接受包含正式形参列表以外的位置参数的 tuple 的 `*name` 形式的
正式形参组合使用。 (`*name` 必须出现在 `**name` 之前。) 例如，如果我们定义一个这样的函数:
```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

该函数可以用如下方式调用：
```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

输出结果如下：
```
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

注意，关键字参数在输出结果中的顺序与调用函数时的顺序一致。

### 4.9.3 特殊参数

默认情况下，参数可以按位置或显式关键字传递给 Python 函数。为了让代码易读、高效，最好限制参数的传递方式，
这样，开发者只需查看函数定义，即可确定参数项是仅按位置、按位置或关键字，还是仅按关键字传递。

函数定义如下：
```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        位置或关键字              |
        |                                - 仅限关键字
         -- 仅限位置
```

`/` 和 `*` 是可选的。这些符号表明形参如何把参数值传递给函数：位置、位置或关键字、关键字。
关键字形参也叫作命名形参。

函数定义中未使用 `/` 和 `*` 时，参数可以按位置或关键字传递给函数。

### 4.9.5 解包实参列表

函数调用要求独立的位置参数，但实参在列表或元组里时，要执行相反的操作。例如，内置的 `range()` 函数
要求独立的 start 和 stop 实参。如果这些参数不是独立的，则要在调用函数时，用 `*` 操作符把实参从列表
或元组解包出来：
```python
>>> list(range(3, 6))            # 附带两个参数的正常调用
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # 附带从一个列表解包的参数的调用
[3, 4, 5]
```

同样，字典可以用 `**` 操作符传递关键字参数：
```python
>>> def parrot(voltage, state='a stiff', action='voom'):
        print("-- This parrot wouldn't", action, end=' ')
        print("if you put", voltage, "volts through it.", end=' ')
        print("E's", state, "!")

>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

### 4.9.7 文档字符串

以下是文档字符串内容和格式的约定。

第一行应为对象用途的简短摘要。为保持简洁，不要在这里显式说明对象名或类型，因为可通过其他方式获取这些信息
（除非该名称碰巧是描述函数操作的动词）。这一行应以大写字母开头，以句点结尾。

文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开。后面的行可包含若干段落，描述对象的
调用约定、副作用等。

对于被用作模块、类或函数文档字符串的多行字符串字面值 Python 解析器会去除其中的缩进。

下面是多行文档字符串的一个例子：
```python
>>> def my_function():
        """Do nothing, but document it.

        No, really, it doesn't do anything:

            >>> my_function()
            >>>
        """
        pass

>>> print(my_function.__doc__)
Do nothing, but document it.

No, really, it doesn't do anything:

    >>> my_function()
    >>>
```

### 4.9.8 函数注解

函数注解是可选的用户自定义函数类型的元数据完整信息（详见 PEP 3107 和 PEP 484 ）。

标注是以字典形式存放在函数的 `__annotations__` 属性中的而对函数的其他部分没有影响。 形参标注的定义方式
是在形参名后加冒号，后面再跟一个将被求值为标注的值的表达式。 返回值标注的定义方式是加符号 `->`，
后面再跟一个表达式，它位于形参列表和表示 `def` 语句结束的冒号之间。 下面的示例具有加了标注的一个必需参数、
一个可选参数以及返回值:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
        print("Annotations:", f.__annotations__)
        print("Arguments:", ham, eggs)
        return ham + ' and ' + eggs

>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

## 4.10 小插曲: 编码风格

现在你即将编写更长、更复杂的 Python 代码段，是时候讨论一下代码风格了。 大多数语言都能被书写为
（或更准确地说，是被格式化为）不同的风格；有些风格相比其他风格可读性更好。 能让别人轻松阅读你的代码
总是一个好主意，而采用一种良好的代码风格对此会很有帮助。

Python 项目大多都遵循 PEP 8 的风格指南；它推行的编码风格易于阅读、赏心悦目。Python 开发者均应
抽时间悉心研读；以下是该提案中的核心要点：

- 缩进，用 `4` 个空格，不要用制表符。    
  4 个空格是小缩进（更深嵌套）和大缩进（更易阅读）之间的折中方案。制表符会引起混乱，最好别用。
- 换行，一行不超过 `79` 个字符。    
  这样换行的小屏阅读体验更好，还便于在大屏显示器上并排阅读多个代码文件。
- 用空行分隔函数和类，及函数内较大的代码块。
- 最好把注释放到单独一行。
- 使用文档字符串。
- 运算符前后、逗号后要用空格，但不要直接在括号内使用： `a = f(1, 2) + g(3, 4)`。
- 类和函数的命名要一致；按惯例，命名类用 `UpperCamelCase`，命名函数与方法用 `lowercase_with_underscores`。
  命名方法中第一个参数总是用 `self` (类和方法详见 初探类)。
- 编写用于国际多语环境的代码时，不要用生僻的编码。Python 默认的 UTF-8 或纯 ASCII 可以胜任各种情况。
- 同理，就算多语阅读、维护代码的可能再小，也不要在标识符中使用非 ASCII 字符。


# 5 数据结构

## 5.1 列表详解

列表即 `list`.

### 5.1.2 用列表实现队列

列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；然而，列表作为队列的效率很低。
因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）。

实现队列最好用 `collections.deque`，可以快速从两端添加或删除元素。

## 5.2 del 语句

可以按索引而不是按值从一个列表移除条目：即使用 `del` 语句。 这不同于返回一个值的 `pop()` 方法。 
del 语句还可被用来从列表移除切片或清空整个列表（之前我们通过将一个空列表赋值给切片实现此功能）。 例如:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

del 也可以用来删除整个变量：
```python
>>> del a
```

此后，再引用 `a` 就会报错（直到为它赋与另一个值）。

## 5.3 元组和序列

列表和字符串有很多共性，例如，索引和切片操作。 这两种数据类型是序列(`Sequence`)。 随着 Python 语言的发展，
其他的序列类型也被加入其中, 如元组(`tuple`).

元组由多个用逗号隔开的值组成，例如：
```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

输出时，元组都要由`圆括号`标注，这样才能正确地解释嵌套元组。输入时，圆括号可有可无，不过经常是必须的
（如果元组是更大的表达式的一部分）。不允许为元组中的单个元素赋值，当然，可以创建含列表等可变对象的元组。

## 5.6 循环的技巧

当对字典执行循环时，可以使用 `items()` 方法同时提取键及其对应的值。
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
        print(k, v)

gallahad the pure
robin the brave
```

在序列中循环时，用 `enumerate()` 函数可以同时取出位置索引和对应的值：
```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
      print(i, v)

0 tic
1 tac
2 toe
```

同时循环两个或多个序列时，用 `zip()` 函数可以将其内的元素一一匹配：
```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))

What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```


# 6 模块

## 6.1 模块详解

### 6.1.3 "已编译的" Python 文件

为了快速加载模块，Python 把模块的编译版本缓存在 `__pycache__` 目录中，文件名为 `module.version.pyc`，
version 对编译文件格式进行编码，一般是 Python 的版本号。

Python 对比编译版与源码的修改日期，查看编译版是否已过期，是否要重新编译。此进程完全是自动的。此外，
编译模块与平台无关，因此，可在不同架构的系统之间共享相同的库。

Python 在两种情况下不检查缓存:
- 一，从命令行直接载入的模块，每次都会重新编译，且不储存编译结果；
- 二，没有源模块，就不会检查缓存。为了让一个库能以隐藏源代码的形式分发（通过将所有源代码变为编译后的版本），
编译后的模块必须放在源目录而非缓存目录中，并且源目录绝不能包含同名的未编译的源模块。

给专业人士的一些小建议：

- 在 Python 命令中使用 `-O` 或 `-OO` 开关，可以减小编译模块的大小。`-O` 去除断言语句，
`-OO` 去除断言语句和 `__doc__` 字符串。有些程序可能依赖于这些内容，因此，没有十足的把握，
不要使用这两个选项。“优化过的”模块带有 `opt-` 标签，并且文件通常会一小些。将来的发行版或许会改进优化的效果。
- 从 `.pyc` 文件读取的程序不比从 `.py` 读取的执行速度快，`.pyc` 文件只是加载速度更快。
- `compileall` 模块可以为一个目录下的所有模块创建 .pyc 文件。
- 本过程的细节及决策流程图，详见 [PEP 3147](https://peps.python.org/pep-3147/)。

## 6.4 包

包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 `A.B` 表示名为 A 的包中
名为 B 的子模块。 就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点号模块名也可以
让 NumPy 或 Pillow 等多模块包的作者也不必担心彼此的模块名冲突。

假设要为统一处理声音文件与声音数据设计一个模块集（“包”）。声音文件的格式很多（通常以扩展名来识别，
例如：.wav，.aiff，.au），因此，为了不同文件格式之间的转换，需要创建和维护一个不断增长的模块集合。
为了实现对声音数据的不同处理（例如，混声、添加回声、均衡器功能、创造人工立体声效果），
还要编写无穷无尽的模块流。下面这个分级文件树展示了这个包的架构：

```
sound/                          最高层级的包
      __init__.py               初始化 sound 包
      formats/                  用于文件格式转换的子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  用于音效的子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  用于过滤器的子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

导入包时，Python 搜索 `sys.path` 里的目录，查找包的子目录。

需要有 `__init__.py` 文件才能让 Python 将包含该文件的目录当作包来处理（除非使用 `namespace package`，
这是一个相对高级的特性）。 这可以防止重名的目录如 string 在无意中屏蔽后继出现在模块搜索路径中的有效模块。 
在最简单的情况下，`__init__.py` 可以只是一个空文件，但它也可以执行包的初始化代码或设置 `__all__` 变量，
这将在稍后详细描述。

还可以从包中导入单个模块，例如：
`import sound.effects.echo`

这将加载子模块 `sound.effects.echo`。 它必须通过其全名来引用:
`sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)`

另一种导入子模块的方法是 ：
`from sound.effects import echo`

这也会加载子模块 echo，并使其不必加包前缀，因此可按如下方式使用:
`echo.echofilter(input, output, delay=0.7, atten=4)`

Import 语句的另一种变体是直接导入所需的函数或变量：
`from sound.effects.echo import echofilter`

同样，这将加载子模块 echo，但这使其函数 echofilter() 直接可用:
`echofilter(input, output, delay=0.7, atten=4)`

注意，使用 `from package import item` 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、
类或变量等其他名称。`import` 语句首先测试包中是否定义了 item；如果未在包中定义，则假定 item 是模块，
并尝试加载。如果找不到 item，则触发 `ImportError` 异常。

相反，使用 `import item.subitem.subsubitem` 句法时，除最后一项外，每个 item 都必须是包；
最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。


# 7 输入与输出

## 7.1 更复杂的输出格式

格式化输出包括以下几种方法:

- 使用格式化字符串字面值

  需要在字符串开头的引号/三引号前添加 `f` 或 `F`. 在这种字符串中，可以在 `{` 和 `}` 
  字符之间输入引用的变量，或字面值的 Python 表达式。

  ```python
  >>> year = 2016
  >>> event = 'Referendum'
  >>> f'Results of the {year} {event}'
  'Results of the 2016 Referendum'
  ```

- 使用 `str.format()`

  你仍将使用 `{` 和 `}` 来标记变量将被替换的位置并且可以提供详细的格式化指令，
  但你还需要提供待格式化的信息.

  ```python
  >>> yes_votes = 42_572_654
  >>> total_votes = 85_705_149
  >>> percentage = yes_votes / total_votes
  >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
  ' 42572654 YES votes  49.67%'
  ```

  请注意 yes_votes 填充了空格并且只为负数添加了负号。 这个例子还打印了 percentage 乘以 100 
  的结果，保留 2 个数位并带有一个百分号 (请参阅 [格式规格迷你语言](https://docs.python.org/zh-cn/3.12/library/string.html#formatspec) 了解详情)。

- 最后，还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。
  字符串类型还支持将字符串按给定列宽进行填充，这些方法也很有用。

如果不需要花哨的输出，只想快速显示变量进行调试，可以用 `repr()` 或 `str()` 函数把值转化为字符串。

`str()` 函数返回供人阅读的值，`repr()` 则生成适于解释器读取的值（如果没有等效的语法，则强制执行 
SyntaxError）。对于没有支持供人阅读展示结果的对象， `str()` 返回与 `repr()` 相同的值。一般情况下，数字、
列表或字典等结构的值，使用这两个函数输出的表现形式是一样的。字符串有两种不同的表现形式。

### 7.1.1 格式化字符串字面值

格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 `f` 或 `F`，通过 `{expression}` 表达式，
把 Python 表达式的值添加到字符串内。

格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。下例将 pi 舍入到小数点后三位：
```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

在 `:` 后传递整数，为该字段设置最小字符宽度，常用于列对齐：
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')

Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

还有一些修饰符可以在格式化前转换值。 `!a` 应用 ascii() ，`!s` 应用 str()，`!r` 应用 repr()：
```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

`=` 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
```python
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

请参阅 [自说明型表达式](https://docs.python.org/zh-cn/3.12/whatsnew/3.8.html#bpo-36817-whatsnew) 
以了解 `=` 说明符的更多信息。 有关这些格式说明的详情，请查看针对 
[格式规格迷你语言](https://docs.python.org/zh-cn/3.12/library/string.html#formatspec) 的参考指南。

### 7.1.2 字符串 format() 方法

`str.format()` 方法的基本用法如下所示：
```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

花括号及之内的字符（称为格式字段）被替换为传递给 `str.format()` 方法的对象。花括号中的数字表示传递给 
`str.format()` 方法的对象所在的位置。

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

`str.format()` 方法中使用关键字参数名引用值。
```python
>>> print('This {food} is {adjective}.'.format(
        food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

位置参数和关键字参数可以任意组合：
```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```

如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传递字典，
并用方括号 `[]` 访问键来完成。
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
          'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

这也可以通过将 table 字典作为采用 `**` 标记的关键字参数传入来实现。
```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

与内置函数 `vars()` 一同使用时这种方式非常实用，它将返回一个包含所有局部变量的字典:
```python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: ...
```

举个例子，以下几行代码将产生一组整齐的数据列，包含给定的整数及其平方与立方:
```python
>>> for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

str.format() 进行字符串格式化的完整概述详见 [格式字符串语法](https://docs.python.org/zh-cn/3.12/library/string.html#formatstrings) 。

## 7.2 读写文件

### 7.2.2 使用 json 保存结构化数据

Python 允许你使用流行的数据交换格式 JSON，而不是让用户持续编写和调试代码来将复杂的数据类型存入文件中。 
标准库模块 `json` 可以接受带有层级结构的 Python 数据，并将其转换为字符串表示形式；这个过程称为 serializing。
根据字符串表示形式重建数据则称为 deserializing。 在序列化和反序列化之间，用于代表对象的字符串可以存储在
文件或数据库中，或者通过网络连接发送到远端主机。

备注 JSON 格式通常用于现代应用程序的数据交换。程序员早已对它耳熟能详，可谓是交互操作的不二之选。
只需一行简单的代码即可查看某个对象的 JSON 字符串表现形式：
```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

`dumps()` 函数还有一个变体， `dump()`，它只将对象序列化为 text file 。因此，如果 f 是 text file 对象，
可以这样做：
```python
json.dump(x, f)
```

要再次解码对象，如果 f 是已打开、供读取的 binary file 或 text file 对象：
```python
x = json.load(f)
```

这种简单的序列化技术可以处理列表和字典，但在 JSON 中序列化任意类的实例，则需要付出额外努力。
json 模块的参考包含对此的解释。


# 8 错误和异常


# 9 类


# 10 标准库简介


# 11 标准库简介2


# 12 虚拟环境和包





























