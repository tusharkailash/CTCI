#Implement an algorithm to determine if a string has all unique characters.


class Solution(object):
    def unique_char(self,str):
        if len(str) > 128:          #ASCII range : 0 to 127
            return False

        arr = [False] * 128

        for i in str:
            if arr[ord(i)] is False:
                arr[ord(i)] = True
            else:
                return False
        return True

str = "abcedfghie"
print Solution().unique_char(str)
