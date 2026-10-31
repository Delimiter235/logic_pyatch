## 要点
1. The trap: 我的直觉认为 python 原生函数`sort`先看长度，实际上它只看 ASCII 。`'flow'` < `'flower'` 是因为空字符 < 有字符；
2. The Trick: 纵向扫描的本质是双层循环。外层`i`是列（字符位置），内层循环`j`是行（字符串索引）,可视化如下：
```
  0 1 2 3 4 5 i
0 f l o w e r base_str
1 f l o w     current_str1
2 f l i g h t current_str2
```
3. The code: 最关键的一行是两个用于判断“前缀断了”的条件，即先判断`current_str`长度防止越界，再检测`i`是否一致，判别式如下：
```
if len(current_str) == i or current_str[i] != char_to_check:
```
## 其他
`.python_history`相关测试指令如下：
```
$ python
>>> str = "hello"
>>> len(str)
5
>>> for i in range(5): print(i)
... 
0
1
2
3
4
>>> for i in range(1, 4): print(i)
... 
1
2
3
>>> for i in range(0, 4): print(i)
... 
0
1
2
3
>>> str = ""
>>> print(str)

>>> str = 's'
>>> print(str)
s
>>> str = ''
>>> len(str)
0
>>> for i in range(len(str)): print(i)
... 
>>> print(str[0])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    print(str[0])
          ~~~^^^
IndexError: string index out of range
>>> str = 'sdfd'
>>> print(str[:3])
sdf
>>> print(len(str[:3]))
3
>>> print(len(str))
4
```