class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        c_dict = {}

        for n in nums:
            if n in c_dict:
                x = c_dict[n] + 1
                c_dict.update({n:x})
            else:
                c_dict.update({n:1})
        
        sorted_items = sorted(c_dict.items(), key=lambda item: item[1], reverse=True)
        
        result = []
        for item in sorted_items[:k]:
            result.append(item[0])
            
        return result
            