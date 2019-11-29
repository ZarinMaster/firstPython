"""
do some class example
Author:luohao
Author:ZarinMaster

"""


class Person(object):

    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 访问器 - getter方法
    @property
    def sex(self):
        return self._sex

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s是%s的，正在玩飞行棋.' % (self._name, self._sex))
        else:
            print('%s是%s的，正在玩斗地主.' % (self._name, self._sex))


def main():
    myperson = Person('王大锤', 12, '男')
    myperson.play()
    a = myperson.name
    print(a)
    myperson.age = 22
    myperson.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
