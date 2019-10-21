# Assume you have a method isSubstring which checks if one word is a
# substring of another. Given two strings, si and s2, write code to check if s2 is
# a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle"is a rotation
# of "erbottlewat").


def isRotation(str1,str2):
    if len(str1)!=len(str2):
        return False
    else:
        str1 += str1
        output = isSubstring(str1,str2)
    return output

def isSubstring(str1,str2):
    if str2 in str1:
        return True
    else:
        return False

str1 = "waterbottle"
str2 = "erbottlewat"
print isRotation(str1,str2)
