
#函数的可变参数 *args，**kwargs
#*args，从此处开始到结束的所有参数组成一个tuple
#**kwargs从此处开始到结束的所有参数组成一个dict

def test(*args):
    print(type(args))
    print(args)

test(1,3,45)
test("iirt","oioor")
test("utit")
test([23,355,345])
test([455,666],[455,56])

def test1(**kwargs):
    print(type(kwargs))
    print(kwargs)

test1(name="lijingsan",age=44,test=89)