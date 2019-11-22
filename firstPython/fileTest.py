"""
fuction2

Version: 0.1
Author: ZarinMaster
"""

import time


def main():
    try:
        # # 一次性读取整个文件
        # with open('.res/getDB.sql', 'r', encoding='UTF-8') as f:
        #     print('-----file begin------')
        #     print(f.read())
        #     print('-----file end------')
        # # for in 循环读取
        # with open('.res/getDB.sql', 'r', encoding='UTF-8') as f:
        #     print('open by for-in')
        #     for line in f:
        #         print(line)
        # 按行以列表形式读取
        with open('.res/getDB.sql', 'r', encoding='UTF-8') as f1:
            fline = f1.read()
        print('readlines begin ')
        print(fline)
        # fline+=''
        # 读取空文件，然后写入
        print('开始写文件')
        with open('.res/writeSql.txt', 'w') as f2:
            f2.write(fline)
        print(fline)
    except FileNotFoundError as e:
        print(e)
        print("未找到指定文件！")
    except IOError as e:
        print(e)
        print("文件打开失败！")
    finally:
        print("程序执行结束！")


if __name__ == '__main__':
    main()
