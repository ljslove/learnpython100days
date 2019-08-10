
#生成指定的验证码，验证码由大小写字母和数字组成
import random
def main(num):
    code="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #result=[]
    code1=''
    for i in range(0,num):
        index=random.randint(0,62)
        #result.append(code[index])
        code1=code1+code[index]

    return code1


if __name__=="__main__":
    print(main(4))




