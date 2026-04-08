class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # We assume size > 0 when popback is called based on problem constraints
        self.size -= 1
        val = self.arr[self.size]
        
        # YOUR memory optimization: Clear the unused spot
        self.arr[self.size] = 0 
        
        return val

    def resize(self) -> None:
        # Handle the edge case where capacity is exactly 0
        if self.capacity == 0:
            self.capacity = 1
        else:
            self.capacity *= 2
            
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size        
    
    def getCapacity(self) -> int:
        return self.capacity