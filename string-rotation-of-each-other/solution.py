def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True

    s1_org = s1

    while True:
        s1 = s1 + s1[0]
        s1 = s1[1:]
        if s1 == s2:
            return True
        elif s1 == s1_org:
            return False
