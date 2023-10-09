# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input 
# would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
num=[2,5,4,9,1]
target=6
i=0
while (i<len(num)):
    for k in range(len(num)):
        sum=num[i]+num[k]
        if(sum==target):
            print([i],[k])
    i=i+1