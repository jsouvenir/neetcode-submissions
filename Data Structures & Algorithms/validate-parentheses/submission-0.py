class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for c in s: #loop through chars in s
            if c in closeToOpen: # checks if closed bracket
                if stack and stack[-1] == closeToOpen[c]:
                    #if stack is not empty and the open bracket matches
                    #the closed bracket: remove the closed bracket
                    stack.pop()
                else: #brackets dont match return false
                    return False
            else: #append open brackets
                stack.append(c)
        
        return True if not stack else False


        