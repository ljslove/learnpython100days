

#判断一个数是不是素数

def is_prime(num):
    flag=True
    for temp in range(2,num):
        if num%temp==0:
            flag=False
    return  flag


def main():
    try:
            for i in range(1,10000):
                if i>=1 and i<=99:
                    with open(r"F:\pythonfile\a.txt","a",encoding="utf-8") as f1:
                     if is_prime(i):
                        f1.write(str(i))
                        f1.write(" ")
                elif i>=100 and i<=999:
                    with open(r"F:\pythonfile\b.txt","a",encoding="utf-8") as f2:
                     if is_prime(i):
                        f2.write(str(i))
                        f2.write(" ")

                elif i>=1000 and i<=9999:
                    with open(r"F:\pythonfile\c.txt","a",encoding="utf-8") as f3:
                     if is_prime(i):
                        f3.write(str(i))
                        f3.write(" ")
    except Exception as e:
        print(e.args)


if __name__=="__main__":
    main()
