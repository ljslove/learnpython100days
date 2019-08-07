
#什么是素数：除了1和它自身外，不能整除其他整数

def prime(num):
    tag=False
    for i in range(2,num):
        if(num%i==0):
            tag=True
    return tag

print(prime(1))
