"""

Given a circular array (the next element of the last element is the first element of the array), 

print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to 

its traversing-order next in the array, which means you could search circularly to find its next greater number. 

If it doesn't exist, output -1 for this number.

"""

##############################################################################################################################




'''
The idea here is to store the indexes of the elements that we haven't seen a greater than value for them yet
we do this because if you stored the values you wouldn't be able to easily know where a value is at so you
can set it accordingly. This comes in handy in the second loop.

The values in the stack when we enter the second loop will always be decending, this is an important part of knowing that 
we are setting the indexes to their correct value. Since we always will set the index's left in the stack to the smallest
number when reiterating over the stack, ensuring a correct answer. 
'''


def nextGreaterElements(self, nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
            
    return result