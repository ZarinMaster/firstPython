"""
fuction2

Version: 0.1
Author: ZarinMaster
"""


def testFuc(*gender):
    theGender = '|'
    for e in gender:
        theGender += e
    print('goodbye world!%s' % theGender)
