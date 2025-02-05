

def puzzle_sum(a,b):
    if len(a) != len(b):
        print("False")
        return False
    my_list = []
    for i in range(len(a)):
        my_list.append(a[i]+b[i])
    if len(set(my_list)) ==1:
        print("True")
        return True
    else:
        print("False")
        return False
    

puzzle_sum([2,2,2,2], [2,2,2,2])




