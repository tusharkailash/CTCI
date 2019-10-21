#Implement a function which reverses a null terminated string.

class Solution(object):
    def reverse(self,str):
        start = 0
        end = len(str) - 1
        str = list(str)
        while start <= end:
            str[start], str[end] = str[end],  str[start]
            start += 1
            end -= 1
        return "".join(str)

str = "Program"
print Solution().reverse(str)
