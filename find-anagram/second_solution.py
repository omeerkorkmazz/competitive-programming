from collections import defaultdict

def isAnagram(self, a, b):

    if len(a) != len(b):
        return False

    if sorted(a) != sorted(b):
        return False

    return True
