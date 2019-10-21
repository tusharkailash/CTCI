# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become
# a2blc5a3. If the "compressed" string would not become smaller than the original
# string, your method should return the original string.


class Solution(object):
    def strcompress(self,word):
        output = ''
        count = 1
        prev = ''

        for i in range(1,len(word)-1):
            prev = word[i-1]
            if word[i] == prev:
                count += 1
            else:
                output = output + prev
                output = output + str(count)
                prev = word[i]
                count = 1
        output = output + prev
        output = output + str(count)

        if len(output) < len(word):
            return output
        else:
            return word


print Solution().strcompress("abbcccdddd")
