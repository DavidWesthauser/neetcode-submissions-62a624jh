class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        
        # Step 2: Convert the map items into a list suitable for sorting.
        # The items are (element, frequency).
        items = list(frequency_map.items())
        
        # Step 3: Sort the items based on their frequency (the second element, index 1).
        # We use lambda x: x[1] as the key and set reverse=True for descending order 
        # (highest frequency first).
        items.sort(key=lambda item: item[1], reverse=True)
        
        # Step 4: Select the top k elements and return only the element values (index 0).
        result = []
        for i in range(k):
            # items[i] is a tuple (element, frequency)
            element = items[i][0]
            result.append(element)
            
        return result