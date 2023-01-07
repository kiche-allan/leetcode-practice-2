# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# The problem can be solved using the brute force aproach



# The below class of solution takes in the method (twoSum) and two arguments - a lis of intergers nums and an interger target
# The method has a return type of List[int] which is a list of intergers


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    #create a dictionary to store the indices of the elements in the array
    indices = {}
    #this creates an empty dictionary called indices which will be used to store the indices of the elements in the array
    
    #we then reiterate through the array
    #thi starts for a loop that iterates troough the elemenets in the 'nums' array. The enumerate function adds a counter to the loo[ so that the index of each element can be accessed. The loop variables 'i' and 'num' represent the index and value of the current element, respectively. 
    for i, num in enumerate(nums):
        #next is to check if the target - nums in in the dictionary, it means that there is no element in the array that, when added to the current element, sums up to the target. In tis case, the current element and its index are added to the 'indices' dictionary
        indices[num] = i
      #next is to return an empty list  
        return []
        