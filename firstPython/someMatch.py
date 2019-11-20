"""
do some math

Version: 0.1
Author: 骆昊
Author: ZarinMaster
"""
"""
sum=0
for x in range(2,100,2):
    sum+=x
print('偶数和为：%d'%sum)



def factiral(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m='))
n = int(input('n='))
print('结果为：%d' % (factiral(m) // factiral(n) // factiral(m - n)))

s1 = 'hello,' * 3
s2 = 'world'
s3 = s1 + s2
print('s1=%s\ns2=%s\ns3=%s\n' % (s1, s2, s3))



list1 = ['aa','bb','cc','dd']
list1.extend(['ee','ff','gg'])
list2 = list1[::-1]
list3 = sorted(list2)
list1.append('hh')

print('list1=%s'%list1)
print('list2=%s'%list2)
print('list3=%s'%list3)

f=[x for x in range(1,15)]
alpha='ABCDE'
num='123456'
f = [x + y for x in alpha for y in num]
print(f)
"""


# import os
# import time
#
#
# def main():
#     content = '北京欢迎你为你开天辟地..........'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()
#
# import random
#
#
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#
#     :param code_len: 验证码的长度(默认4个字符)
#
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     # all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # last_pos = len(all_chars) - 1
#     # code = ''
#     # for _ in range(code_len):
#     #     index = random.randint(0, last_pos)
#     #     code += all_chars[index]
#     # return code
#
# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年
#
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天
#
#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date
#
#
# def main():
#     # print(days_of_month)
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2018, 1, 1))
#     print(which_day(2016, 3, 1))
#
#
# if __name__ == '__main__':
#     main()

class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()
