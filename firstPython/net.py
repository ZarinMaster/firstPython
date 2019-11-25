# -*- coding: utf-8 -*-
# @Time : 2019/11/25 16:09
# @Author : ZarinMaster
# @Site : 
# @File : net.py
# @Software: PyCharm

from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'grant_reg@163.com'
    receivers = 'dugang106@163.com'
    mailText = '用Python发送邮件的示例代码.\n' + \
               '第2行\n' + \
               '第3行'
    try:
        with open('.res/getDB.sql', 'r', encoding='utf-8') as f:
            mailText = f.read()
    except FileNotFoundError as e:
        print(e)
        print('文件未找到')
    except IOError:
        print('文件打开失败')
    finally:
        f.close()
    message = MIMEText(mailText, 'plain', 'utf-8')
    message['From'] = '王大锤' + '<grant_reg@163.com>'
    message['To'] = 'dugang106<dugang106@163.com>'
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'auth163')
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
