class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False
        
        i = 0
        
        # 1. Walk up the mountain (strictly increasing)
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
            
        # Peak cannot be the first or the last element
        if i == 0 or i == n - 1:
            return False
            
        # 2. Walk down the mountain (strictly decreasing)
        while i + 1 < n and arr[i] > arr[i+1]:
            i += 1
            
        # If we reached the end, it's a valid mountain array
        return i == n - 1