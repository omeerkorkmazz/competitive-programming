def isAnagram(self, a, b):

    if len(a) != len(b):
        return False

    char_dic = {}

    for c in a:
        if c not in char_dic:
            char_dic[c] = 1
        else:
            char_dic[c] += 1

    for c in b:
        if c not in char_dic:
            return False
        else:
            char_dic[c] -= 1

    for key in char_dic:
        if char_dic[key] != 0:
            return False

    return True
