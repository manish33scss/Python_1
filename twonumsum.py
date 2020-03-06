# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 00:03:23 2020

@author: Manish
"""##problem : Find the two numbers in list whose sum is equal to a target sum.

def numsum(array, targetsum):
    nums={}
    for num in array:
        potential_match = targetsum - num
        if potential_match in nums:
            return [potential_match,num]
        else:
            nums[num]=True
    return []

o=[1,2,5,6,7,9,7,5,9,1,4,0]
tsum=5

zx=numsum(o,tsum)

print(zx)

def sumnum(array,tsum):
    for i in range(len(array)-1):
        firstN= array[i]
        for j in range(i+1,len(array)):
            secN=array[j]
            if firstN+secN==tsum:
                return [firstN,secN]
    return[]
    
z=[1,2,3,4,5,4,3,0,9]
tsum=9


print(sumnum(z,tsum))
