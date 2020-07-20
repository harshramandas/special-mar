# Fibonacci Series:  Probably the most famous of all Mathematical sequences; it goes like this—- 1,1,2,3,5,8,13,21,34,55,89…

# At first glance one may wonder what makes this sequence of numbers so sacrosanct or important or famous. However a quick inspection shows that it begins with two1 s and continues to get succeeding terms by adding, each time, the last two numbers to get the next number
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
