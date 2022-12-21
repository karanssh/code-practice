from typing import List 

def asteroidCollision(asteroids: List[int]) -> List[int]:
        s = []
        i = 0
        while i < len(asteroids):
            asteroid = asteroids[i]
            if len(s) > 0 and s[-1] > 0 and asteroid < 0:
                if abs(asteroid) > s[-1]:
                    s.pop() 
                elif abs(asteroid) == s[-1]:
                    s.pop() 
                    i += 1
                else:
                    i += 1
            else:
                s.append(asteroid)
                i += 1
            
        return s
        


asteroidCollision([-5,-10,-5])