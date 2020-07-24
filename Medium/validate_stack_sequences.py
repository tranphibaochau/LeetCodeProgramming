#Given two sequences pushed and popped with distinct values, 
#return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

#Hint: Greedy Algorithm
def validateStackSequences(pushed, popped):
    result = []
        l = 0
        for n in pushed:
            result.append(n)
            while result and result[-1] == popped[l]: #pop the stack as long as you see it at the top of the popped
                result.pop()
                l+=1
        return not result