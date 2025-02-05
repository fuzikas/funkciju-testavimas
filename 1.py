

def puzzle_sum(first_list:list,second_list:list)->bool:
    if len(first_list) != len(second_list):
        print("False")
        return False
    my_list = []
    for i in range(len(first_list)):
        my_list.append(first_list[i]+second_list[i])
    if len(set(my_list)) ==1:
        print("True")
        return True
    else:
        print("False")
        return False
    

puzzle_sum([2,2,2,2], [2,3,2,2])




