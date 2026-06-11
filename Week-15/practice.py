asteroids = [5,10,-5]
stack = []
for ast in asteroids:
          
    while stack and ast < 0 and stack[-1] > 0:
        diff = ast + stack[-1]
        if diff < 0:
              stack.pop()
        elif diff > 0:
              break
        else:
              stack.pop()
              break
    else:
            stack.append(ast)
                


print(stack)