class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):       # b only searches AFTER a
                for k in range(j + 1, n):   # c only searches AFTER b
                    
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]

                    if a + b + c == 0:
                        output.add((a, b, c)) 

        return [list(triplet) for triplet in output]