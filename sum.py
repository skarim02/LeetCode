class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, value in enumerate(nums):
            n = target - value
            if n in seen:
                print (seen[n],idx)
                #return (seen[n],idx)
            else:
                seen[value] = idx
                #print (value,seen[value])



test = Solution()
test.twoSum([3,2,3],5)
