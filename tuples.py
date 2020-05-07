te = () # empty tuple...immutable
t = (2 , 'mit', 3)
print(t[0]) #2
'''work like lists or array data type in JS'''

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        print( (t[1],))
        nums = nums + (t[0],)
        '''if t[1] not in words:
            words = words + (t[1])
'''
        print(nums)




test = ((1, 'a'), (2, 'b'), (1, 'a'), (7, 'b'))

get_data(test)
#print(get_data(test))


