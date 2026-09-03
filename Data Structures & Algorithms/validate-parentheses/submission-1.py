class Solution:
    def isValid(self, s: str) -> bool:

        parentheses =  {'(':')', '{':'}', '[' :']'}
        stack = []

        for char in s : 

            if char in parentheses.values() : 
                if not stack : 
                    return False 
                if parentheses[stack[-1]] == char : 
                    stack.pop()
                else : 
                    return False 
            else : 
                stack.append(char)
        return stack == []
        

        