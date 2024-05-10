
nums = [1,2,3]
class Solution:
    def containsDuplicate(self, nums: list[int]) ->bool:

        hash = set()

        for i in nums:
            if i in hash:
                return True
            hash.add(i)
        return False
    
# Create an instance of the Solution class
solution = Solution()


# Call the function and print the result
print(solution.containsDuplicate(nums))