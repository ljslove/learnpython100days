
#字典是键值对

#定义一个字典
dict1={"name":"li","age":13,"address":"test"}
print(dict1)
#添加一个元素
dict1['shcool']="test2"
dict1[455]=9099
print(dict1)
#更新值
dict1["school"]="testest1"
print(dict1)
#通过键来获取值
print(dict1.get("school"))
#遍历字典的值
for i in dict1.values():
    print(i)
#遍历字典的键
for j in dict1.keys():
    print(j)
#遍历字典的键值对
for i,j in dict1.items():
    print(i,j)
#删除字典中的元素
dict1.popitem();
print(dict1)
#删除指定的元素
dict1.pop("address")
print(dict1)
#清空字典
dict1.clear()
print(dict1)