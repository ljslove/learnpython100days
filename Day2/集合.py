#集合的基本用法
#集合的元素可以改变，但是集合不能有重复的元素

#创建一个集合
set1={1,3,4,4,2,3,1}
print(set1)
#将字符串转换为集合
str1="tyutuyioo"
print(set(str1))
#将列表转换为集合
list1=["2233","2233","ioo"]
print(set(list1))
#添加元素
set1.add("ioioo")
print(set1)
#使用update来添加元素
set1.update("iiui")
print(set1)
set1.update([222,8989])
print(set1)
set1.update({"65":"oioo"})
print(set1)
#删除元素
set1.pop()
print(set1)

