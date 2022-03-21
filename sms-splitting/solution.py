import os


def segments(message):
    MAX_LEGTH_WITH_SUFFIX = 155  # (1/5) 5 chars
    message_len = len(message)
    segment_count = (message_len // 160) + 1
    message_segments = []

    # less than 2 segments
    if segment_count <= 1:
        message_segments.append(message)
        return message_segments

    start = 0
    end = MAX_LEGTH_WITH_SUFFIX

    for i in range(0, segment_count):
        word = message[start:end]

        if message_len >= end + 1 and message[end] != ' ':
            counter = 0
            hasSpace = False
            word_len = len(word)

            while(hasSpace is False):
                if word[word_len - counter - 1] != ' ':
                    counter += 1
                else:
                    hasSpace = True

            word = message[start:end-counter]
            word = word + "(" + str(i + 1) + "/" + str(segment_count) + ")"
            message_segments.append(word)

            start = end-counter
            end = end-counter + MAX_LEGTH_WITH_SUFFIX
        else:
            word = word + "(" + str(i + 1) + "/" + str(segment_count) + ")"
            message_segments.append(word)
            start = end
            end += MAX_LEGTH_WITH_SUFFIX

    return message_segments


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    result = segments(message)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
