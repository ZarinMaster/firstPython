# -*- coding: utf-8 -*-
# @Time : 2019/11/26 16:07
# @Author : ZarinMaster
# @Site :
# @File : mailSend.py
# @Software: PyCharm

from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

import yaml


# class emailClass(object):
#     # __slots__ = ('_sender', '_receivers')
#
#     def __init__(self):
#         self.currentTime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#         yaml.load(open('.res/mailConfig.yaml'))

class MyMail(object):
    def __init__(self, sender, receiver, server, title, text):
        self._sender = sender
        self._receiver = receiver
        self._server = server
        self._title = title
        self._text = text

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, server):
        self._server = server

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def sendMail(self):
        # 请自行修改下面的邮件发送者和接收者
        # sender = 'grant_reg@163.com'
        # receivers = 'dugang106@163.com'
        # mailText = '用Python发送邮件的示例代码.\n' + \
        #            '第2行\n' + \
        #            '第3行'
        # try:
        #     with open('.res/getDB.sql', 'r', encoding='utf-8') as f:
        #         mailText = f.read()
        # except FileNotFoundError as e:
        #     print(e)
        #     print('文件未找到')
        # except IOError:
        #     print('文件打开失败')
        # finally:
        #     f.close()
        message = MIMEText(self._text, 'plain', 'utf-8')
        # message['From'] = '王大锤' + '<grant_reg@163.com>'
        # message['To'] = 'dugang106<dugang106@163.com>'
        # message['Subject'] = Header('示例代码实验邮件', 'utf-8')
        # smtper = SMTP('smtp.163.com')
        message['From'] = self._sender
        message['To'] = self._receiver
        message['Subject'] = Header(self._title, 'utf-8')
        smtper = SMTP(self._server)
        # 请自行修改下面的登录口令
        try:
            smtper.login(self._sender, 'auth163')
            smtper.sendmail(self._sender, self._receiver, message.as_string())
        except Exception as e:
            print(e)
            print('邮件发送失败！')
        else:
            print('邮件发送完成!')
        finally:
            smtper.quit()

    sendadd = 'grant_reg@163.com'
    receivadd = 'dugang106@163.com'


def get_mail_conf():
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
        print(myyaml['people'][1]['addr'])
    # open自带关闭功能
    # finally:
    #     f.close()
    return myyaml


def main():
    mconf = get_mail_conf()

    mail1 = MyMail('grant_reg@163.com', 'dugang106@163.com', 'smtp.163.com', '测试title', 'mailText')
    mail1.sendMail()
    print(mconf)
    for item in mconf['people']:
        print(item['addr'])


if __name__ == '__main__':
    main()
