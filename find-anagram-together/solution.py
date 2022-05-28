from collections import defaultdict

def Anagrams(words):
    temp = defaultdict(list)
    
    for el in words:
        temp[str(sorted(el))].append(el)
    
    res = list(temp.values())
    return res



samples = ["beriln", "cat", "atc", "berlin", "acet", "linber"]
print(Anagrams(samples))