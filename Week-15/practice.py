class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for ast in asteroids:
            # We only have a collision if the stack has a RIGHT-moving asteroid
            # and the current asteroid is LEFT-moving.
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                
                if diff < 0:
                    # The incoming left-asteroid is bigger. Top of stack explodes.
                    stack.pop()
                    # The loop continues to see if 'ast' destroys the next item.
                elif diff > 0:
                    # The top of stack is bigger. Incoming 'ast' explodes.
                    break
                else:
                    # Both are equal size. Both explode.
                    stack.pop()
                    break
            else:
                # This 'else' belongs to the while loop!
                # It executes ONLY if the loop finishes normally without hitting a 'break'.
                # It means 'ast' survived all collisions, or there were no collisions to start with.
                stack.append(ast)
                
        return stack