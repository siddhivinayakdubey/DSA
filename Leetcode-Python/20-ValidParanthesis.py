from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for i in range(0,len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            else:
                if len(stack)!=0:
                    if s[i]==')' and stack[len(stack)-1]=='(' or s[i]==']' and stack[len(stack)-1]=='[' or s[i]=='}' and stack[len(stack)-1]=='{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
