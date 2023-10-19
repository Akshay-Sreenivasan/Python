#  		    1 
#          1 1 
#         1 2 1 
#        1 3 3 1 
#       1 4 6 4 1 
#      1 5 10 10 5 1 
#     1 6 15 20 15 6 1 
#    1 7 21 35 35 21 7 1 
#   1 8 28 56 70 56 28 8 1
from math import factorial
n = int(input('Enter the limit: '))
for i in range(n):
	for j in range(n-i+1):
		print(end=" ")
	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	print()
