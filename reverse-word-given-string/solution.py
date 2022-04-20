def reverseWords(S):
    reverseStr = ""
    end = len(S)

    for i in range(len(S)-1, -1, -1):
        if S[i] == '.':
            if reverseStr == "":
                reverseStr = reverseStr + S[i+1:end]
            else:
                reverseStr = reverseStr + "." + S[i+1:end]
            
            end = i
        
        if i == 0:
            if reverseStr == "":
                reverseStr = reverseStr + S[:end]
            else:
                reverseStr = reverseStr + "." + S[:end]
            
    return reverseStr

print(reverseWords("sample.john.foo"))