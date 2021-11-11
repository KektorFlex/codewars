'''
Your goal in this kata is to implement a difference function,
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present
in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be
removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''
#Не прошло все тесты - список b может быть больше списка a
#def array_diff(a, b):
#    a_list = []
#    for num_1 in a:
#        a_list.append(num_1)
#    for num_2 in b:
#        for num_1 in a:
#            if num_2 == num_1:
#                a_list.remove(num_1)
#    print(a_list)
#
#
#array_diff([1,2,2,2,3],[2])


def array_diff(a, b):
    a_list = []
    for num in a:
        if num not in b:
            a_list.append(num)
    print(a_list)


array_diff([1,2,2,2,3],[2])

#Самый лучший вариант
#def array_diff(a, b):
#    return [i for i in a if i not in b]