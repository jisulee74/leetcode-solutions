class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        # 충돌 조건: 직전 소행성은 오른쪽(>0), 새로운 소행성은 왼쪽(<0)
        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                # 새로운 소행성이 더 크면 연속 충돌 가능성 존재함
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                   
                break
            else:
                stack.append(asteroid)
        return stack