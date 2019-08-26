
#覆盖以前的使用模式"w",追加”a“

def main():
    with open(r"F:\pythonfile\test2.txt","w",encoding="utf-8") as f:
        f.write("testlkgogko")
        f.write("jrkopkopkl")
        list1=["cjof","mcmlkjkl","piopiop"]
        f.writelines(list1)



if __name__=="__main__":
    main()