
#文件的操作模式：读取“r”，写入“w”，写入（如果文件已经存在会产生异常）：“x”，追加”a“
#二进制模式”b“，文本模式”t“，更新（既可以读又可以写）”+“

def main():
    f=open(r"F:\pythonfile\test1.txt","r",encoding="utf-8")
    print(f.read())
    f.close()


if __name__=="__main__":
    main()