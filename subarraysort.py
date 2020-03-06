"""
Question : 1. Find smallest subarray. Given an array of integers, find out the 

following
(i) unsorted numbers.
(ii) min and max of unsorted numbers
(iii) their acutal position. <--- to return


"""
def subarraysort(array):
    min_out_of_order=float("inf")
    max_out_of_order=float("-inf")
    for i in range(len(array)):
        num=array[i]
        
        if is_out_of_order(i,num,array):
            min_out_of_order=min(min_out_of_order,num)
            max_out_of_order=max(max_out_of_order,num)
    if    min_out_of_order==float("inf"):
        return [-1,-1]
    subarrayLeftIdx=0
    
    while min_out_of_order>=array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
        
    subarrayRightIdx=len(array)-1
    while max_out_of_order<=array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    print("Min outt of order number is {} and max out of order is {} \n Their position is :".format(min_out_of_order,max_out_of_order))
    #print (".........", array[subarrayLeftIdx], array[subarrayRightIdx]) 
    return [subarrayLeftIdx,subarrayRightIdx]
    
    
            
            
            
def is_out_of_order(i,num,array):
    if i==0:
        return num>array[i+1]
    if i==len(array)-1:
        return num<array[i-1]
    return num>array[i+1] or num<array[i-1]


        
    
zr=[0,8,78,10,55,36,5,7,99]
subarraysort(zr)
