"""
Question 1 - Leetcode

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up
 to target.

You may assume that each input would have exactly one
solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""

def twoSum(arr, target):

    for num in arr:
        for num2 in arr:
            if num + num2 == target:
                return [arr.index(num),arr.index(num2)]

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))