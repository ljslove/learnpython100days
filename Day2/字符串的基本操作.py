
#字符串的基本操作，字符串的值不能更改

str1="hello word!"
#字符串的长度
print(len(str1))
#首字母大写
print(str1.capitalize()) #生成了新的字符串
#字符串全部大写
print(str1.upper())
#从字符串中查找子串所在的位置
print(str1.find("lo"))
print(str1.index("lo"))
#检查字符串是否以指定的字符串开头
print(str1.startswith("he"))
#检查字符串是否以指定的字符串结尾
print(str1.endswith("d!"))
#字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50,"*"))
#字符串以指定的宽度靠右侧放置并在左侧填充指定的字符
print(str1.ljust(50,"-"))
str2="abcd123456"
print(str2[3])
print(str2[1:5])
print(str2[1::2])
print(str2[-1:-5])
#检查字符串是否以数字构成
print(str2.isdigit())
#检查字符串是否以字母构成
print(str2.isalpha())
#检查字符串是否以数字和字母构成
print(str2.isalnum())
str3="   rutrijtio  "
#获取去掉字符串左右空格的拷贝,移除字符串头尾指定的字符
print(str3.strip())
#以i来分割字符串,分割成2+1个字符串，返回值是列表
print(str3.split("i",2))



