class Solution(object):
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0:
            return []
        EDS={}
        for i, n in enumerate(nums):
            EDS[n] = [1, i]
        nums.sort() #sort the list, takes O(n.log(n))
        largest = 1
        max_n = nums[0]
        for i, n in enumerate(nums): #find EDS(nums(i))
            maxsub = 0  #maximum subset size
            max_item = nums[0] # biggest element in the divisible set so far
            for j in range(i, -1, -1):
                if (nums[i] % nums[j] == 0 and nums[i] != nums[j]):
                    if EDS[nums[j]][0] > maxsub:
                        maxsub = EDS[nums[j]][0]
                        max_item = nums[j]
            EDS[nums[i]] = [(1+ maxsub), max_item] #current biggest divisible set must be 1 + the size of previous divisible subset
            if EDS[nums[i]][0] > largest: #record the biggest divisible subset
                largest = EDS[nums[i]][0]
                max_n = nums[i]
        #reconstruct the largest divisible subset from the biggest size and previous element
        result = [max_n]
        n = max_n
        while EDS[n][0] != 1:
            result.append(EDS[n][1])
            n = EDS[n][1]
        return result
        
            
        
            
                
                
                    
            
        