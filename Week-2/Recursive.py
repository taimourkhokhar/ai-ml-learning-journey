def find_sum(n):
  # sum=0
  # for i in range(2,n+1):
  #   sum+=i
  # return sum
  #recusrve approach
#   if n==1:
#     return 1
#   return n+find_sum(n-1)


# if __name__=='__main__':
#   print(find_sum(5))




  #fibonanaci number


  def fib(n):
    if n==0 or n==1:
      return n
    return fib(n-1)+fib(n-2)



  if __name__=='__main__':
   print(fib(6))