##### 1. 打印与注释
```python
print("hello world")
print('hello')
print('i "said"do not touch this')
#print('i live this type')
```
*注意：#在python中用作注释*
##### 2. 数字与数字计算 
*主要*：+，-，/（除），*，%*(取余)，<,>,<=,>=
```python
print(5+3) 
#输出：8
print(25+30/6)
#输出：30.0
print(5%3)
#输出：2
print(3+2<6-9)
#输出：false
```
##### 3.字符串运算
```python
print("well water"+"river")
#输出结果：well waterriver
```
1.
```python
print("i ove you"*8)
#输出结果：i love youi love youi love youi love youi love youi love youi love youi love you
 
print("i love you\n"*8) 
#输出结果是:i love you
#i love you
#i love you
#i love you
#i love you
#i love you
#i love you
#i love you 
```
2.
```python
print("i love you\n"+8) 
#结果：TypeError: must be str, not int 
```
*注意：int不能与字符串相加*

#### 1.变量
**print("there are",car_number,"cars available.")(第一种打印变量的方法，car_number是变量)**
```python
car_number=100
 
#python中命名变量时不能使用空格如下
#错误用法：
#car numbner=100
 
a_car_space=4.0
#4.0是浮点数
drivers=30
passenger=90
car_down=car_number - drivers
#操作符两边尽量打空格，方便阅读
carpool_number=drivers*a_car_space
 
print("there are",car_number,"cars available.")
#打印不同字符串用“，”隔开
print("ther are",car_down,"cars do not have driver")
print("wow",carpool_number,"wow")
```
**需要注意：** 
- “_”的使用，如car_number=100，不能用car number=100
- a_car_space=4.0，4.0是浮点数
- =代表赋值，==代表是否相等（结果为：ture或者false）
#### 2. 格式化字符串（在字符串中插入变量）
**print(f"let's talk about {my_name}.")（第二种打印变量的方法，my_name是变量）**
```python
my_name = 'woow' 
my_age = 99
#不能用  99 = my_age
#99不是有效的变量名称，变量名要以字母开头
my_height = 176
my_weight = round(148.4)
#round(148.4) 可以让将浮点数四舍五入
my_eye = 'black'
my_teeth="white"
 
print(f"let's talk about {my_name}.")
print(f'he is{my_age} years old and {my_height} mm,he has {my_eye} eyes and {my_teeth} teeth.')
print(f"he is {my_weight} pounds heavy.")
#格式化字符串要以f开头 
```
- 注意：
- 99不是有效的变量名称，变量名要以字母开头 
- 格式化字符串要以f开头
#### 3.字符串简化（第三种打印变量的方法）
```python
t_p = 10
x = f"there are {t_p} type of people."
apex = False
bodyy = True
y = f"those who know it is {boddy} or {apex}"
print(x + y)
```
**注意：format使用方法** 
- 基本使用格式是：
     <模板字符串>.format(<逗号分隔的参数>)
```
print("{}：计算机{}的CPU 占用率为{}%。".format("2016-12-31","PYTHON",10))
Out[10]: '2016-12-31：计算机PYTHON的CPU 占用率为10%。'
```
- format()方法可以非常方便地连接不同类型的变量或内容，如果需要输出大括号，采用{{表示{，}}表示} 
**print("{}{}{}".format("圆周率是",3.1415926,"..."))
(第四种打印变量的方法)**
```
print("{}{}{}".format("圆周率是",3.1415926,"..."))
Out[11]: '圆周率是3.1415926...'
```
##### 4.字符串转义（两种方法）
- 使用\n将字符串扩展到多行（\可以将难录入的字符放到字符串中）
```python
print("i am 6'2\" tall.")
print('i am 6\'2" tall.')
#i am 6'2" tall.
#i am 6'2" tall.
#其中 \" 代表 " 的意思(详见转义序列表 python2.2)
```
- 使用“三引号”**（第四种打印变量的方法，my_name是变量）**
```python
print("""
i'll do a list:
food
water
fish
grass
""")
#三引号之间可以任意放入多行文本
```


#### 1. 输入提示（两种输入方式） -input
- 直接print
```python
print("how old are you?",end=' ')
age = input()
#input默认输入的是字符串
#如果是要用来计算的数字，则需要写成
#age = int(input())或者再加一个变量age_int = int(age)
print("you are {} years old.".format(age))
#end=' '是告诉print不要用换行符结束这一行
```
- 在input（）的（）中加入提示
```
age = input("how old are you?")
print("you are {} years old.".format(age))
```
#### 2.输入模块 -argv
```python
from sys import argv
script,first,second,third = argv
 
print("the script is called:",script)
print("you",first)
print("your second",second)
print("ssss",third)
 
#出现argv需要在cmd控制台里运行文件
#运行时出现文件夹必须保存在 C:\Users\euphonium>
#键入：(base) C:\Users\euphonium>python untitled1.py 1st 2nd 3ir
 
#输出：the script is called: untitled1.py
#you 1st
#your second 2nd
#ssss 3ir
 
#用spyder直接运行的结果会报错
#如下：
# File "C:/Users/euphonium/untitled1.py", line 8, in <module>
#   script,first,second,third = argv
#
#ValueError: not enough values to unpack (expected 4, got 1)
```
**注意：argv是在用户执行命令是就输入，而input是在运行脚本是输入**
```python
from sys import argv
script,use_name = argv
prompt = '>'
 
print(f"hi {use_name},i am the {script} script.")
likes = input(prompt)
lives = input(prompt)
computer = input(prompt)
print(f"""
{likes}{lives}{computer}
""")
#不加f是不能与格式化工具一起使用的
```

#### 1.读取文件(两种方式)
-1st
```python
from sys import argv
script, filename = argv
txt = open(filename)
#上面的是关键，用open来打开文件，用read（）来读取
 
print(f"here's your life{filename}:")
print(txt.read())
#read 后面有个括号
```
-2nd
```
print("输入文件名:")
file_again = input(">")
txt_again = open(file_again)
#同样处理完文件后需要close()来关闭
print(txt_again.read())
```
#### 2.读写文件
文件命令：txt.read()
**close**：关闭文件 
**read**：读取文件内容 
**readline**：只读取文本文件中的一行 
**truncate**；清空文件，be careful 
**write('stuff')**:将“stuff”写入文件 
**seek(0)**:将读写位置移动到文件开头
```python
from sys import argv
script, filename = argv
 
print(f"come on ,wo are going to edite {filename}.")
print("go")
 
print("input someting you want")
input('>')
 
print("opening the file....")
txt = open(filename,'w')
#这里的'w'是一个字符的特殊字符串，用来表示文件的访问模式
#可以用+修饰表示多种模式，读写等
#'w'是写入模式，write
#'r'是读取模式，read
#'a'是追加模式，append
print("cleaner is working....")
txt.truncate()
print("let write this text!")
l1 = input("first line:")
l2 = input("second line:")
l3 = input("third line:")
 
txt.write("{}\n{}\n{}".format(l1,l2,l3))
#txt.write(l1)
#txt.write("\n")
#txt.write(l2)
#txt.write("\n")
#txt.write(l3)
#txt.write("\n")
#和上面有相同的作用
 
print(f"{filename} is going to close ")
txt.close()
```
- 文件复制
```python
from sys import argv
from os.path import exists
 
script,from_file,to_file = argv
print(f"copy from{from_file} to {to_file}")
 
in_txt = open(from_file)
indata = in_txt.read()
 
print(f"{len(indata)}B long")
print(f"true to {exists(to_file)}")
print("go")
input('>')
 
out_txt = open(to_file,'w')
out_txt.write(indata)
 
print("well done")
out_txt.close()
in_txt.close()
```
