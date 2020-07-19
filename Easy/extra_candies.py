#Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

#For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have 
#the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

#Example:
#Input: candies = [2,3,5,1,3], extraCandies = 3
#Output: [true,true,true,false,true] 

def kidsWithCandies(self, candies, extraCandies):
    max_candies = max(candies)
    for i, kid in enumerate(candies):
        candies[i] = (candies[i] + extraCandies >= max_candies)
    return candies