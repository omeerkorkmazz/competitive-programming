def dictionary_contains(word, dictionary):

    if word in dictionary:
        return True
    else:
        return False


def is_word_segmented(line, dictionary):
    line_len = len(line)
    dp = [False] * (line_len + 1)

    for i in range(0, line_len+1):
        if dp[i] == False and dictionary_contains(line[:i], dictionary):
            dp[i] = True

        if dp[i] == True:
            if i == line_len:
                return True

            for j in range(i+1, line_len+1):
                if dp[j] == False and dictionary_contains(line[i:j], dictionary):
                    dp[j] = True

                if dp[j] == True and j == line_len:
                    return True

    return False


words = ["i", "like","you"]
line = "ilike"

print(is_word_segmented(line,words))
