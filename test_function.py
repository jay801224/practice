import numpy as np

inputnum = int(input("請輸入要驗證的資料:"))
inputnumst = [int(n) for n in str(inputnum)]
print (inputnum)
print (len(inputnumst),inputnumst)
inputnumst.reverse()
print (inputnum)
print (len(inputnumst),inputnumst)






inputnum2 = input("請輸入要驗證的資料:").split()
array = np.array(inputnum2)
revarray = array[::-1]
print (inputnum2)
print (array)
print (revarray)

#正矩正解法
def verified_valuea ():
    if array[0] == array[-1] and array[1] == array[-2] :
        print ("pass AB")
        return True
    elif array[0] == array[-1] and array[1] != array[-2] :
        print ("pass A")
        return False
    elif array[0] != array[-1] and array[1] == array[-2] :
        print ("pass B")
        return False  
    else :
        print ("all failed")
        return False

#正反矩正解法
def verified_valueb ():
    if array[0] == revarray[0] and array[1] == revarray[1] :
        print ("pass AB")
        return True
    elif array[0] == revarray[0] and array[1] != revarray[1] :
        print ("pass A")
        return False
    elif array[0] != revarray[0] and array[1] == revarray[1] :
        print ("pass B")
        return False    
    else :
        print ("all failed")
        return False

print ( verified_valuea())