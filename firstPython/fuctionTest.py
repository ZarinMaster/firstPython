"""
fuctionTest

Version: 0.1
Author: ZarinMaster
"""

# from fuc1 import testFuc
# testFuc('boy','girl')
# from fuc2 import testFuc
# testFuc('girl','papa','daughter')

# import fuc1 as f1
# import fuc2 as f2
#
# f1.testFuc('a', 'b', 'c', 'd')
# f2.testFuc('1', '2')


list1 = [1, 3, 5, 7, 100]
list1.insert(2, 28)
print(list1)
# list2 = list1[:]
list2 = sorted(list1, reverse=True)
# print('list2:')
# list2.sort()
# for index, elem in enumerate(list2):
#     print(index, elem)
print('list1:')
print(list1)
print('list2:')
print(list2)

f = [x for x in range(1, 12, 3)]
print(f)
