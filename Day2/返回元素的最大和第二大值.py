

#返回传入的列表的最大和第二大值

def main(list1):
    list1.sort(reverse=True);
    return(list1[0],list1[1])

if __name__=="__main__":
    list1=[3,6,8,2,5,9,12,78]
    print(main(list1))