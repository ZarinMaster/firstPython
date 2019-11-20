"""
猜数字：1-100范围的整数，系统提示大一点，小一点，直到猜中。

Version: 0.1
Author: 骆昊
Author: ZarinMaster
"""

import random

answer = random.randint(1, 100)
count = 0
while True:
    count += 1
    number = int(input('请输入：'))
    if number > answer:
        print('大了！')
    elif number < answer:
        print('小了！')
    else:
        print('Bingo!')
        break

if count > 10:
    print('您居然猜了%d次，超过了10次！该吃药了！' % count)
else:
    print('您一共猜了%d次' % count)
