
#返回指定文件的后缀

def main(name):
    list1=name.split(".")
    return list1[-1]

if __name__=="__main__":
    print(main("test.tets.docx"))
