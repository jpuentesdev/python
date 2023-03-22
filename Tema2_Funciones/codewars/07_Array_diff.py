#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

'''
''' Sólo se borra el número una vez, si están repetidos no funciona
def array_diff(a, b):
    for nums in a:
        if nums in b:
            for nums in b:
                a.remove(nums)
        
    return a

print(array_diff([1,2,3,4],[2,1]))

'''

def array_diff(a, b):
    return [x for x in a if x not in b]
        

print(array_diff([1,2,3,4],[2,1]))