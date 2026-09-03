class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # The rightmost element has no elements to its right, so its initial max value is -1
        max_from_right = -1
        
        # Traverse the array backwards from the last element to the first element
        for i in range(len(arr) - 1, -1, -1):
            # Temporarily store the current element before overwriting it
            current = arr[i]
            
            # Replace the current element with the maximum value found to its right
            arr[i] = max_from_right
            
            # Update max_from_right if the current element is greater than the previous maximum
            if current > max_from_right:
                max_from_right = current
                
        return arr