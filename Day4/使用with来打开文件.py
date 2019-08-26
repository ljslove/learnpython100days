
#通过使用with来打开文件，可以指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源

def main():
    try:
        with open(r"F:\pythonfile\test1.txt","r",encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("找不到文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("解码错误")

if __name__=="__main__":
    main()
