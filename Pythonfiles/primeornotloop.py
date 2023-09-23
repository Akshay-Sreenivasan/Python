# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97---prime numbers
i=2
a=int(input('Enter a number'))
while i<a:
    if((a%i)==0):
        print('Number  is not a Prime Number')
    i=i+1
else:
    print('Number is a Prime Number')
