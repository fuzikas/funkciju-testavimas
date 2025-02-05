def puzz(a,b):
    if len(a) != len(b):
        return False
    c = a[0] + b[0]
    for i in range(len(a)):
        if a[i] + b[i] != c:
            print("False")
            return False
    else:
            print("True")
            return True
    
puzz([5,5,5,5], [1,1,1,1])