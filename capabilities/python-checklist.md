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

