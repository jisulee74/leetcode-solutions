class Solution:
    def duplicateZeros(self, arr):
        zeros = arr.count(0)
        n = len(arr)
        
        i = n - 1
        # Position where the last element would end up when zeros are duplicated
        j = n + zeros - 1 
        
        while i >= 0:
            # Copy value if the target position is within the actual array bounds
            if j < n:
                arr[j] = arr[i]
             # If the current value is 0, we need to duplicate it, so shift j to the left and insert another 0
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            
            i -= 1
            j -= 1