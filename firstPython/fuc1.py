"""
fuction1

Version: 0.1
Author: ZarinMaster
"""


def testFuc(*gender):
    theGender = '|'
    for e in gender:
        theGender+='|'
        theGender += e
    print('hello world!%s' % theGender)
