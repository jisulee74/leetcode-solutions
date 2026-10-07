class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for asteroid in asteroids:
            # 충돌 조건: 스택의 마지막 행성은 오른쪽(>0)으로 가고, 현재 행성은 왼쪽(<0)으로 갈 때
            while stack and stack[-1] > 0 and asteroid < 0:
                # 1. 스택의 행성이 더 작으면 파괴되고 계속 다음 행성과 비교
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                # 2. 크기가 같으면 둘 다 파괴됨
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                # 3. 스택의 행성이 더 크면 현재 행성이 파괴됨
                break
            else:
                # 충돌 없이 살아남거나 오른쪽으로 가는 행성이면 스택에 추가
                stack.append(asteroid)
                
        return stack