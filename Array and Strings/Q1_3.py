#Given two strings, write a method to decide if one is a permutation of the other

def permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    dic = {}
    for i in str1:
        dic[i] = dic.get(i,0) + 1
    for i in str2:
        if dic.get(i,0) < 0:
            return False
        else:
            dic[i] -= 1
    return True



string1 = "coding"
string2 = "dincgo"
print permutation(string1,string2)
