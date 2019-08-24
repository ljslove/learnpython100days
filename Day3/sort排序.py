#一个对象由两个属相，可以先根据一个属性排序，再根据另一个属性再次排序
#对象如果不重写__str__方法，打印出的对象是内存的地址

class Card(object):
    def __init__(self,suite,face):
        self._suite=suite
        self._face=face
    @property
    def suite(self):
        return self._suite
    @property
    def face(self):
        return self._face
    def __str__(self):
        return '%s%s'%(self._suite,self._face)
    def __repr__(self):
        return self.__str__()

list1=[Card('红',1),Card('红',3),Card('梅',4),Card('方',5),Card('梅',5)]

print(list1)
def get_key(card):

    return(card.suite,card.face)

list1.sort(key=get_key)

print(list1)

def get_key2(card):
    return card.face

list1.sort(key=get_key2)
print(list1)