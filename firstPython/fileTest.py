"""
fuction2

Version: 0.1
Author: ZarinMaster
"""

# import time
import json

import yaml


# import exception


def TryFile():
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


def getFile():
    myfile = {
        'name': 'ZarinMaster',
        'age': 38,
        'qq': 12345

    }
    try:
        # 要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。
        # 注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常。
        # 既可以读，又可以写，用+
        with open('.res/mailConfig.yaml', mode='r', encoding='utf-8') as f:
            # yaml.dump(myfile, f)
            myyaml = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    else:
        print('文件打开成功！')
        print(myyaml['people'][1]['emAddr'])
    # open自带关闭功能
    # finally:
    #     f.close()
    return myfile


def main():
    print(getFile())
    pass


if __name__ == '__main__':
    main()
