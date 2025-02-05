from typing import List

def puzz(first_list:List[int],second_list:List[int])->bool:
    if len(first_list) != len(second_list):
        return False
    c = first_list[0] + second_list[0]
    for i in range(len(first_list)):
        if first_list[i] + second_list[i] != c:
            print("False")
            return False
    else:
            print("True")
            return True
    
puzz([5,5,3,5], [1,1,1,1])