
#python查找一个变量时会按照“局部作用域”，嵌套作用域，全局作用域和内置作用域查找

#以下代码无法修改a的值
def foo():
    a=200
    print(a)

if __name__=="__main__":
    a=100;
    foo()
    print(a)
#将a定义为全局变量

