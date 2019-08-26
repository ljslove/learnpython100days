

#读写文件时会遇到各种异常情况，如文件不存在等，使用try except来处理异常

def main():
    try:
        f=open(r"F:\pythonfile\test2.txt","r",encoding="utf-8")
        print(f.read())
    except FileNotFoundError:
        print("文件不存在")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")
    finally:
        f.close()

if __name__=="__main__":
    main()
