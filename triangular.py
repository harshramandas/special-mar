# A triangular number or triangle number counts objects arranged in an equilateral triangle, as in the diagram on the right. The n-th triangular number is the number of dots composing a triangle with n dots on a side, and is equal to the sum of the n natural numbers from 1 to n.



def triangular_series(n):

     for i in range(1, n + 1):
         print( i*(i+1)//2,end=' ')
triangular_series(int(input("Enter the nth term")))
