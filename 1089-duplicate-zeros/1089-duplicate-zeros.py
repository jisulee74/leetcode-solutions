class Solution:
    def duplicateZeros(self, arr):
        zeros = arr.count(0)
        n = len(arr)
        
        i = n - 1
        j = n + zeros - 1 # 0이 복제되었을 때 최종적으로 끝나는 위치
        
        while i >= 0:
            # 만약 j가 실제 배열 범위(n) 안에 있다면, 값을 복사
            if j < n:
                arr[j] = arr[i]
             # 만약 현재 값이 0이라면, 0을 한 번 더 복제해야 하므로 j를 한 칸 앞으로 옮겨서 또 0을 넣
            if arr[i] == 0:
                j -= 1
                if j < n:
                    arr[j] = 0
            
            i -= 1
            j -= 1