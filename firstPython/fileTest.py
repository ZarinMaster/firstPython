"""
fuction2

Version: 0.1
Author: ZarinMaster
"""

# import time
import json


# import exception



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
        print("例子1程序执行结束！")
    # 例子2开始
    myDict = {
        'name': 'Zarin-DG',
        'gender': 'male',
        'age': '31',
        'books': [
            {'coding': '《C++编程指南》',
             'history': '《史记》',
             'music': '《巴赫和贝多芬》'}
        ]
    }
    try:
        with open('.res/myDict.json', 'w', encoding='utf-8') as fjson:
            json.dump(myDict, fjson)
    except IOError as e:
        print(e)
    finally:
        print('例子2执行结束！')
    # print(dir(exception))


if __name__ == '__main__':
    main()
