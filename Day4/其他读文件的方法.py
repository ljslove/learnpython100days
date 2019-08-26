
#使用readline或者readlines来读写文件

def main():
    try:
        #一次性读取整个文件
        with open(r"F:\pythonfile\test1.txt","r",encoding="utf-8") as f:
            print("一次性去读文件")
            print(f.read())
        #一次读取一行
        with open(r"F:\pythonfile\test1.txt","r",encoding="utf-8") as f:
            for line in f:
                print(line,end="???")
        #一次性将文件读取到列表中
        with open(r"F:\pythonfile\test1.txt","r",encoding="utf-8") as f:
            print(f.readlines())
    except FileNotFoundError:
        print("文件不存在")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("解码错误")

if __name__=="__main__":
    main()