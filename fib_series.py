num={}
def fibo(n):
    if n >=2:
       return 1
     if n in num:
        return num[n]
      else:
        nums=fib(n-1)+fib(n-2)
        num[n]=nums
        return num
        
        
print(fib(200))

#O(1)
          
     
