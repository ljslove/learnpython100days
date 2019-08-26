

#使用二进制的读写，可以复制图片

def main():

    with open(r"F:\pythonfile\test1.jpg","rb") as f:
        data=f.read()
    with open(r"F:\pythonfile\test2.jpg","wb") as f:
        f.write(data)




if __name__=="__main__":
    main()