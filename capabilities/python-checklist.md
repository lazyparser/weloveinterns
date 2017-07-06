TODO

# Python 学习

## Python数据类型

与大多数语言一样，python也支持常见的数据类型，整数，浮点数，字符串，布尔类型

以及空值等类型的数据，另外还支持列表和字典，python还允许自定义数据类型。

**整数**

整数和浮点数与主流语言表示相同，对于整数，python支持利用十六进制表示，只需在

十六进制数字前面加上 0x 前缀，例如如下表示：0xff00, oxa5b4c3d2等

**浮点数**

python支持浮点数常规表示法和科学计数表示法，科学计数法表示如下：1.2e-5, 1.23e9

**字符串**

python支持字符串的两种记法，用双引号和单引号做标记，如："string"和'string'完全

等价，都表示字符串string, 如果字符串中含有引号，则分情况处理：

1. 字符串中只含有双引号或者只含有单引号，则可用与字符串中不同的引号来括起来字符串

例如： "I'm Robin", 'This is an "example" '

2. 字符串中既含有双引号，又含有单引号，可以用转义符来进行转义：

例如： 'I\'m an "example"', "I'm an \"example\" "

字符串续行：

如果字符串过长，需要将字符串连接到下一行继续书写，python提供字符串续行功能，如下：

"I'm so happy that you can come to my home and participate in my birthday party \

Thank you \
		 
so much"

多行字符串表示：

如果是一段文字，为书写格式美观，可以分行书写，python提供分行书写字符串的功能：

'''line1

line2

line3'''

注意每次书写一行时，提示符由>>>变成...，注意字符串的开头和结尾都是三个单引号.

**布尔值**

python中的布尔值有两个，True和False,这里需要注意大小写即可.布尔值可以用逻辑运算

and, or, not来进行运算.

**空值**

python中提供空值None，同样注意大小写，None不同于0，None是空值，而0是有意义的值.

**List和tuple**

list列表是有序集合，可添加和删除其中元素。定义如下：

		classmates = ['Robin','Vini','Bob']

访问列表元素：

		classmates[0]
		classmates[1]
		classmates[2]

**向list中添加和删除元素**

添加元素使用list中的append方法，删除使用pop方法，示例如下：

		classmates.append("Luc")	#追加元素到末尾
		classmates.append(i,"Luc")	#追加元素到下表为i的位置
		classmates.pop(i)			#删除下标为i的元素

tuple跟list类似，只是定义之后无法修改，其定义方式为:

		classmates = ('Robin','Vini','Bob')

需要注意的是，这里的无法修改是指在tuple层面无法修改，如果tuple中含有list，

那么list本身是可以修改的，举例如下：

		list1 = ['abc','123']
		classmates = ('Robin','Vini','Bob',list1)

上面classmates是一个tuple，但是其中的一个元素list1是一个list，我们可以随意修改

list1，这样也不会出现错误，相当于每个元素只是指向其值所在的空间，只要地址不变，

tuple就被认为是不变的。

## Python字典

python字典为dict，存储方式为key-value模式，与java中的map类似，定义方式如下：

		d = {'Robin':90,'Bob':89,'Vini':100}
		d['Bob']			#查看Bob对应的值

dict支持增加和删除操作，其方式如下：

		d['Luc'] = 98			#增加Luc和其对应的值
		d.pop('Bob')			#删除Bob和其对应的值

## Python循环

Python循环有for和while两种。下面说下用法：

for循环常用的是 for x in array，表示一次对于array中的每个元素，执行下面操作，

例如，打印classmates中的每个元素：

		for name in classmates:
			print(name)

另外，为了书写简便，python为for循环提供了一种特殊的记法，for i in range(n)，其中

n表示一个整数，range(n)表示从0到n-1的整数序列。

while循环与主流语言相同，示例如下：

		i=0
		sum=0
		while i<100:
			sum=sum+i
			i=i+1

## Python函数

Python函数定义方式与主流语言类似，示例如下：

		def add_two_ints(a,b):
			return a+b

上面定义了一个求两个数之和的函数，需要注意的有几点:

1. 定义函数时前面加def关键字
2. 函数的参数不需要向其它语言一样指明类型
3. 不要忘记后面的冒号
4. 缩进一定要正确，python对缩进十分敏感
5. 无需指明函数返回值类型

调用函数时直接调用函数名即可，例如上面的求和函数，调用方式如下：

		sum = add_two_ints(3,2)

## Python类

Python是一种面向对象的语言，我们可以定义自己的类，定义方式如下：

		class Example(parent_class):
			def __init__(self,name,score):
				self.name = name
				self.score = score

			def display_socre(self):
				print('%s: %s'%(self.name,self.score))

需要注意的是，定义类用class关键字，圆括号内指明所继承的父类，如果没有

可以不填或者填object类，因为所有的类都要继承object类。同样地，不要忘记

后面的冒号。定义__init__初始化函数时，init两边分别有两个下划线，一共四个

另外，init函数的第一个参数始终是self，类的属性不用预先定义，只需在初始化

函数__init__中用self调用即可。类中也可以自定义其它函数，定义方式与上面定

义函数大致相同，只是函数的第一个参数也是self，如果没有其它参数，则函数

只有一个self参数。


